#!/bin/bash

#sudo python printPowerOnLCD.py {\"simulation\":1}
#python printPowerOnLCD.py {\"simulation\":0}

#sh -c "python printPowerOnLCD.py {'simulation':1}"
sh -c "cd /media/data/public_html/bananapi/projects/powerMonitor; python powerMonitorSocket.py param1"

echo press enter

read

