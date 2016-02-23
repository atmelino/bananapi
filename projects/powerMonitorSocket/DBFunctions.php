<?php

error_reporting(E_ALL);

date_default_timezone_set('Europe/London');


//print "before calling main()\n";

main();

//print "after calling main()\n";


function main()
{
	$hostname="localhost";
	$username="solarPanel";
	$password="solarPanel";
	$database="solarPanel";

	//print "function main() start\n";
	$json=$_GET['json'];
	$decoded = json_decode($_GET['json']);
	$functionString=$decoded->fs;
	//print "functionString=".$functionString."\n";

	$con=mysql_connect($hostname,$username,$password) or die("Error " . mysqli_error($con ));;
	mysql_select_db($database, $con);
	if(strcmp($functionString,'saveValues')==0)
	{
		//print "calling saveValues\n";
		//print "calling saveValues".$bv3."\n";
		saveValues($con,$database,$decoded);
	}
	if(strcmp($functionString,'showTables')==0)
	{
		showTables($con,$database);
	}
	if(strcmp($functionString,'loadValues')==0)
	{
		loadValues($con,$database,$decoded);
	}
	mysql_close($con);
}


function saveValues($con,$database,$decoded)
{
	//print "function saveValues() start\n";

	$lV3=$decoded->lV3;
	$cmA3=$decoded->cmA3;
	$pw3=$decoded->pw3;
	//print "lV3=".$lV3."\n";

	$sql = "INSERT INTO  `".$database."`.`myvalues` ";
	$sql .= "( `id` ,	`date` ,	`lV3` ,	`cmA3` ,	`pw3` )";
	$sql .=" VALUES ( NULL , NOW( )";
	$sql .=",'".$lV3."','".$cmA3."','".$pw3."'";
	$sql .=" );";
	//print $sql;
	$result = mysql_query($sql);
}



function showTables($con,$database)
{

	$sql = "SHOW tables FROM solarPanel";
	$result = mysql_query($sql);

	$myarray=array();

	while($row = mysql_fetch_assoc($result)) {
		print $row[1];

		//var_dump($row);
		$myarray['table'][]= $row['Tables_in_solarPanel'];
	}
	// create response object
	$encoded= json_encode($myarray);
	echo $encoded;



	//loop to show all the tables
	// 	$query1 = mysql_query("SHOW tables FROM solarPanel") or die ('cannot select tables');
	// 	while($table = mysql_fetch_array($query1))
	// 	{

	// 		echo "Table: ";
	// 		echo $table[0];
	// 	}


}



function loadValues($con,$database,$decoded)
{

	$date=$decoded->date;
	$sql = "SELECT * FROM ".$date;
	$result = mysql_query($sql);

	$myarray=array();

	while($row = mysql_fetch_assoc($result)) {
		//var_dump($row);
		$myarray['date'][]= $row['date'];
		$myarray['lV1'][]= $row['lV1'];
		$myarray['cmA1'][]= $row['cmA1'];
		$myarray['pw1'][]= $row['pw1'];
		$myarray['lV2'][]= $row['lV2'];
		$myarray['cmA2'][]= $row['cmA2'];
		$myarray['pw2'][]= $row['pw2'];
		$myarray['lV3'][]= $row['lV3'];
		$myarray['cmA3'][]= $row['cmA3'];
		$myarray['pw3'][]= $row['pw3'];
	}
	// create response object
	$encoded= json_encode($myarray);
	echo $encoded;


}



?>