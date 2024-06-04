import os
import json # 載入 json 標準函式庫，處理回傳的資料格式

from dotenv import load_dotenv

from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 獲取當前目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
print('current_dir:' + current_dir)

# 構建上一層目錄的 .env 檔案路徑
dotenv_path = os.path.join(current_dir, '../', '.env')
print('dotenv_path:' + dotenv_path)

# 加載 .env 檔案
load_dotenv(dotenv_path)
# 讀取環境變數
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
line_authtoken = os.getenv('LINE_AUTHTOKEN')
print('channel_access_token:' + channel_access_token)
print('line_authtoken:' + line_authtoken)

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    # print(body)
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        # access_token = channel_access_token
        # secret = line_authtoken
        line_bot_api = LineBotApi(channel_access_token)      # 確認 token 是否正確
        handler = WebhookHandler(line_authtoken)             # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            reply = msg
        else:
            reply = '你傳的不是文字呦～'
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()
