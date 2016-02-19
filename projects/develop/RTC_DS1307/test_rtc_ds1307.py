#!/usr/bin/python

import RTC_DS1307 as RTC


print "myrtc"
myrtc = RTC.RTC_DS1307()



a=myrtc.read_all()

print a

