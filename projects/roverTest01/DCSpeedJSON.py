#!/usr/bin/python

import time
import atexit
import sys
import json
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor


myparams=sys.argv[1]
print "python: "+myparams

print(json.dumps(myparams))
					
parsed_json = json.loads(myparams)					
#decoded = json.loads(myparams)

if 'speedfl' in parsed_json:
  speedfl=20*int(parsed_json['speedfl'])	
  speedfr=20*int(parsed_json['speedfr'])	
  speedrl=20*int(parsed_json['speedrl'])	
  speedrr=20*int(parsed_json['speedrr'])
  print "python speed: %d %d %d %d" % (speedfl,speedfr,speedrl,speedrr)


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

print "run motors"

if speedfl>0:
  myMotor1.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor1.run(Adafruit_MotorHAT.BACKWARD)
if speedfr>0:
  myMotor2.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor2.run(Adafruit_MotorHAT.BACKWARD)
if speedrl>0:
  myMotor3.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor3.run(Adafruit_MotorHAT.BACKWARD)
if speedrr>0:
  myMotor4.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor4.run(Adafruit_MotorHAT.BACKWARD)

myMotor1.setSpeed(abs(speedfl))
#time.sleep(0.01)
myMotor2.setSpeed(abs(speedfr))
#time.sleep(0.01)
myMotor3.setSpeed(abs(speedrl))
#time.sleep(0.01)
myMotor4.setSpeed(abs(speedrr))
time.sleep(0.01)


#myMotor1.setSpeed(0)
#time.sleep(0.01)
#myMotor2.setSpeed(0)
#time.sleep(0.01)
#myMotor3.setSpeed(0)
#time.sleep(0.01)



#print "Release"
#myMotor3.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(1.0)



print "End python program"

