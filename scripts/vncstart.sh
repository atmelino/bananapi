#!/bin/bash


sudo service lightdm restart


#x11vnc -bg -o %HOME/.x11vnc.log.%VNCDISPLAY -auth /var/run/lightdm/root/:0 -forever

x11vnc -bg -geometry 1024x768 -o %HOME/.x11vnc.log.%VNCDISPLAY -auth /var/run/lightdm/root/:0 -forever



#sudo service lightdm restart

echo press enter

read


