<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View 100 Voltages</title>
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
//mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());
mysql_connect('raspi34.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//echo "<center>".$mintemp1.$mintemp3['min(outside_temp)'],.PHP_EOL."</center>";
///$mintemp1 = "Minimum Outside Temperature Today = ";
///$mintemp2 = mysql_query("SELECT min(outside_temp),1 FROM garage_temp WHERE date=CURDATE()");
///$mintemp3 = mysql_fetch_assoc($mintemp2);
///$mintemp4 = ROUND($mintemp3['min(outside_temp)'],2);
///echo "<center>".$mintemp1.$mintemp4.PHP_EOL."</center>";

//echo "<center>".$maxtemp1.$maxtemp3['max(outside_temp)'].PHP_EOL."</center>";
///$maxtemp1 = "Maximum Outside Temperature Today = ";
///$maxtemp2 = mysql_query("SELECT max(outside_temp) FROM garage_temp WHERE date=CURDATE()");
///$maxtemp3 = mysql_fetch_assoc($maxtemp2);
///$maxtemp4 = ROUND($maxtemp3['max(outside_temp)'],2);
///echo "<center>".$maxtemp1.$maxtemp4.PHP_EOL."</center>";

$result = mysql_query("SELECT * from voltages ORDER BY date DESC, time DESC LIMIT 100");

//Table starting tag and header cells
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Date</th><th>Time</th><th>APRX Battery</th><th>Blue Truck</th></th><th>Grey Truck</th><th>Secondary (Orange)</th><th>Primary (Green)</th><th>12V-1 (Blue)</th><th>12V-2 (Brown)</th></tr>";
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


