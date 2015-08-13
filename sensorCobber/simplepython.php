<?php

echo "call python test <br>";


$python = `python hello.py`;
//$python = `python simpletest.py`;
//$python = `simpletest.sh`;

echo $python;
echo "<br>";


echo "call python end";

 



?>

