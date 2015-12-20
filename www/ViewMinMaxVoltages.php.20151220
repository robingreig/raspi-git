<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Min/Max Voltages</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<div style="text-align: center;"><img
style="width: 125px; height: 125px;" alt="Raspberrypi"
src="large_logo_pi.png"></div>
<br>

<center><a href="index-voltages.html">Back</a></center>

<br>
<center><font size = "6">Daily Minimum / Maximum Voltages</font></center>
<br>


<?php

//Connect to MySQL
mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());
/*
Display the results in different cells
 Voltage0 = APRX Battery
 Voltage1 = Black Truck
 Voltage2 = Grey Truck
 Voltage3 = Bank 1
 Voltage4 = Bank 2
 Voltage5 = Bank 3
 Voltage6 = Bank 4
 Voltage7 = Bank 5
*/

//Table starting tag and header cells
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Date</th><th>APRX Battery</th><th>Black Truck</th></th><th>Grey Truck</th><th>Orange 1</th><th>Green 2</th><th>Blue 3</th><th>Bank 4</th></tr>";

// For loop to scroll through todays values & 9 previous by incrementing the interval of the CURDATE below
for ($i = 0; $i <=15; $i++){

 $minvolt00 = mysql_query("SELECT date, min(voltage0), min(voltage1), min(voltage2), min(voltage3), min(voltage4), min(voltage5), min(voltage6) FROM voltages WHERE date= (CURDATE() - INTERVAL $i DAY)");
 $maxvolt00 = mysql_query("SELECT date, max(voltage0), max(voltage1), max(voltage2), max(voltage3), max(voltage4), max(voltage5), max(voltage6) FROM voltages WHERE date= (CURDATE() - INTERVAL $i DAY)");
// While loop to pull out the min & max values of each voltage
 while(($row = mysql_fetch_array($minvolt00))and ($row1 = mysql_fetch_array($maxvolt00))){
   $slash = " / ";
   $minvolt0 = ROUND($row['min(voltage0)'],2);
   $minvolt1 = ROUND($row['min(voltage1)'],2);
   $minvolt2 = ROUND($row['min(voltage2)'],2);
   $minvolt3 = ROUND($row['min(voltage3)'],2);
   $minvolt4 = ROUND($row['min(voltage4)'],2);
   $minvolt5 = ROUND($row['min(voltage5)'],2);
   $minvolt6 = ROUND($row['min(voltage6)'],2);
   $maxvolt0 = ROUND($row1['max(voltage0)'],2);
   $maxvolt1 = ROUND($row1['max(voltage1)'],2);
   $maxvolt2 = ROUND($row1['max(voltage2)'],2);
   $maxvolt3 = ROUND($row1['max(voltage3)'],2);
   $maxvolt4 = ROUND($row1['max(voltage4)'],2);
   $maxvolt5 = ROUND($row1['max(voltage5)'],2);
   $maxvolt6 = ROUND($row1['max(voltage6)'],2);
  echo "<tr><td>" . $row['date'] . "</td><td>" . ($minvolt0.$slash.$maxvolt0) . "</td><td>" . ($minvolt1.$slash.$maxvolt1) . "</td><td>" .($minvolt2.$slash.$maxvolt2) . "</td><td>" . ($minvolt3.$slash.$maxvolt3) . "</td><td>" . ($minvolt4.$slash.$maxvolt4) . "</td><td>" . ($minvolt5.$slash.$maxvolt5) . "</td><td>" . ($minvolt6.$slash.$maxvolt6) . "</td></tr>";
 }
}

//Table closing tag
echo "</table>";

?>

<br>
<center><a href="index-voltages.html">Back</a></center>

</body>
</html>
