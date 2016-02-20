#!/usr/bin/env python

import os, threading
import sys
import time
import datetime
import random 
import SDL_Pi_INA3221
import DBfunctions
import json
from mysql.connector.errors import InterfaceError
import RTC_DS1307 as RTC

global simINA3221
global lcdType
global lcd
global RTCinstalled
global myrtc
global userMessage
global timercounter

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
    
    try:
        myparamjson = json.loads(myparams)               
        if 'simINA3221' in myparamjson:
            print myparamjson['simINA3221']
            simINA3221 = myparamjson['simINA3221']
        if 'LCD' in myparamjson:
            print myparamjson['LCD']
            lcdType = myparamjson['LCD']
        if 'RTC' in myparamjson:
            print myparamjson['RTC']
            RTCinstalled=myparamjson['RTC']
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print 'Decoding JSON has failed'
else:
    simINA3221 = 1
    lcdType = "none"
    RTCinstalled=0

class PowerMonitor:

    def __init__(self):
        global lcdType
        global lcd
        global myrtc
        global userMessage
        global timercounter

        # global simINA3221  
        # simINA3221 = 1
        userMessage = "hello"
        timercounter = 0
        
        
        print "__init__()"
        # self.runit()
        if lcdType == 'mcp':
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
        
        if lcdType == 'plate':
            # Init LCD
            import Adafruit_CharLCD as LCD
        
            lcd = LCD.Adafruit_CharLCDPlate(cols=20, lines=4)
            #lcd.set_backlight(0)


        if RTCinstalled==1:
            myrtc = RTC.RTC_DS1307()


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
        # sys.exit(1)

        
    def readPipe(self):
        global userMessage
        counter = 0

        pipe_name = "/tmp/testpipe"

        
        while True:
            time.sleep(0.5)

            if not os.path.exists(pipe_name):
                # os.mkfifo( pipe_name, 0644 )
                os.mkfifo(pipe_name, 0777)
            counter += 1
            # print 'waiting for pipe: %d' %counter
            pipe = open(pipe_name, 'rw+')

            # read forever and print anything written to the pipe
            data = pipe.readline()
            if data != '':
                print 'Received from pipe:'
                print data
                pipe.seek(0, 0)
                # pipe.write('')
                pipe.truncate()


                try:
                    decoded = json.loads(data)
                
                    if 'simINA3221' in decoded:
                        if decoded['simINA3221'] == 1:
                            simINA3221 = 1
                        else:
                            simINA3221 = 0
                                            
                    if 'line4' in decoded:
                        userMessage = decoded['line4']
                    if 'exit' in decoded:
                        if decoded['exit'] == 1:
                            print 'Exit'
                            self.stop()
                            break  # exit app

                except ValueError:  # includes simplejson.decoder.JSONDecodeError
                    print 'Decoding JSON has failed'
                
    def readINA3221(self):
        global simINA3221
        global lcdType
        global lcd
        global myrtc
        global userMessage
        global timercounter


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
            
            
            
            if RTCinstalled==1:
                RTCTime=myrtc.read_str()
                nowdatetime='20'+RTCTime
            else:
                nowdatetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            returnval = {
                'date': nowdatetime,
                'bV3': busvoltage3,
                'sV3': shuntvoltage3,
                'lV3': loadvoltage3,
                'cmA3': current_mA3,
                'pw3': power3
            }
            if lcdType == 'none':
                print(json.dumps(returnval))
            
            if lcdType == 'mcp':
                # lcd.clear()
                line1 = "%4.2f V %6.0f mW" % (loadvoltage1, power1)
                line2 = "%4.2f V %6.0f mW" % (loadvoltage2, power2)
                lcd.set_cursor(0, 0);
                lcd.message(line1)
                lcd.set_cursor(0, 1);
                # lcd.message(line2)
                lcd.message(userMessage)
                if RTCinstalled==1:
                    lcd.set_cursor(0, 1);
                    lcd.message(RTCTime)

            
            if lcdType == 'plate':
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
                lcd.message(userMessage)
        
            #
            

            
            
            if timercounter % 10 == 0:
                try:
                    #print 'SQL save'
                    DBfunctions.measureStore(nowdatetime, loadvoltage1, current_mA1, power1, loadvoltage2, current_mA2, power2, loadvoltage3, current_mA3, power3)
                except InterfaceError:  
                    print 'SQL save has failed'

            
            time.sleep(1)
            timercounter += 1




def main():
    powerMonitor = PowerMonitor()
    PowerMonitor.startThreads(powerMonitor)
    PowerMonitor.allThreadsJoin(powerMonitor)


if __name__ == '__main__':
    main()
