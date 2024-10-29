#!/usr/bin/env python3
# script for 'smart' doorbell 
# developed for .zip artlab Rotterdam
# by Dave Borghuis
# Sound Effect from pixabay.com 99933

import time
import signal
import subprocess
import os
import uuid
import requests
import config
from config import chaturl,telegram_token,telegram_chat
from gpiozero import Button

doorbell = Button(26,bounce_time=0.2)

def door_ring():
    print("Doorbel Ringing")
    send_notification(chaturl)
    env = os.environ.copy()
    subprocess.Popen(["aplay", "/home/zeno/deurbel/dingdong.wav"])
    process = None
    if not process or not chaturl:
        print("Open url : ",chaturl)
        process = subprocess.Popen(["firefox", chaturl])
    else:
        print("Can't start video chat -- already started or missing chat id")
    time.sleep(100) #video time in seconds
    if process :
        #process.terminate()
        os.kill(process.pid, signal.SIGTERM)
    print("....End")

def send_notification(msg):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {'chat_id': telegram_chat, 'text': '<a href="'+msg+'">There is someone at the door</a>', 'parse_mode': 'HTML','disable_web_page_preview':True}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Telegram message sent url:"+msg)
    else:
        print("Failed to send Telegram message. Status code:"+ str(response.status_code))

def waitforbell():
    print("Setup Doorbell")
    try:
        doorbell.when_released = door_ring
        signal.pause()
    finally:
        print("Setup Failed")

if __name__ == "__main__":
    print('Setup')
    waitforbell()