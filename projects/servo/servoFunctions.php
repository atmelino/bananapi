<?php



error_reporting(E_ALL);
/*
echo "popen() set servo to 300 <br>\n";
//$cmd = "/usr/bin/python hello.py";
$cmd = "/usr/bin/python ./Servo_pos300.py 2>&1";
$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);
//process = subprocess.Popen(["your_cmd"]...)
//process.wait()
//echo $res;
//echo $res[2];
echo "<br>";
var_dump($res);
//$resbr = str_replace("\n", "<br>",$res);
//$resbr = str_replace("O", "res", "<br>");
//echo $resbr;

*/






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
