import os
import json # 載入 json 標準函式庫，處理回傳的資料格式
from flask import Flask, request
from openAItools import create_chat_completion
# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from config import channel_access_token, line_authtoken

print('channel_access_token:' + channel_access_token)
print('line_authtoken:' + line_authtoken)

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
    return "test"

# 每次重啟服務的時候 記得把 NGROK 的 Forwarding https://a878-125-227-151-121.ngrok-free.app
# 更新至 lineBot 的 Webhook settings -> Webhook URL

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    print(body)
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        print(json_data)
        line_bot_api = LineBotApi(channel_access_token)      # 確認 token 是否正確
        handler = WebhookHandler(line_authtoken)             # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        print('type:' + type)
        if type == 'text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print('提交給GPT:' + msg)                         # 印出內容
            reply = msg
            # response = create_chat_completion(msg)
            # reply = json.dumps(response, indent=4)

        else:
            reply = '你傳的不是文字呦～'

        print(reply)
        line_bot_api.reply_message(tk, TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
