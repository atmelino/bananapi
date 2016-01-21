<?php

error_reporting(E_ALL);


$json=$_GET['json'];
echo "PHP: ".$json."\n";


//$decoded = json_decode($_GET['json']);
//echo $decoded;

//$speedfl=$decoded->speedfl;
//echo $speedfl;



// $speed = $_GET['speed'];
// $wheel = $_GET['wheel'];

$cmd = "/usr/bin/python ./testSDL_Pi_INA3221.py ".escapeshellarg($json);

$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

//var_dump($res);
echo $res;

echo 'end PHP program';



?>
