  #myparams=sys.argv[1]
  #arg2=int(sys.argv[2])

  #print "myparams="+sys.argv[1]

  #wheel=myparams
  #speed=20*arg2
  #print "wheel=%s speed=%d" % (wheel, speed)
later=0
if later>0:
  print "python run motors"

  # create a default object, no changes to I2C address or frequency
  mh = Adafruit_MotorHAT(addr=0x60)


  ################################# DC motor test!
  myMotor1 = mh.getMotor(1)
  myMotor2 = mh.getMotor(2)
  myMotor3 = mh.getMotor(3)
  myMotor4 = mh.getMotor(4)



  if speed>0:
    print "Forward! "
    myMotor1.run(Adafruit_MotorHAT.FORWARD)
    myMotor1.setSpeed(abs(speedfl))
   	time.sleep(0.01)

    myMotor2.run(Adafruit_MotorHAT.FORWARD)
    myMotor2.setSpeed(abs(speedfr))
  else:
    print "Backward! "
    myMotor1.run(Adafruit_MotorHAT.BACKWARD)


