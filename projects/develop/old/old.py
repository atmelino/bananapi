
  
  
  

            # create the pipe and open it for reading
            #os.mkfifo(pipeNameIn)
            #os.chmod(pipeNameIn, 0777)
            #pipe = open(pipeNameIn, 'r')
  
              #pipe_name = "/tmp/hourly"
  #print 'read from pipe'
  
  
              #print 'while true loop'

            # the name of the pipe
            #pipeNameIn = '/run/shm/web/powerMonitorPipe'

            # we will get an error if the pipe exists
            # when creating a new one, so try removing it first
            #try:
                #os.unlink(pipeNameIn)
            #except:
                #pass

  
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


#myMotor1.setSpeed(0)
#time.sleep(0.01)
#myMotor2.setSpeed(0)
#time.sleep(0.01)
#myMotor3.setSpeed(0)
#time.sleep(0.01)







#print "Release"
#myMotor3.run(Adafruit_MotorHAT.RELEASE)
#time.sleep(1.0)

