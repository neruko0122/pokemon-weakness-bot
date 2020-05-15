from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction
)
import logic
import constants

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    result = logic.find_pokemon(event.message.text)
    print(result)
    if result != constants.POKEMON_NOT_FOUND_MESSAGE:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=result))
        return
    else:
        suggest_list = logic.find_suggest(event.message.text)
        print(suggest_list)
        if len(suggest_list) == 0:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=result))
            return
        if len(suggest_list) > 10:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='該当件数が多すぎます。'))
            return
        if len(suggest_list) == 1:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='1件該当しました。',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(label="label", text="text"))
                                ]))
            )
            return
        if len(suggest_list) > 1:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='候補から選択して下さい。'))
            return

# text_message = TextSendMessage(text='Hello, world',
#                                quick_reply=QuickReply(items=[
#                                    QuickReplyButton(action=MessageAction(label="label", text="text"))
#                                ]))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)