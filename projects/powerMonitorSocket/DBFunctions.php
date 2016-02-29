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
	if(strcmp($functionString,'SaveToExcel')==0)
	{
		SaveToExcel($con);
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
	$myarray=array();
	$myarray['message']='';

	$sql ="SELECT count(*) as count from ".$date;
	//$myarray['sql']=$sql;
	$result=mysql_query($sql);
	$count=mysql_fetch_assoc($result);
	$count=$count['count'];
	$myarray['count']=$count;
	$myarray['message'].=$count;


	$limit=$decoded->limit;
	$range=$decoded->range;
	$myarray['message'].=' '.$limit.' '.$range;
	$sql = "SELECT * FROM ".$date." LIMIT ".$limit.' , '.$range ;
	$result = mysql_query($sql);

	//var_dump($result);
	//$myarray['sqlresult']=$result;
	//$myresult = var_export($result, true);
	//$myarray['sqlresult']=$myresult;

	while($row = mysql_fetch_assoc($result)) {
		//var_dump($row);
		//$myarray['sqlresult'].=$row;
		//$myarray['sqlresult'].=var_export($row, true);
		$myarray['id'][]= $row['id'];
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


function SaveToExcel($con)
{
	//print "SaveToExcel() called<br>";

	$myarray=array();
	$myarray['message']='';
	$json=$_GET['json'];

	$decoded = json_decode($_GET['json']);

	$date=$decoded->date;

	$sql ="SELECT * from ".$date;
	//print $sql."<br>";
	//$result=mysql_query($sql) or reportErrorData();
	$result = mysql_query($sql);
	//print $row['A01'];

	$rows=0;
	while($row = mysql_fetch_assoc($result)) {
		$myarray['id'][]= $row['id'];
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
		$rows++;
	}

	// require the PHPExcel file
	require '../../lib/Classes/PHPExcel.php';

	// Create a new PHPExcel object
	$objPHPExcel = new PHPExcel();
	$objPHPExcel->getDefaultStyle()->getFont()
	->setName('Arila')
	->setSize(10);
	$objPHPExcel->getActiveSheet()->setTitle('data');


	$objPHPExcel->getActiveSheet()->setCellValue("A1", "id");
	$objPHPExcel->getActiveSheet()->setCellValue("B1", "Date");
	$objPHPExcel->getActiveSheet()->setCellValue("C1", "Volt");
	$objPHPExcel->getActiveSheet()->setCellValue("D1", "mA");
	$objPHPExcel->getActiveSheet()->setCellValue("E1", "mW");
	$objPHPExcel->getActiveSheet()->setCellValue("F1", "Volt");
	$objPHPExcel->getActiveSheet()->setCellValue("G1", "mA");
	$objPHPExcel->getActiveSheet()->setCellValue("H1", "mW");
	$objPHPExcel->getActiveSheet()->setCellValue("I1", "Volt");
	$objPHPExcel->getActiveSheet()->setCellValue("J1", "mA");
	$objPHPExcel->getActiveSheet()->setCellValue("K1", "mW");

	// Loop through the result set
	for ($rowpos = 0; $rowpos < $rows; $rowpos++) {
		$excelstring=sprintf('A%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['id'][$rowpos]);
		$excelstring=sprintf('B%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['date'][$rowpos]);
		$excelstring=sprintf('C%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['lV1'][$rowpos]);
		$excelstring=sprintf('D%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['cmA1'][$rowpos]);
		$excelstring=sprintf('E%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['pw1'][$rowpos]);
		$excelstring=sprintf('F%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['lV2'][$rowpos]);
		$excelstring=sprintf('G%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['cmA2'][$rowpos]);
		$excelstring=sprintf('H%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['pw2'][$rowpos]);
		$excelstring=sprintf('I%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['lV3'][$rowpos]);
		$excelstring=sprintf('J%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['cmA3'][$rowpos]);
		$excelstring=sprintf('K%d',$rowpos+2);
		$objPHPExcel->getActiveSheet()->setCellValue($excelstring,$myarray['pw3'][$rowpos]);
	}

	$objPHPExcel->getActiveSheet()->getColumnDimension('B')->setAutoSize(true);
	
	$objPHPExcel->getActiveSheet()->getStyle('C1:C'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('D1:D'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('E1:E'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('F1:F'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('G1:G'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('H1:H'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('I1:I'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('J1:J'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	$objPHPExcel->getActiveSheet()->getStyle('K1:K'.($rows+1))->getNumberFormat()->setFormatCode(PHPExcel_Style_NumberFormat::FORMAT_NUMBER_COMMA_SEPARATED1);
	
	// Save as an Excel BIFF (xls) file
	$objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');

	header('Content-Type: application/vnd.ms-excel');
	header('Content-Disposition: attachment;filename="myFile.xls"');
	header('Cache-Control: max-age=0');

	$objWriter->save('php://output');
	//exit();
}



?>