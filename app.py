# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('7LqG17akolgCsUxpkRBZ7elpy7P67gPZZdY9nRhvXx4o/+IerZgFhOpoYZoH6lXdmWg7dF3pa07q3OIRWtpDEPBo4g3TKiK8wTRzHZS1MyeDpODqS3UiNwOLqNIWZqJfnrs2xMjL9+irtKbjCPJlDQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ce45ee51783afbb04cb35ab7b453c943')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()