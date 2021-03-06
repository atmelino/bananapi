#!/usr/bin/env python

import sys
import datetime
import random 
import SDL_Pi_INA3221
import json

# the three channels of the INA3221 named for SunAirPlus Solar Power Controller channels (www.switchdoc.com)
LIPO_BATTERY_CHANNEL = 1
SOLAR_CELL_CHANNEL   = 2
OUTPUT_CHANNEL       = 3


myparams=sys.argv[1]
#print "python: "+myparams

parsed_json = json.loads(myparams)                         
if 'simulation' in parsed_json:
  simulation=parsed_json['simulation']     

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

if simulation==1:
     busvoltage3 = 1
     shuntvoltage3 = 2
     current_mA3 = 8
     loadvoltage3 = 6
     power3=loadvoltage3*current_mA3          
     
     #now=time.strftime("%Y-%m-%d %H:%M:%S")     
     #print "%12s %3.2f V  %3.2f mV  %3.2f V  %3.2f mA" % (now, busvoltage3, shuntvoltage3, loadvoltage3 ,current_mA3)
     #sys.stdout.write("%12s %3.2f V  %3.2f mV  %3.2f V  %3.2f mA" % (now, busvoltage3, shuntvoltage3, loadvoltage3 ,current_mA3))


else:
     ina3221 = SDL_Pi_INA3221.SDL_Pi_INA3221(twi=2,addr=0x40)
     
     later =0
     if later>0:
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
          
          
          busvoltage2 = ina3221.getBusVoltage_V(SOLAR_CELL_CHANNEL)
          shuntvoltage2 = ina3221.getShuntVoltage_mV(SOLAR_CELL_CHANNEL)
          current_mA2 = -ina3221.getCurrent_mA(SOLAR_CELL_CHANNEL)
          loadvoltage2 = busvoltage2 + (shuntvoltage2 / 1000)
          
          print "Solar Cell Bus Voltage 2:  %3.2f V " % busvoltage2
          print "Solar Cell Shunt Voltage 2: %3.2f mV " % shuntvoltage2
          print "Solar Cell Load Voltage 2:  %3.2f V" % loadvoltage2
          print "Solar Cell Current 2:  %3.2f mA" % current_mA2
          print 
     
     
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
print(json.dumps(returnval))


#print "%12s %3.2f V  %3.2f mV  %3.2f V  %3.2f mA " % (now, busvoltage3, shuntvoltage3, loadvoltage3 ,current_mA3)
#sys.stdout.write("%12s %3.2f V  %3.2f mV  %3.2f V  %3.2f mA" % (now, busvoltage3, shuntvoltage3, loadvoltage3 ,current_mA3))
#print "%12s %3.2f V  %3.2f mV  %3.2f V  %3.2f mA %5.3f mW" % (now, busvoltage3, shuntvoltage3, loadvoltage3 ,current_mA3,power3)

