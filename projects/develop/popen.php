<?php

//$handle = popen("/bin/ls", "r");
//echo $handle;


error_reporting(E_ALL);

echo "popen() example <br>";

// Add redirection so we can get stderr.

$handle = popen('ls 2>&1', 'r');
echo "'$handle'; " . gettype($handle) . "\n";
echo "<br>";

echo "ls command: <br>";
$read = fread($handle, 2096);
echo $read;
pclose($handle);

?>
