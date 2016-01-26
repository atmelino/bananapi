<?php

error_reporting(E_ALL);


$json=$_GET['json'];
//echo "PHP: ".$json."\n";


$cmd = "/usr/bin/python ./getINA3221.py ".escapeshellarg($json);
//$cmd = "/usr/bin/python ./testDate.py ".escapeshellarg($json);

$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

//var_dump($res);
//echo 'response from python';
echo $res;

//echo 'end PHP program';

?>
