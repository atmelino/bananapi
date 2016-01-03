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





if ( isset($_GET['angle']))
{
	$angle = $_GET['angle'];


	if ( $angle=='150'){
		print "150";
		
		
		
		
		shell_exec('echo default-on > /sys/class/leds/green\:ph24\:led1/trigger');
	}
	if ( $angle=='none'){
		print "off";
		shell_exec('echo none > /sys/class/leds/green\:ph24\:led1/trigger');
	}

	if ( $angle=='heartbeat'){
		print "heartbeat";
		shell_exec('echo heartbeat > /sys/class/leds/green\:ph24\:led1/trigger');
	}


}




?>
