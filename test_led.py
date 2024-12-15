#!/usr/bin/env python3
from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(14)
button = Button(26)

def toggle_led():
    led.on()
    sleep(3)
    led.off()

button.when_pressed = toggle_led

pause()
