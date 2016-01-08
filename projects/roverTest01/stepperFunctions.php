<?php



error_reporting(E_ALL);




if ( isset($_GET['angle']))
{
	$angle = $_GET['angle'];

	echo "angle: "+$angle;
	
	if ( $angle=='150'){
		//print "150";				
		$cmd = "/usr/bin/python ./Servo_pos150.py 2>&1";
		$handle = popen($cmd, 'r');
		$res = fread($handle, 8192);
		pclose($handle);
	}
	if ( $angle=='300'){
		//$cmd = "/usr/bin/python ./Servo_pos300.py 2>&1";
		$cmd = "/usr/bin/python ./Servo_pos300.py";
		$handle = popen($cmd, 'r');
		$res = fread($handle, 8192);
		pclose($handle);
	}
	if ( $angle=='600'){
		$cmd = "/usr/bin/python ./Servo_pos600.py 2>&1";
		$handle = popen($cmd, 'r');
		$res = fread($handle, 8192);
		pclose($handle);
	}

var_dump($res);

}




?>
