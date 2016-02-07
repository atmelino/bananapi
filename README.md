# bananapi

My Banana Pi Projects. More Information at 
<a href="http://kingofprotons.blogspot.com">Maker Projects</a>


<h3>Installation - Common to all projects</h3>

Download Lubuntu image from <a href="http://www.lemaker.org/product-bananapro-resource.html">LeMaker Resource Downloads</a>

user is bananapi
password is bananapi


install LAMP server:

sudo apt-get install tasksel

sudo tasksel




sudo apt-get install phpmyadmin

<h3>Installation - power monitor</h3>

create user and database named solarPanel

point web browser to the Banana Pi

open phpmyadmin
<a href="http://localhost/phpmyadmin">phpmyadmin</a>

create new user and new database at the same time

<img src="phpmyadmin_solarPanel.png" alt="phpmyadmin" style="width:600px;">



<h3>Power Monitor</h3>


For a new system install, in order to make the python script run automatically when the computer is started,

open a terminal and run

crontab -e

add the line

@reboot /media/data/public_html/bananapi/projects/powerMonitor/autoStartPM.sh  >> $HOME/testpylog.txt 2>&1

the script autoStartPM.sh is then automatically started when the system boots. 



To disable the autostart, run

crontab -e

and convert the line to a comment.

To run it at at startup again, uncomment the line.


Now run as superuser

sudo crontab -e

add the line

@reboot /media/data/public_html/bananapi/projects/powerMonitor/pipe_web.sh  >> $HOME/testpylog.txt 2>&1





