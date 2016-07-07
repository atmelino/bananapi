import RPi.GPIO as GPIO
import time

 
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)
 
# Set up the GPIO channel
#GPIO.setup(11, GPIO.IN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

 
print "pin 11 = GPIO 0"

#while True:
for i in range(1,30):

    #input_value = GPIO.input(11)
    #print "on"
    print GPIO.input(11)
    time.sleep(0.1)



