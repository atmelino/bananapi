import RPi.GPIO as GPIO
import time

 
# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)
 
# Set up the GPIO channels - one input and one output
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
 
 
# Output to pin 11
print "pin 11 = GPIO 0"

#while True:
for i in range(1,3):

    GPIO.output(11, GPIO.HIGH)
    print "on"
    time.sleep(4)
    GPIO.output(11, GPIO.LOW)
    print "off"
    time.sleep(4)

# Input from pin 12
#input_value = GPIO.input(12)

 
# The same script as above but using BCM GPIO 00..nn numbers
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)
#GPIO.setup(18, GPIO.OUT)
#input_value = GPIO.input(17)
#GPIO.output(18, GPIO.HIGH)

