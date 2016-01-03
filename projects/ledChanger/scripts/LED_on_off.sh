#!/bin/bash

# find out possible commands
#cat /sys/class/leds/green\:ph24\:led1/trigger
# expected:
#none battery-charging-or-full battery-charging battery-full battery-charging-blink-full-solid 
#ac-online usb-online mmc0 timer heartbeat backlight [gpio] cpu0 cpu1 default-on


echo none > /sys/class/leds/green\:ph24\:led1/trigger


sleep 4


echo default-on > /sys/class/leds/green\:ph24\:led1/trigger


echo press enter

read





