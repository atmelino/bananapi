#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
PIN_NUM = 7

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)
while True:

	GPIO.output(PIN_NUM,True)
	print "on"
	time.sleep(1)
	GPIO.output(PIN_NUM,False)
	print "off"
	time.sleep(1)

