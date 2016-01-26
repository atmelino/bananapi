<?php

error_reporting(E_ALL);

global $hostname;
global $username;
global $password;
global $database;

$hostname="localhost";
$username="solarPanel";
$password="solarPanel";
$database="solarPanel";

date_default_timezone_set('Europe/London');


$con=mysql_connect($hostname,$username,$password) or die("Error " . mysqli_error($con ));;
mysql_select_db($database, $con);


$loadV=3.78;

$sql = "INSERT INTO  `".$database."`.`myvalues` ";
$sql .= "( `id` ,	`date` ,	`loadVolt` )";
$sql .=" VALUES ( NULL , NOW( ),  '".$loadV."');	";
print $sql;
$result = mysql_query($sql);







?>