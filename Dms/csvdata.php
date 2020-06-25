<?php
header('Content-type: text/plain');
//Connect to MySQL
mysql_connect('localhost', 'robin', 'raspberry') or die (mysql_error());

//Select database
mysql_select_db('dms_stats') or die (mysql_error());

$result = mysql_query("SELECT * from dms_temp ORDER BY date DESC, time DESC LIMIT 1008");

$return_string = "date,time,dms,e119,e501\n";
    
while($row = mysql_fetch_array($result)){
    $return_string .= $row['date'].",".$row['time'].",".$row['dms_temp'].",".$row['E119_temp'].",".$row['E501_temp']."\n";
}

echo $return_string;
?>