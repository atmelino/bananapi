#!/bin/bash

# make folder in ramdisk for pipe
#mkdir /run/shm/web
#chown www-data:www-data /run/shm/web



#sudo python printPowerOnLCD.py {\"simulation\":1}
#python printPowerOnLCD.py {\"simulation\":0}

#sh -c "python printPowerOnLCD.py {'simulation':0}"
sh -c "cd /media/data/public_html/bananapi/projects/powerMonitor; python printPowerOnLCD.py"

echo press enter

read

