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
		saveValues($con,$database);
	}
	if(strcmp($functionString,'loadValues')==0)
	{
		loadValues($con,$database);
	}
	mysql_close($con);
}


function saveValues($con,$database)
{
	//print "function saveValues() start\n";

	$loadV=3.78;

	$sql = "INSERT INTO  `".$database."`.`myvalues` ";
	$sql .= "( `id` ,	`date` ,	`loadVolt` )";
	$sql .=" VALUES ( NULL , NOW( ),  '".$loadV."');	";
	print $sql;
	$result = mysql_query($sql);
}


function loadValues($con,$database)
{

	$sql = "SELECT * FROM myvalues";
	$result = mysql_query($sql);
	
	$myarray=array();
	
	while($row = mysql_fetch_assoc($result)) {
		$myarray['date'][]= $row['date'];
		$myarray['loadVolt'][]= $row['loadVolt'];
	}
	// create response object
	$encoded= json_encode($myarray);
	echo $encoded;
	

}



?>