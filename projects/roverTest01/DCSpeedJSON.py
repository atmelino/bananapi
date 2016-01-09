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
myMotor_rr = mh.getMotor(4)
myMotor_lr = mh.getMotor(3)
myMotor_fr = mh.getMotor(2)
myMotor_fl = mh.getMotor(1)

print "run motors"

if speedfl>0:
  myMotor_rr.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor_rr.run(Adafruit_MotorHAT.BACKWARD)
if speedfr>0:
  myMotor_lr.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor_lr.run(Adafruit_MotorHAT.BACKWARD)
if speedrl>0:
  myMotor_fr.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor_fr.run(Adafruit_MotorHAT.BACKWARD)
if speedrr>0:
  myMotor_fl.run(Adafruit_MotorHAT.FORWARD)
else:
  myMotor_fl.run(Adafruit_MotorHAT.BACKWARD)

myMotor_rr.setSpeed(abs(speedfl))
myMotor_lr.setSpeed(abs(speedfr))
myMotor_fr.setSpeed(abs(speedrl))
myMotor_fl.setSpeed(abs(speedrr))
time.sleep(0.01)

if speedfl==0 and speedfr==0 and speedrl==0 and speedrr==0:
  print "motors off"
  turnOffMotors()



print "End python program"

