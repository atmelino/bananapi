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
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

arg1=sys.argv[1]
arg2=int(sys.argv[2])

#print "arg1="+sys.argv[1]

wheel=arg1
speed=20*arg2
print "wheel=%s speed=%d" % (wheel, speed)


if speed>0:
  print "Forward! "
  if wheel=='fl':
    myMotor1.run(Adafruit_MotorHAT.FORWARD)
    myMotor1.setSpeed(abs(speed))
#  if wheel=='fr':
    myMotor2.run(Adafruit_MotorHAT.FORWARD)
    myMotor2.setSpeed(abs(speed))
else:
  print "Backward! "
  myMotor1.run(Adafruit_MotorHAT.BACKWARD)

#time.sleep(1.0)

#myMotor1.setSpeed(100)

#time.sleep(3)




#print "Release"
#myMotor1.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(1.0)


print "End program"


#print "arg0="+sys.argv[0]
#print "arg2="+sys.argv[2]
#print "arg3="+sys.argv[3]



