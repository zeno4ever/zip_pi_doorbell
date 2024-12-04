# Pi Doorbell
DIY smart doorbell based on Raspberry Pi 5

Created for "Workshop: Build your Own Smart Doorbell" workshop [ZIP media Lab Rotterdam](https://zipspace.nl) by Roos Groothuizen & Dave Borghuis

## Needed hardware

- Raspberry Pi 5 (tested with 4 & 5)
- Power adapter (Pi is picky about this so buy the right one.)
- microSD card for OS, minimal 16GB type A1 or better
- Pi Camera (with Pi5 cable)
- USB External speaker (that acts like a soundcard, so no 3,5mm plug!)
- a button
- LED
- 430 Ohm resistor (for led)
- wires to led and button

# Hardware



# Installation

## Camera
You use the flex cable to connect your camera to your pi, follow the instructions on their site. The rasberry pi  automatic recognise this.


## Setup Telegram

We use telegram messages to give you realtime update that someone is standing on the door. 

First create a new private telegram channel where you want to recieve the door notifications. If you want to hear updates enable (sound) notifications for this channel.

### Get your API Token

Get your personal bot token via these [steps](https://core.telegram.org/bots/features#creating-a-new-bot) and save the bot token. 

Add you telegram bot to your channel. (on your phone)

### Channel ID

Log in with your account to [Telegram web](https://web.telegram.org) and select the Telegram group. Then, in the URL of your web browser you should see something similar to https://web.telegram.org/k/#-XXXXXXXXX. Then, the ID you need to use for the Telegram group is -XXXXXXXXX, where each X character represents a number. Remember to include the minus symbol preceding the numbers.

We included a 'test_telegram.py' programm to test and find the right channel number (sometimes the above methode don't give the right number).


## Setup Pi
Make image for your pi with [Pi Imager](https://www.raspberrypi.com/software/), select the correct hardware and "Raspberry Pi OS (64-bit)" as image to create. Select your SD card and wait until the imager is done.

Put the SD card in your Pi and turn it on.  After a quick automatic reboot the pi is ready for use. 

## Pi doorbell scripts
Install the workshop software by opening a terminal on the Pi and clone this repositry to your own local system with :

`git clone https://github.com/zeno4ever/zip_pi_doorbell`

copy 'config.py.example' to 'config.py' with the 'cp' command :
`cp config.py.example config.py`


## Change config.py 
Fill in the parameters you got in the steps from telegram. For the jitsi change the url   part 'your_channel' to your own variation.

chaturl -  f"https://meet.hack42.nl/your_channel#config.prejoinConfig.enabled=false" 
telegram_token - bot API token
telegram_chat - channel id of channel of the door

## modify home directiory in scripts
In the script 'doorbell.py' and 'doorbell.desktop' you have to fill in your own home directory if you user name is different then 'pi'. Look for '/home/pi' and replace 'pi' with your own user name.

# GPIO header pins

We use the header to add some additional hardware to the pi. See [Raspberry documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio) for more informations about the Pi GPIO header pins. 

## LED

- Pin 6 - GND
- Pin 8 - GPIO14


## Button

- Pin 37 - GPIO26
- Pin 39 - GND

## Testing if everyting is connected

Your can see if the camera works with command :
`libcamera-hello`

This should give you a preview of the camera (video) picture for 5 seconds.

Test the sound with 'aplay dingdong.wav', you should hear the doorbell sound. If you hear noting check the audio volumes with command 'alsamixer'

Start firefox and go to the jitsi you configured. Adjust camera and sound setting for jitsi, so next time the system knows what to use.

Final test, in the terminal on the desktop start the script and press the button.

You should hear the dingdong bell, get a message in telegram and the jitsi channel should be joint by the door.

## Autostart the doorbell script

Create the autostart directory this will not exist on a new system.

`mkdir ~/.config/autostart`

In the 'doorbell.desktop' change the paths to the directory where to script is. Move file 'doorbell.desktop' to ~.config/autostart/

`mv doorbell.desktop ~.config/autostart/`

In the 'doorbell.desktop' is a path to your homedirectory. Default we asume this is user 'pi', if this is diferent change it accordingly.

Reboot the pi and wait until its fully booted. Pres the button and enjoy your own DIY smart doorbell.

# Commen mistakes 


# Pi4 speaker alternative
Instead of a USB sound card you can use - Adafruit STEMMA Speaker (ada3885) and 3 pin JST cable with female pin connectors.

## Speaker

- Pin 6 - GND
- Pin 4 - +5V
- Pin 12 - GPIO18 / signal


## Change boot/firmware/config.txt

Add the following lines to the config.txt file after the 'dtparam=audio=on' line.

    audio_pwm_mode=2
    dtoverlay=audremap,pins_18_19

This will set the audio output to the header pins. Reboot the pi to make this active.