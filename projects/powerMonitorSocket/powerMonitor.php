<?php

error_reporting(E_ALL);


main();

function main()
{

	//print "function main() start\n";
	$json=$_GET['json'];
	echo "PHP: ".$json."\n";
	$decoded = json_decode($_GET['json']);
	$functionString=$decoded->fs;
	//print "functionString=".$functionString."\n";

	if(strcmp($functionString,'sendMessage')==0)
	{
		print "calling sendMessage\n";
		sendtoPipe($var);
	}

}



function sendtoPipe($String)
{
	print ("sending string to pipe".$cString."\n");
	$pipe = fopen('/dev/shm/powerMonitorpipe','r+');
	fwrite($pipe,$String);
	fclose($pipe);
}

//echo 'end PHP program';

?>
