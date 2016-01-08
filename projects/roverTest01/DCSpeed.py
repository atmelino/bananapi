#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import sys

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

#atexit.register(turnOffMotors)

################################# DC motor test!
myMotor = mh.getMotor(3)

print "arg1="+sys.argv[1]

arg2=int(sys.argv[2])

#speed=15*sys.argv[2]
speed=20*arg2
print "speed=%d" % speed


if speed>0:
  print "Forward! "
  myMotor.run(Adafruit_MotorHAT.FORWARD)
else:
  print "Backward! "
  myMotor.run(Adafruit_MotorHAT.BACKWARD)


#myMotor.setSpeed(100)
myMotor.setSpeed(abs(speed))
time.sleep(1.0)

#time.sleep(3)




#print "Release"
#myMotor.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(1.0)


print "End program"


#print "arg0="+sys.argv[0]
#print "arg2="+sys.argv[2]
#print "arg3="+sys.argv[3]



