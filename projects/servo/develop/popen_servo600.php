<?php


error_reporting(E_ALL);

echo "popen() set servo to 600 <br>\n";

//$cmd = "/usr/bin/python hello.py";

$cmd = "/usr/bin/python ./Servo_pos600.py 2>&1";


$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);


//process = subprocess.Popen(["your_cmd"]...)
//process.wait()


echo $res;
echo $res[2];

var_dump($res);


?>
