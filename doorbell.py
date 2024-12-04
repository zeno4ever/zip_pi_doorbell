#!/usr/bin/env python3
# script for 'smart' doorbell 
# developed for .zip artlab Rotterdam
# by Dave Borghuis
# Sound Effect from pixabay.com 99933

import time
import signal
import subprocess
import requests
from config import chaturl,telegram_token,telegram_chat
from gpiozero import Button, LED

doorbell = Button(26,bounce_time=0.2)
led = LED(14)

def door_ring():
    print("Doorbel Ringing")
    send_notification(chaturl)
    subprocess.Popen(["aplay","-q","/home/pi/zip_pi_doorbell/dingdong.wav"])
    process = None
    led.blink()
    if not process or not chaturl:
        process = subprocess.Popen(["firefox", chaturl])
    else:
        print("Can't start video chat -- already started or missing chat id")
    time.sleep(10)
    led.on()
    time.sleep(100) #video time in seconds
    if process :
        process.terminate()
    led.off()

def send_notification(msg):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    data = {'chat_id': telegram_chat, 'text': '<a href="'+msg+'">There is someone at the door</a>', 'parse_mode': 'HTML','disable_web_page_preview':True}
    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("Failed to send Telegram message. Status code:"+ str(response.status_code))

def waitforbell():
    print("Setup Doorbell")
    try:
        doorbell.when_released = door_ring
        signal.pause()
    finally:
        print("Setup Failed")

if __name__ == "__main__":
    waitforbell()
