#!/usr/bin/python

import time
import atexit
import sys
import json


myparams=sys.argv[1]
print "python: "+myparams

print(json.dumps(myparams))
					
parsed_json = json.loads(myparams)					
#decoded = json.loads(myparams)

if 'speedfl' in parsed_json:
  speedfl=int(parsed_json['speedfl'])	
  speedfr=int(parsed_json['speedfr'])	
  speedrl=int(parsed_json['speedrl'])	
  speedrr=int(parsed_json['speedrr'])	
	
  print "speed: %d %d %d %d" % (speedfl,speedfr,speedrl,speedrr)


later=0
if later>0:
  from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

  # create a default object, no changes to I2C address or frequency
  mh = Adafruit_MotorHAT(addr=0x60)


  ################################# DC motor test!
  myMotor1 = mh.getMotor(1)
  myMotor2 = mh.getMotor(2)
  myMotor3 = mh.getMotor(3)
  myMotor4 = mh.getMotor(4)

  myparams=sys.argv[1]
  arg2=int(sys.argv[2])

  #print "myparams="+sys.argv[1]

  wheel=myparams
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

print "End python program"

