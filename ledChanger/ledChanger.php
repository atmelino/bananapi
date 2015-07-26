<?php

// print "LED0";
// print "LED1";
// print "LED2";
// print "LED3";



if ( isset($_GET['onOff']))
{
	$onOff = $_GET['onOff'];


	if ( $onOff=='1'){
		print "on";
		shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr0/brightness');
		shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr1/brightness');
		shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr2/brightness');
		shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr3/brightness');
	}
	else {
		print "off";
		shell_exec('echo 0 > /sys/class/leds/beaglebone:green:usr0/brightness');
		shell_exec('echo 0 > /sys/class/leds/beaglebone:green:usr1/brightness');
		shell_exec('echo 0 > /sys/class/leds/beaglebone:green:usr2/brightness');
		shell_exec('echo 0 > /sys/class/leds/beaglebone:green:usr3/brightness');
	}

}


// print "LED0";
// print "LED1";
// print "LED2";
// print "LED3";



// 	print "led and onOff set";

// 	$led = $_GET['led'];

// 	//exec( "/www/cgi-bin/ledctl $led $onOff" );
// 	//shell_exec("echo \"1\" > /sys/class/gpio/gpio30/value");
// 	shell_exec('echo 1 > /sys/class/leds/beaglebone:green:usr3/brightness');

?>
