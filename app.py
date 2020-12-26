from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from random import *


#======python的函數庫==========
import tempfile, os
import datetime
import time
import random
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('channel access token')
# Channel Secret
handler = WebhookHandler('channel secret')

# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg == 'help':
       instruction = '決定現在要吃什麼，是全天下最難的問題,請輸入「吃什麼」，讓我幫你決定吧! ! !'      
       line_bot_api.reply_message(event.reply_token, TextSendMessage(text=instruction))
    if msg == '吃什麼':
        x = random.randint(0,65)
        if x == 0 :
            answer = '煦悅'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 1 :
            answer = '麥當勞'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 2 :
            answer = '肯德基'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 3 :
            answer = '大醬'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 4 :
            answer = '鴨霸'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 5 :
            answer = '牛伯'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 6 :
            answer = '食方味'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 7 :
            answer = '鹿耳晚晚'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 8 :
            answer = 'isaac吐司'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 9 :
            answer = '十六咖哩'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 10 :
            answer = '克林台包'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 11 :
            answer = 'subway'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 12 :
            answer = 'Au主廚_義大利麵'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 13 :
            answer = '傑米廚房'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 14 :
            answer = "am's foods & goods"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 15 :
            answer = '阿財牛肉湯'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 16 :
            answer = '億哥牛肉湯'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 17 :
            answer = '小叉子'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 18 :
            answer = '山大廚房'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 19 :
            answer = '八峰亭_拉麵'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 20 :
            answer = '不好說_料理工作室'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 21 :
            answer = '咖哩意識'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 22 :
            answer = '鴻公公越南河粉'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 23 :
            answer = '鰻丼作'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 24 :
            answer = '性格'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 25 :
            answer = '山禾堂_拉麵'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 26 :
            answer = '覺丸拉麵'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 27 :
            answer = '采田壽司'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 28 :
            answer = '而且鍋燒'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 29 :
            answer = '朱熹漢堡'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 30 :
            answer = '餵公子哥吃餅'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 31 :
            answer = '湧飯'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 32 :
            answer = '寶來軒'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 33 :
            answer = '早到幸胡'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 34 :
            answer = '派克雞排'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 35 :
            answer = '宜華蛋餅'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 36 :
            answer = '金三益'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 37 :
            answer = 'comebuy_海神'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 38 :
            answer = '日船章魚小丸子'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 39 :
            answer = '7-11'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 40 :
            answer = '全家'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 41 :
            answer = '蜷尾家'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 42 :
            answer = '很餃舍'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 43 :
            answer = '日好早午餐'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 44 :
            answer = '迷克夏'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 45 :
            answer = '萱安茶業'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 46 :
            answer = '濰克'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 47 :
            answer = '活力小廚'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 48 :
            answer = 'MASA LOFT'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 49 :
            answer = '生命樹咖啡'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 50 :
            answer = '鳳凰來炸雞'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 51 :
            answer = '我們家'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 52 :
            answer = '元味屋'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 53 :
            answer = '簡單餐飲'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 54 :
            answer = '光餐(光復學生餐廳)'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 55 :
            answer = '醫餐'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 56 :
            answer = '漢堡王'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 57 :
            answer = '輕水煮'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 58 :
            answer = '老夫子牛肉麵'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 59 :
            answer = '築地壽司'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 60 :
            answer = '丹丹漢堡'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 61 :
            answer = '成大館'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 62 :
            answer = '大盒水果'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 63 :
            answer = '唐樓酒吧'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 64 :
            answer = '長鼻子咖哩'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        elif x == 65 :
            answer = '兩餐'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        else:
            answer = 'walking su'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
