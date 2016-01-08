#!/usr/bin/python
#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import sys


print "arg0="+sys.argv[0]
print "arg1="+sys.argv[1]
print "arg2="+sys.argv[2]
print "arg3="+sys.argv[3]

later=0

if later:

	# create a default object, no changes to I2C address or frequency
	mh = Adafruit_MotorHAT(addr=0x60)
	
	
	################################# DC motor test!
	myMotor = mh.getMotor(3)

	print "Forward! "
	myMotor.run(Adafruit_MotorHAT.FORWARD)
	
	print "\tSpeed up..."
	for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)
	
	print "\tSlow down..."
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)
	
	print "Backward! "
	myMotor.run(Adafruit_MotorHAT.BACKWARD)
	
	print "\tSpeed up..."
	for i in range(255):
		myMotor.setSpeed(i)
		time.sleep(0.01)
	
	print "\tSlow down..."
	for i in reversed(range(255)):
		myMotor.setSpeed(i)
		time.sleep(0.01)
	
	print "Release"
	myMotor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)
