#!/bin/bash

# find name of LED
#ls -1 /sys/class/leds
# find out what triggers LED currently
#cat /sys/class/leds/beaglebone::usr0/trigger

echo 1 > /sys/class/leds/beaglebone:green:usr3/brightness


sleep 4


echo 0 > /sys/class/leds/beaglebone:green:usr3/brightness



echo press enter

read





