# bananapi

My Banana Pi Projects. More Information at 
<a href="http://kingofprotons.blogspot.com">Maker Projects</a>


<h3>Installation - Common to all projects</h3>

Download Lubuntu image from <a href="http://www.lemaker.org/product-bananapro-resource.html">LeMaker Resource Downloads</a>

user is bananapi
password is bananapi


install LAMP server:

<code>sudo apt-get install tasksel</code>

<code>sudo tasksel</code>

when asked, select LAMP and continue.

install phpmyadmin:

<code>sudo apt-get install phpmyadmin</code>

This will make it easier to create a database when needed.

<h3>Installation - power monitor</h3>

create user and database named solarPanel

point web browser to the Banana Pi

open phpmyadmin
<a href="http://localhost/phpmyadmin">phpmyadmin</a>

user is root
password is what you entered in tasksel

create new user and new database at the same time

<img src="phpmyadmin_solarPanel.png" alt="phpmyadmin" style="width:600px;">


install mySQL library for Python:

<code>sudo apt-get install mysql.connector</code>



<h3>Power Monitor</h3>

We want the python script to start automatically when the Pi is booted, so that the power values are displayed without user intervention.

For a new system install, in order to make the python script run automatically when the computer is started,

open a terminal and run

<code>crontab -e</code>

Depending on the configuration, add one of the lines:

- For a Banana Pro with the INA3221 hat and the Adafruit LCD hat:

<code>@reboot /media/data/public_html/bananapi/projects/powerMonitorSocket/autoStartPM_INA_LCDplate.sh  >> $HOME/testpylog.txt 2>&1</code>

- For a Banana Pro without the INA3221 hat and a MCP23017 based LCD hat:

<code>@reboot /media/data/public_html/bananapi/projects/powerMonitorSocket/autoStartPM_noINA_LCDmcp.sh  >> $HOME/testpylog.txt 2>&1</code>

- For any computer:

<code>@reboot /media/data/public_html/bananapi/projects/powerMonitorSocket/autoStartPM_noINA_noLCD.sh  >> $HOME/testpylog.txt 2>&1</code>



the script is then automatically started when the system boots. 

Now run as superuser

<code>sudo crontab -e</code>

add the line

<code>@reboot /media/data/public_html/bananapi/projects/powerMonitorSocket/pipe_web.sh  >> $HOME/testpylog.txt 2>&1</code>





To disable the autostart, run

<code>crontab -e</code>

and convert the line to a comment.

To run it at at startup again, uncomment the line.







