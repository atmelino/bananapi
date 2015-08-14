<?php

//$handle = popen("/bin/ls", "r");
//echo $handle;



error_reporting(E_ALL);

echo "popen() example <br>";

// Add redirection so we can get stderr.

echo "read sensor: <br>";
$handle = popen('python BMP180_test.py 2>&1', 'r');
echo "'$handle'; " . gettype($handle) . "\n";
echo "<br>";

echo "sensor result: <br>";
$read = fread($handle, 2096);
echo $read;
pclose($handle);

?>
