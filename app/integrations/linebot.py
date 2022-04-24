from flask import request, abort
from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent, ImageSendMessage

linebotinfo = line_bot_api.get_bot_info()

class LineUser():
    def __init__(self, line_userId):
        self.user_id = line_userId

def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except Exception as e: #InvalidSignatureError:
        print(e)
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(FollowEvent)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # if registered, reply login link(using token)
    print(f"line event type: {event.type}")
    line_userId = event.source.user_id # The attribute is called user_id, surprise lol
    print(f"user id:{line_userId}")

def send_line(to, msg_body):

    line_bot_api.push_message(to, ImageSendMessage(original_content_url=msg_body, preview_image_url=msg_body))
    line_bot_api.push_message(to, TextMessage(text=msg_body))