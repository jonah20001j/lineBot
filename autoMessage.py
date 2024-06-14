from linebot.models import MessageEvent, TextMessage, TextSendMessage

# @app.route("/")
def autoMessage(line_bot_api, userId):
    # body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    # print(body)
    print('autoMessage userId:' +  userId)
    try:
        # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法
        line_bot_api.push_message(userId, TextSendMessage(text='Hello World!!!'))
        return 'OK'
    except:
        print('error')


        # json_data = json.loads(body)                         # json 格式化訊息內容
        # print(json_data)
        # line_bot_api = LineBotApi(channel_access_token)      # 確認 token 是否正確
        # handler = WebhookHandler(line_authtoken)             # 確認 secret 是否正確
        # signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        # handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        # tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        # type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        # print('type:' + type)
        # if type == 'text':
        #     msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
        #     print('提交給GPT:' + msg)                         # 印出內容
        #     reply = msg
        #     # response = create_chat_completion(msg)
        #     # reply = json.dumps(response, indent=4)

        # else:
        #     reply = '你傳的不是文字呦～'

        # print(reply)
        # line_bot_api.reply_message(tk, TextSendMessage(reply))# 回傳訊息
    # except:
    #     print(body)                                          # 如果發生錯誤，印出收到的內容
    # return 'OK'
