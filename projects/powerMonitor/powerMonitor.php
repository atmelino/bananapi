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
		$json=$_GET['json'];
		print $json."\n";
		sendtoPipe($json);
	}

}



// note: the folder /run/shm/web must be owned by www-data:www-data
function sendtoPipe($String)
{
	print ("sending string to pipe: ".$String."\n");
	//print ($_SERVER['DOCUMENT_ROOT']."\n");
	//$filename=$_SERVER['DOCUMENT_ROOT'].'/test.txt';
	//$filename='/run/shm/web/powerMonitorpipe';
	$filename='/tmp/testpipe';
	
	//print ($filename."\n");
	$pipe =fopen($filename,'w+');
	print ("fopen success: ".$pipe."\n");
	var_dump($pipe);
	fwrite($pipe,$String);
	//fwrite($pipe,'hello');
	fclose($pipe);
	print ("sendtoPipe() done\n");
}

//echo 'end PHP program';

?>
