<?php


error_reporting(E_ALL);

echo "popen() DCTest01.py <br>\n";

//$cmd = "/usr/bin/python ./DCTest01.py 2>&1";
$cmd = "/usr/bin/python ./DCTest01.py";

$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

$resbr = str_replace("\n", "<br>",$res);
echo $resbr;
//var_dump($res);


?>
