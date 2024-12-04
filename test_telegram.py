#!/usr/bin/env python3
# script for testing telegram channel 
# developed for .zip artlab Rotterdam
# by Dave Borghuis

import requests
import json
from config import telegram_token,telegram_chat

def send_notification(channel):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {'chat_id': channel, 'text': 'Test Telegram', 'parse_mode': 'HTML','disable_web_page_preview':True}
    return requests.post(url, data=data)


channel = telegram_chat
print("Configured channel ",telegram_chat," Sending test message")

res = send_notification(channel)

if res.status_code == 200:
    print("Succes : Telegram message send.")
else:
    channel = int('-100'+str(telegram_chat).lstrip("-"))
    print("Failed, try with channel +100", channel)
    res = send_notification(channel)
    if res.status_code == 200:
        print("Message send, change telegram_chat in config.py to channel ",channel)
    else:
        # try to read all bot messages and get channel id from that
        print("Failed, Process all messages from bot.")
        url = f'https://api.telegram.org/bot{telegram_token}/getUpdates'
        channel = 0
        response = requests.post(url)

        if response.status_code == 200:
            jsondata=json.loads(response.text)
            for tmsg in jsondata["result"]:
                if "message" in tmsg:
                    chatmsg = tmsg["message"]
                    if "chat" in chatmsg:
                        channel = int(chatmsg["chat"]["id"])
                        print("Testing found channel :",channel)  
                        res2 = send_notification(channel)
                        if res2.status_code == 200:
                            print("Message send, change telegram_chat in config.py to channel ",channel)
            if channel == 0:
                print("No messages available, send a message from your channel  to your bot.")
        else:
            print("Failed to send Telegram message. Status code:"+ str(response.status_code))
