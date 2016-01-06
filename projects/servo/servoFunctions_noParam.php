<?php


print "run python program\n";
//$cmd = "/usr/bin/python ./Servo_pos300.py 2>&1";
$cmd = "/usr/bin/python ./Servo_pos300.py";
$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);




?>
