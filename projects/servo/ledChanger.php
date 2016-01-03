<?php


if ( isset($_GET['onOff']))
{
	$onOff = $_GET['onOff'];


	if ( $onOff=='default-on'){
		print "on";
		shell_exec('echo default-on > /sys/class/leds/green\:ph24\:led1/trigger');
	}
	if ( $onOff=='none'){
		print "off";
		shell_exec('echo none > /sys/class/leds/green\:ph24\:led1/trigger');
	}

	if ( $onOff=='heartbeat'){
		print "heartbeat";
		shell_exec('echo heartbeat > /sys/class/leds/green\:ph24\:led1/trigger');
	}



//	else {
	//	print "off";
		//shell_exec('echo none > /sys/class/leds/green\:ph24\:led1/trigger');
	//}

}


// 	print "led and onOff set";

// 	$led = $_GET['led'];


?>
