from flask import Flask, request   # 載入 Flask

# 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式
app = Flask(__name__)

# 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
@app.route("/", methods=['POST'])
# 發出請求後會執行 home() 的函式
def home():
    # 執行函式後會回傳特定的網頁內容
    return "<h1>hello world</h1>"

@app.route("/ok", methods=['GET'])
def ok():
    return "<h1>ok</h1>"

@app.route("/yes")
def yes():
    return "<h1>yes</h1>"

@app.route("/args")
def home():
    print(request.args)            # 使用 request.args
    return "<h1>hello world</h1>"

# 執行
app.run(host="0.0.0.0", port=5555)
