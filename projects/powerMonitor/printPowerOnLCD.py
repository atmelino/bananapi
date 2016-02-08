#!/usr/bin/env python

import sys
import time
import datetime
import random 
import SDL_Pi_INA3221
import json


# the three channels of the INA3221 named for SunAirPlus Solar Power Controller channels (www.switchdoc.com)
LIPO_BATTERY_CHANNEL = 1
SOLAR_CELL_CHANNEL   = 2
OUTPUT_CHANNEL       = 3


#myparams=sys.argv[1]
#print "python: "+myparams

#parsed_json = json.loads(myparams)                         
#if 'simulation' in parsed_json:
#  simulation=parsed_json['simulation']     

simulation=1     

busvoltage1   = 0
shuntvoltage1 = 0
current_mA1   = 0
loadvoltage1  = 0
power1=0
busvoltage2 = 0
shuntvoltage2 = 0
current_mA2 = 0
loadvoltage2 = 0
power2=0
busvoltage3 = 0
shuntvoltage3 = 0
current_mA3 = 0
loadvoltage3 = 0
power3=0



# LCD Type
lcd='plate'
lcd='none'
lcd='mcp'

if lcd=='mcp':
    # Init LCD
    import Adafruit_CharLCD as LCD
    import Adafruit_GPIO.MCP230xx as MCP
    
    # Define MCP pins connected to the LCD.
    lcd_rs        = 0
    lcd_en        = 1
    lcd_d4        = 2
    lcd_d5        = 3
    lcd_d6        = 4
    lcd_d7        = 5
    lcd_red       = 6
    lcd_green     = 7
    lcd_blue      = 8
    
    # Define LCD column and row size for 16x2 LCD.
    lcd_columns = 16
    lcd_rows    = 2

    print "char_lcd_mcp.py init gpio"
    gpio = MCP.MCP23017()
    lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                                lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue, gpio=gpio)
    




if lcd=='plate':
    # Init LCD
    import Adafruit_CharLCD as LCD

    lcd = LCD.Adafruit_CharLCDPlate(cols=20,lines=4)


#print 'sending start messsage to LCD'
#lcd.message('Power Monitor .2')



while True:

    if simulation==1:
         busvoltage3 = 1
         shuntvoltage3 = 2
         current_mA3 = 8
         loadvoltage3 = 6
         power3=loadvoltage3*current_mA3          
          
    
    else:
         ina3221 = SDL_Pi_INA3221.SDL_Pi_INA3221(twi=2,addr=0x40)
         
         #later =0
         #if later>0:
         busvoltage1 = ina3221.getBusVoltage_V(LIPO_BATTERY_CHANNEL)
         shuntvoltage1 = ina3221.getShuntVoltage_mV(LIPO_BATTERY_CHANNEL)
         current_mA1 = ina3221.getCurrent_mA(LIPO_BATTERY_CHANNEL)                
         loadvoltage1 = busvoltage1 + (shuntvoltage1 / 1000)              
         power1=loadvoltage1*current_mA1          

         busvoltage2 = ina3221.getBusVoltage_V(SOLAR_CELL_CHANNEL)
         shuntvoltage2 = ina3221.getShuntVoltage_mV(SOLAR_CELL_CHANNEL)
         current_mA2 = -ina3221.getCurrent_mA(SOLAR_CELL_CHANNEL)
         loadvoltage2 = busvoltage2 + (shuntvoltage2 / 1000)
         power2=loadvoltage2*current_mA2          
         
         busvoltage3 = ina3221.getBusVoltage_V(OUTPUT_CHANNEL)
         shuntvoltage3 = ina3221.getShuntVoltage_mV(OUTPUT_CHANNEL)
         current_mA3 = ina3221.getCurrent_mA(OUTPUT_CHANNEL)
         loadvoltage3 = busvoltage3 + (shuntvoltage3 / 1000)
         power3=loadvoltage3*current_mA3          
    
    
    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #print(now)
    
    returnval = {
        'date': now,
        'bV3': busvoltage3,
        'sV3': shuntvoltage3,
        'lV3': loadvoltage3,
        'cmA3': current_mA3,
        'pw3': power3
    }
    if lcd=='none':
        print(json.dumps(returnval))
    
    if lcd!='none':
        #lcd.clear()
        line1= "%4.2f V %6.0f mW" % (loadvoltage1,power1)
        line2= "%4.2f V %6.0f mW" % (loadvoltage2,power2)
        line3= "%4.2f V %6.0f mW" % (loadvoltage3,power3)
        lcd.set_cursor( 0, 0);
        lcd.message(line1)
        lcd.set_cursor( 0, 1);
        lcd.message(line2)
        lcd.set_cursor( 0, 2);
        lcd.message(line3)

    #
    time.sleep(0.5)

