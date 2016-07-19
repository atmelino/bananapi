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


ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)



class KBHit:

    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''


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
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''
        s = ''
        return sys.stdin.read(1)


    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []


    def getArduinoData(self)	:
        try:
	        response = ser.readline()
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
                    fh = open(filename, "a")
                    output="%s %s \n" %(curdatetime,response.rstrip())
                    fh.write(output)
                    fh.close
                    print response
        except Exception:
                print(traceback.format_exc())
                print "exception"


# Test    
if __name__ == "__main__":

    kb = KBHit()
    i=1
    print('Hit any key, or ESC to exit')

    while True:
        i=i+1
        print (i)

        kb.getArduinoData()

        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break
            print(c)
        time.sleep(1.5)

    # after break from while loop
    kb.set_normal_term()
    ser.close()



