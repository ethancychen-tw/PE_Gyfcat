from flask import request, abort, url_for
from app import line_bot_api, handler
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FollowEvent,
    ImageSendMessage,
)

linebotinfo = line_bot_api.get_bot_info()


def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except Exception as e:  # InvalidSignatureError:
        print(e)
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)
    return "OK"


@handler.add(FollowEvent)
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # if registered, reply login link(using token)
    print(f"line event type: {event.type}")
    if event.type != "message":
        return
    line_userId = event.source.user_id  # The attribute is called user_id, surprise lol
    print(f"user id:{line_userId}")
    msg_body = event.message.text
    re_msg = "Unknown command"
    try:
        app_cmd, arg = msg_body.split(" ", 1)

        if app_cmd.lower() == "trending":
            re_msg = url_for("trending")
        elif app_cmd.lower() == "search":
            re_msg = url_for("search", _external=True, search_text=arg)
    except:
        pass
    line_bot_api.reply_message(event.reply_token, TextSendMessage(re_msg))


def send_line(to, msg_body):

    line_bot_api.push_message(
        to, ImageSendMessage(original_content_url=msg_body, preview_image_url=msg_body)
    )
    line_bot_api.push_message(to, TextMessage(text=msg_body))
