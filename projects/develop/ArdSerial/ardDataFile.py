import serial
from datetime import datetime
import time

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)



try:
    while 1:
        response = ser.readline()
        curdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fh = open("ardData.txt", "a")
        output="%s %s " %(curdate,response)
        fh.write(output)
        fh.close
        print response
except KeyboardInterrupt:
    ser.close()

