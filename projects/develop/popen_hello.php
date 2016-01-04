<?php

//$handle = popen("/bin/ls", "r");
//echo $handle;


error_reporting(E_ALL);

echo "popen() example <br>";



/*
// Add redirection so we can get stderr.
$python = `python hello.py`;

//$handle = popen('ls 2>&1', 'r');
$handle = popen($python, 'r');
echo "'$handle'; " . gettype($handle) . "\n";
echo "<br>";


//echo "ls command: <br>";

$read = fread($handle, 2096);
echo $read;
pclose($handle);
*/


//$cmd = "/usr/bin/python hello.py";

$cmd = "/usr/bin/python ./hello.py 2>&1";


$handle = popen($cmd, 'r');
$res = fread($handle, 8192);
pclose($handle);

# Now you can make pretty printer about it.
echo $res;


return $res;



?>
