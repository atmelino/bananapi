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

//$json=$_GET['json'];
//$decoded = json_decode($_GET['json']);


echo "connecting to database<br>\n";
echo "hostname: ".$hostname."<br>\n";
echo "username: ".$username."<br>\n";
echo "database: ".$database."<br>\n";

mysql_connect($hostname,$username,$password);
echo "database connection on $hostname established<br>\n";

mysql_select_db($database) or die(mysql_error());
echo "database $database selected<br>\n";


createValuesTable();

mysql_close();


function createValuesTable()
{
	global $database;

	$sql = "CREATE  TABLE IF NOT EXISTS myvalues ";
	$sql .=" ( `id` INT NOT NULL AUTO_INCREMENT ";
	$sql .=",  PRIMARY KEY (`id`) ";
	$sql .=", username VARCHAR(45) NOT NULL";
	$sql .=", date DATETIME  ";
	$sql .=", loadVolt float  ";
	$sql .=", loadAmp float  ";
	$sql .=", power float  ";
	$sql .="  ) ENGINE=InnoDB;";
	print $sql."<br>";

	$success=mysql_query($sql) or reportErrorData();

	if($success==true)
	{
		echo "solar panel values table $table created";
		echo "<br>";
	}

}


function reportErrorData()
{
	echo mysql_error();
	echo "<br>";
}

?>