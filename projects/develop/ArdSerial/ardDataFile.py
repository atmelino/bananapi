#!/usr/bin/env python

import os
import time
import sys
import termios
import atexit
from select import select
from datetime import datetime
import serial
import traceback


#ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=1)

global termTrueFalse

#background or interactive mode?
if os.isatty(sys.stdin.fileno()):
    # command line mode.
    print "started from command line"
    termTrueFalse=True
    pass
else:
    # Cron mode.
    print "started from cron"
    termTrueFalse=False
    pass

class ArdDataFile:

    def __init__(self):
        # constructor

        if termTrueFalse==True:
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)


    def set_normal_term(self):
        # Resets to normal terminal.  On Windows this is a no-op.
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def getch(self):
        #Returns a keyboard character after kbhit() has been called.
        #Should not be called in the same program as getarrow().
        s = ''
        return sys.stdin.read(1)


    def kbhit(self):
        #Returns True if keyboard character was hit, False otherwise.
        dr,dw,de = select([sys.stdin], [], [], 0)
        return dr != []


    def getArduinoData(self)	:
        try:
	        #response = ser.readline()
	        response = self.readLastLine()
                #for character in response.rstrip():
                   #print character, character.encode('hex')

                #if response != '\x0D' and response != '\x0A':

                #if response[0]=='\x0a':
                    #print "oh-a"

                if response:
                    curdate = datetime.now().strftime("%Y-%m-%d")
                    curdatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    fileName=("ardData%s.txt" %curdate)
                    #fh = open("ardData.txt", "a")
                    fh = open(fileName, "a")
                    output="%s %s \n" %(curdatetime,response.rstrip())
                    fh.write(output)
                    fh.close
                    #print "stored:"
                    print response,   # comma prints without extra newline
        except Exception:
                print(traceback.format_exc())
                print "exception"



    def readLastLine(self):
        last_data=''
        while True:
            data=ser.readline()
            #print "skipped:"
            #print data
            if data!='':
                last_data=data
            else:
                return last_data



# Test    
if __name__ == "__main__":

    kb = ArdDataFile()
    i=1
    print('Hit any key, or ESC to exit')

    while True:
        i=i+1
        #print (i)

        kb.getArduinoData()

        if termTrueFalse==True:
            if kb.kbhit():
                c = kb.getch()
                if ord(c) == 27: # ESC
                    break
                print(c)
        time.sleep(10)

    # after break from while loop
    if termTrueFalse==True:
        kb.set_normal_term()
    
    
    ser.close()

