<?php


error_reporting(E_ALL);

echo "popen() DCTest.py <br>\n";

$cmd = "/usr/bin/python ./DCTest.py 2>&1";

$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

$resbr = str_replace("\n", "<br>",$res);
echo $resbr;
//var_dump($res);


?>
