#!/usr/bin/env python


import os
import time
import sys
import termios
import atexit
from select import select
import datetime
import random 
import SDL_Pi_INA3221
import RPi.GPIO as GPIO


class KBHit:

    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''
            # use P1 header pin numbering convention
            GPIO.setmode(GPIO.BOARD)
 
            # Set up the GPIO channel
            #GPIO.setup(11, GPIO.IN)
            GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


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

        if os.name == 'nt':
            pass

        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''

        s = ''

        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')

        else:
            return sys.stdin.read(1)


    def getarrow(self):
        ''' Returns an arrow-key code after kbhit() has been called. Codes are
        0 : up
        1 : right
        2 : down
        3 : left
        Should not be called in the same program as getch().
        '''

        if os.name == 'nt':
            msvcrt.getch() # skip 0xE0
            c = msvcrt.getch()
            vals = [72, 77, 80, 75]

        else:
            c = sys.stdin.read(3)[2]
            vals = [65, 67, 66, 68]

        return vals.index(ord(c.decode('utf-8')))


    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []


    def getINAValues()	:
        # the three channels of the INA3221 named for SunAirPlus Solar Power Controller channels (www.switchdoc.com)
        LIPO_BATTERY_CHANNEL = 1
        SOLAR_CELL_CHANNEL   = 2
        OUTPUT_CHANNEL       = 3

        ina3221 = SDL_Pi_INA3221.SDL_Pi_INA3221(twi=2,addr=0x40)

        print "------------------------------"
        shuntvoltage1 = 0
        busvoltage1   = 0
        current_mA1   = 0
        loadvoltage1  = 0


        busvoltage1 = ina3221.getBusVoltage_V(LIPO_BATTERY_CHANNEL)
        shuntvoltage1 = ina3221.getShuntVoltage_mV(LIPO_BATTERY_CHANNEL)
        # minus is to get the "sense" right.   - means the battery is charging, + that it is discharging
        current_mA1 = ina3221.getCurrent_mA(LIPO_BATTERY_CHANNEL)  

        loadvoltage1 = busvoltage1 + (shuntvoltage1 / 1000)

        print "LIPO_Battery Bus Voltage: %3.2f V " % busvoltage1
        print "LIPO_Battery Shunt Voltage: %3.2f mV " % shuntvoltage1
        print "LIPO_Battery Load Voltage:  %3.2f V" % loadvoltage1
        print "LIPO_Battery Current 1:  %3.2f mA" % current_mA1
        print

        shuntvoltage2 = 0
        busvoltage2 = 0
        current_mA2 = 0
        loadvoltage2 = 0

        busvoltage2 = ina3221.getBusVoltage_V(SOLAR_CELL_CHANNEL)
        shuntvoltage2 = ina3221.getShuntVoltage_mV(SOLAR_CELL_CHANNEL)
        current_mA2 = -ina3221.getCurrent_mA(SOLAR_CELL_CHANNEL)
        loadvoltage2 = busvoltage2 + (shuntvoltage2 / 1000)

        print "Solar Cell Bus Voltage 2:  %3.2f V " % busvoltage2
        print "Solar Cell Shunt Voltage 2: %3.2f mV " % shuntvoltage2
        print "Solar Cell Load Voltage 2:  %3.2f V" % loadvoltage2
        print "Solar Cell Current 2:  %3.2f mA" % current_mA2
        print 

        shuntvoltage3 = 0
        busvoltage3 = 0
        current_mA3 = 0
        loadvoltage3 = 0

        busvoltage3 = ina3221.getBusVoltage_V(OUTPUT_CHANNEL)
        shuntvoltage3 = ina3221.getShuntVoltage_mV(OUTPUT_CHANNEL)
        current_mA3 = ina3221.getCurrent_mA(OUTPUT_CHANNEL)
        loadvoltage3 = busvoltage3 + (shuntvoltage3 / 1000)

        print "Output Bus Voltage 3:  %3.2f V " % busvoltage3
        print "Output Shunt Voltage 3: %3.2f mV " % shuntvoltage3
        print "Output Load Voltage 3:  %3.2f V" % loadvoltage3
        print "Output Current 3:  %3.2f mA" % current_mA3
        print




# Test    
if __name__ == "__main__":

    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        print (i)
        input_value = GPIO.input(11)

        if input_value:
            print "LED on"
        else:
            print "LED off"
            getINAValues()

        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break
            print(c)
        time.sleep(1.5)

    kb.set_normal_term()


