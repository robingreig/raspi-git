<?php
header('Content-type: text/plain');

// How many days back? Change below ...
$days = 60;

// DON'T CHANGE BELOW THIS POINT ===========
$qty_limit = 144 * $days;

//Connect to MySQL
mysql_connect('localhost', 'robin', 'raspberry') or die (mysql_error());

//Select database
mysql_select_db('dms_stats') or die (mysql_error());

$result_dms = mysql_query("SELECT date, time, dms_temp from dms_temp ORDER BY date DESC, time DESC LIMIT ".$qty_limit);
$result_e119 = mysql_query("SELECT date, time, E119_temp from dms_temp ORDER BY date DESC, time DESC LIMIT ".$qty_limit);
$result_e501 = mysql_query("SELECT date, time, E501_temp from dms_temp ORDER BY date DESC, time DESC LIMIT ".$qty_limit);

$dms_string = "{\"key\": \"DMS\",\n\"values\": [";
while($row = mysql_fetch_array($result_dms)){
    //$dms_string .= "[\"".$row['date']." ".$row['time']."\", ".$row['dms_temp']."], ";
    $dms_string .= "[".strtotime($row['date']." ".$row['time'])."000, ".$row['dms_temp']."], ";
}
$dms_string = substr($dms_string, 0, -2); // chop off last two characters, comma-space, to have valid json
$dms_string .= "\n]}";

$e119_string = "{\"key\": \"E119\",\n\"values\": [";
while($row = mysql_fetch_array($result_e119)){
    //$e119_string .= "[\"".$row['date']." ".$row['time']."\", ".$row['E119_temp']."], ";
    $e119_string .= "[".strtotime($row['date']." ".$row['time'])."000, ".$row['E119_temp']."], ";
}
$e119_string = substr($e119_string, 0, -2);
$e119_string .= "\n]}";

$e501_string = "{\"key\": \"E501\",\n\"values\": [";
while($row = mysql_fetch_array($result_e501)){
    //$e501_string .= "[\"".$row['date']." ".$row['time']."\", ".$row['E501_temp']."], ";
    $e501_string .= "[".strtotime($row['date']." ".$row['time'])."000, ".$row['E501_temp']."], ";
}
$e501_string = substr($e501_string, 0, -2);
$e501_string .= "\n]}";

echo "[\n".$dms_string.", \n".$e119_string.", \n".$e501_string."\n]";
?>