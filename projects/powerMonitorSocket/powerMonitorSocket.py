#!/usr/b1in/env python

import os, threading
import sys
import time
import datetime
import random 
import SDL_Pi_INA3221
import json


global simINA3221
global lcd
        # LCD Type
        # lcd = 'mcp'
        # lcd = 'none'
        # lcd = 'plate'

# the three channels of the INA3221 named for SunAirPlus Solar Power Controller channels (www.switchdoc.com)
LIPO_BATTERY_CHANNEL = 1
SOLAR_CELL_CHANNEL = 2
OUTPUT_CHANNEL = 3

# print len(sys.argv)
if len(sys.argv) > 1:
    myparams = sys.argv[1]
    print "python: " + myparams
    myparamjson = json.loads(myparams)
    print myparamjson['simINA3221']
    print myparamjson['LCD']

    simINA3221 = myparamjson['simINA3221']
    lcd = myparamjson['LCD']
else:
    simINA3221 = 1
    lcd = "none"


class PowerMonitor:

    def __init__(self):
        global lcd
        # global simINA3221  
        # simINA3221 = 1
        print "__init__()"
        # self.runit()
        if lcd == 'mcp':
            # Init LCD
            import Adafruit_CharLCD as LCD
            import Adafruit_GPIO.MCP230xx as MCP
            
            # Define MCP pins connected to the LCD.
            lcd_rs = 0
            lcd_en = 1
            lcd_d4 = 2
            lcd_d5 = 3
            lcd_d6 = 4
            lcd_d7 = 5
            lcd_red = 6
            lcd_green = 7
            lcd_blue = 8
            
            # Define LCD column and row size for 16x2 LCD.
            lcd_columns = 16
            lcd_rows = 2
        
            print "char_lcd_mcp.py init gpio"
            gpio = MCP.MCP23017()
            lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                        lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue, gpio=gpio)
        
        if lcd == 'plate':
            # Init LCD
            import Adafruit_CharLCD as LCD
        
            lcd = LCD.Adafruit_CharLCDPlate(cols=20, lines=4)
        
        
        # print 'sending start messsage to LCD'
        # lcd.message('Power Monitor .2')
        


    def startThreads(self):
        print "startThreads()"
        # start read pipe thread
        self.readPipe_thread = threading.Thread(target=self.readPipe)
        self.readPipe_thread.setDaemon(1)
        self.readPipe_thread.start()
        # start read INA3221 thread
        self.readINA3221_thread = threading.Thread(target=self.readINA3221)
        self.readINA3221_thread.setDaemon(1)
        self.readINA3221_thread.start()
        
        
    def allThreadsJoin(self):
        self.readPipe_thread.join()
        self.readINA3221_thread.join()
        
    def stop(self):           
        self.alive = False
        os._exit(1)
        #sys.exit(1)

        
    def readPipe(self):

        pipe_name = "/tmp/testpipe"

        
        while True:

            if not os.path.exists(pipe_name):
                # os.mkfifo( pipe_name, 0644 )
                os.mkfifo(pipe_name, 0777)

            print 'waiting for pipe:'
            pipe = open(pipe_name, 'r')

            # read forever and print anything written to the pipe
            data = pipe.readline()
            if data != '':
                print 'Received from pipe:'
                print data
                
                decoded = json.loads(data)
                
                if 'simINA3221' in decoded:
                    if decoded['simINA3221'] == 1:
                        simINA3221 = 1
                    else:
                        simINA3221 = 0
                # print 'simulation=%d' % simulation                        
                if 'line4' in decoded:
                    line4 = decoded['line4']
                if 'exit' in decoded:
                    if decoded['exit'] == 1:
                        #sys.exit(1)
                        print 'Exit'
                        self.stop()
                        break  # exit app

        

    def readINA3221(self):
        global simINA3221
        global lcd

        # print "readINA()"
        while True:
        
            if simINA3221 == 1:
                 busvoltage1 = 1
                 shuntvoltage1 = 2
                 current_mA1 = 8
                 loadvoltage1 = random.randint(0, 9)
                 power1 = loadvoltage1 * current_mA1          
                 busvoltage2 = 1
                 shuntvoltage2 = 2
                 current_mA2 = 8
                 loadvoltage2 = random.randint(0, 9)
                 power2 = loadvoltage2 * current_mA2          
                 busvoltage3 = 1
                 shuntvoltage3 = 2
                 current_mA3 = 8
                 loadvoltage3 = random.randint(0, 9)
                 power3 = loadvoltage3 * current_mA3          
                  
            
            else:
                 ina3221 = SDL_Pi_INA3221.SDL_Pi_INA3221(twi=2, addr=0x40)
                 
                 busvoltage1 = ina3221.getBusVoltage_V(LIPO_BATTERY_CHANNEL)
                 shuntvoltage1 = ina3221.getShuntVoltage_mV(LIPO_BATTERY_CHANNEL)
                 current_mA1 = ina3221.getCurrent_mA(LIPO_BATTERY_CHANNEL)                
                 loadvoltage1 = busvoltage1 + (shuntvoltage1 / 1000)              
                 power1 = loadvoltage1 * current_mA1          
        
                 busvoltage2 = ina3221.getBusVoltage_V(SOLAR_CELL_CHANNEL)
                 shuntvoltage2 = ina3221.getShuntVoltage_mV(SOLAR_CELL_CHANNEL)
                 current_mA2 = -ina3221.getCurrent_mA(SOLAR_CELL_CHANNEL)
                 loadvoltage2 = busvoltage2 + (shuntvoltage2 / 1000)
                 power2 = loadvoltage2 * current_mA2          
                 
                 busvoltage3 = ina3221.getBusVoltage_V(OUTPUT_CHANNEL)
                 shuntvoltage3 = ina3221.getShuntVoltage_mV(OUTPUT_CHANNEL)
                 current_mA3 = ina3221.getCurrent_mA(OUTPUT_CHANNEL)
                 loadvoltage3 = busvoltage3 + (shuntvoltage3 / 1000)
                 power3 = loadvoltage3 * current_mA3          
            
            
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(now)
            
            returnval = {
                'date': now,
                'bV3': busvoltage3,
                'sV3': shuntvoltage3,
                'lV3': loadvoltage3,
                'cmA3': current_mA3,
                'pw3': power3
            }
            if lcd == 'none':
                print(json.dumps(returnval))
            
            if lcd != 'none':
                # lcd.clear()
                line1 = "%4.2f V %6.0f mW" % (loadvoltage1, power1)
                line2 = "%4.2f V %6.0f mW" % (loadvoltage2, power2)
                line3 = "%4.2f V %6.0f mW" % (loadvoltage3, power3)
                lcd.set_cursor(0, 0);
                lcd.message(line1)
                lcd.set_cursor(0, 1);
                lcd.message(line2)
                lcd.set_cursor(0, 2);
                lcd.message(line3)
                lcd.set_cursor(0, 3);
                lcd.message(line4)
        
            #
            time.sleep(1)
        



def main():
    powerMonitor = PowerMonitor()
    PowerMonitor.startThreads(powerMonitor)
    PowerMonitor.allThreadsJoin(powerMonitor)


if __name__ == '__main__':
    main()
