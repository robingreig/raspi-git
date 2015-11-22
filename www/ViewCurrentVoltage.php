<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Voltages</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<div style="text-align: center;"><img
style="width: 125px; height: 125px;" alt="Raspberrypi"
src="large_logo_pi.png"></div>
<br>

<center><a href="index-voltages.html">Back</a></center>

<?php

//Connect to MySQL
mysql_connect('localhost', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

$minvolt01 = "Minimum Today = ";
$minvolt02 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date=CURDATE()");
$minvolt03 = mysql_fetch_assoc($minvolt02);
$minvolt04 = ROUND($minvolt03['min(voltage1)'],2);
echo "<center>".$minvolt01.$minvolt04.PHP_EOL."</center>";

$minvolt11 = " = ";
$minvolt12 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date = (CURDATE() - INTERVAL 1 DAY)");
$minvolt13 = mysql_fetch_assoc($minvolt12);
$minvolt14 = ROUND($minvolt13['min(voltage1)'],2);
echo "<center>".$minvolt13[date].$minvolt11.$minvolt14.PHP_EOL."</center>";

$minvolt21 = " = ";
$minvolt22 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date = (CURDATE() - INTERVAL 2 DAY)");
$minvolt23 = mysql_fetch_assoc($minvolt22);
$minvolt24 = ROUND($minvolt23['min(voltage1)'],2);
echo "<center>".$minvolt23[date].$minvolt21.$minvolt24.PHP_EOL."</center>";

$minvolt31 = " = ";
$minvolt32 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date = (CURDATE() - INTERVAL 3 DAY)");
$minvolt33 = mysql_fetch_assoc($minvolt32);
$minvolt34 = ROUND($minvolt33['min(voltage1)'],2);
echo "<center>".$minvolt33[date].$minvolt31.$minvolt34.PHP_EOL."</center>";

$minvolt41 = " = ";
$minvolt42 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date = (CURDATE() - INTERVAL 4 DAY)");
$minvolt43 = mysql_fetch_assoc($minvolt42);
$minvolt44 = ROUND($minvolt43['min(voltage1)'],2);
echo "<center>".$minvolt43[date].$minvolt41.$minvolt44.PHP_EOL."</center>";

$minvolt51 = " = ";
$minvolt52 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date = (CURDATE() - INTERVAL 5 DAY)");
$minvolt53 = mysql_fetch_assoc($minvolt52);
$minvolt54 = ROUND($minvolt53['min(voltage1)'],2);
echo "<center>".$minvolt53[date].$minvolt51.$minvolt54.PHP_EOL."</center>";

$minvolt61 = " = ";
$minvolt62 = mysql_query("SELECT date, min(voltage1),1 FROM voltages WHERE date=(CURDATE() - INTERVAL 6 DAY)");
$minvolt63 = mysql_fetch_assoc($minvolt62);
$minvolt64 = ROUND($minvolt63['min(voltage1)'],2);
echo "<center>".$minvolt63[date].$minvolt61.$minvolt64.PHP_EOL."</center>";

//echo "<center>".$maxtemp1.$maxtemp3['max(outside_temp)'].PHP_EOL."</center>";
///$maxtemp1 = "Maximum Outside Temperature Today = ";
///$maxtemp2 = mysql_query("SELECT max(outside_temp) FROM garage_temp WHERE date=CURDATE()");
///$maxtemp3 = mysql_fetch_assoc($maxtemp2);
///$maxtemp4 = ROUND($maxtemp3['max(outside_temp)'],2);
///echo "<center>".$maxtemp1.$maxtemp4.PHP_EOL."</center>";

$result = mysql_query("SELECT * from voltages ORDER BY date DESC, time DESC LIMIT 1");

//Table starting tag and header cells
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Date</th><th>Time</th><th>APRX Battery</th><th>Black Truck</th></th><th>Grey Truck</th><th>Orange 1</th><th>Green 2</th><th>Blue 3</th><th>Bank 4</th></tr>";
while($row = mysql_fetch_array($result)){
   //Display the results in different cells
   echo "<tr><td>" . $row['date'] . "</td><td>" . $row[time] . "</td><td>" . $row['voltage0'] . "</td><td>" . $row['voltage1'] . "</td><td>" . $row['voltage2'] . "</td><td>" . $row['voltage3'] . "</td><td>" . $row['voltage4'] . "</td><td>" . $row['voltage5'] . "</td><td>" . $row['voltage6']. "</td></tr>";
}
//Table closing tag
echo "</table>";

?>

<br>
<center><a href="index-voltages.html">Back</a></center>

</body>
</html>


