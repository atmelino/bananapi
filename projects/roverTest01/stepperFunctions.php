<?php

error_reporting(E_ALL);

if ( isset($_GET['speed']))
{
	$speed = $_GET['speed'];
	$wheel = $_GET['wheel'];
	
	//echo "speed: "+$speed;

	//$cmd = "/usr/bin/python ./DCSpeed.py ".$wheel." ".$speed."2>&1";
	$cmd = "/usr/bin/python ./DCSpeed.py ".$wheel." ".$speed;
	$handle = popen($cmd, 'r');
	$res = fread($handle, 8192);
	pclose($handle);

	//var_dump($res);
	echo $res;
	
}


?>
