#!/usr/bin/env python3
from gpiozero import LED, Button
from time import sleep

led = LED(14)

while True:
    led.on()
    sleep(3)
    led.off()
    sleep(3)
