<?php


$descriptorspec = array(
		0 => array("pipe","r"),
		1 => array("pipe","w"),
		2 => array("file","./error.log","a")
) ;

echo "proc_open() test <br>";

// define current working directory where files would be stored
$cwd = './' ;

// open process reprint.pl and pass it an argument
$process = proc_open('python ./hello.py ' . $argv1, $descriptorspec, $pipes, $cwd) ;
echo "variable process ";
echo $process;

echo "<br>";

//$argv1 doing nothing here its just for the example
if (is_resource($process)) {// print pipe output
	echo stream_get_contents($pipes1) ;// close pipe
	fclose($pipes1) ;

	// close process
	proc_close($process) ;

}

echo "proc_open() end";





if ( isset($_GET['speed']))
{
	$speed = $_GET['speed'];


	if ( $speed=='150'){
		//print "150";				
		$cmd = "/usr/bin/python ./Servo_pos150.py 2>&1";
		$handle = popen($cmd, 'r');
		$res = fread($handle, 8192);
		pclose($handle);
	}
	if ( $speed=='300'){
		$cmd = "/usr/bin/python ./Servo_pos300.py 2>&1";
		$handle = popen($cmd, 'r');
		$res = fread($handle, 8192);
		pclose($handle);
	}
	if ( $speed=='600'){
		$cmd = "/usr/bin/python ./Servo_pos600.py 2>&1";
		$handle = popen($cmd, 'r');
		$res = fread($handle, 8192);
		pclose($handle);
	}


}




?>
