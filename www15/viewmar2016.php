<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Temps</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<div style="text-align: center;"><img
style="width: 125px; height: 125px;" alt="Raspberrypi"
src="large_logo_pi.png"></div>
<br>

<center><a href="index-temps.html">Back</a></center>

<?php

//Connect to MySQL
//mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());
mysql_connect('localhost', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//echo "<center>".$mintemp1.$mintemp3['min(outside_temp)'],.PHP_EOL."</center>";
$mintemp1 = "Minimum Irricana Outside Temperature March 2016 = ";
//$mintemp2 = mysql_query("SELECT min(outside_temp),1 FROM garage_temp WHERE date=CURDATE()");
$mintemp2 = mysql_query("SELECT min(outside_temp),1 FROM garage_temp WHERE YEAR(date)=2016 AND MONTH(date)=3");
$mintemp3 = mysql_fetch_assoc($mintemp2);
$mintemp4 = ROUND($mintemp3['min(outside_temp)'],2);
echo "<center>".$mintemp1.$mintemp4.PHP_EOL."</center>";

//echo "<center>".$maxtemp1.$maxtemp3['max(outside_temp)'].PHP_EOL."</center>";
$maxtemp1 = "Maximum Irricana Outside Temperature March 2016 = ";
//$maxtemp2 = mysql_query("SELECT max(outside_temp) FROM garage_temp WHERE date=CURDATE()");
$maxtemp2 = mysql_query("SELECT max(outside_temp) FROM garage_temp WHERE YEAR(date)=2016 AND MONTH(date)=3");
$maxtemp3 = mysql_fetch_assoc($maxtemp2);
$maxtemp4 = ROUND($maxtemp3['max(outside_temp)'],2);
echo "<center>".$maxtemp1.$maxtemp4.PHP_EOL."</center>";

//echo "<center>".$mintemp5.$mintemp7['min(maple_house)'],.PHP_EOL."</center>";
$mintemp5 = "Minimum Maple Creek House Temperature March 2016 = ";
//$mintemp6 = mysql_query("SELECT min(maple_house),1 FROM garage_temp WHERE date=CURDATE()");
$mintemp6 = mysql_query("SELECT min(maple_house),1 FROM garage_temp WHERE YEAR(date) = 2016 AND MONTH(date)=3");
$mintemp7 = mysql_fetch_assoc($mintemp6);
$mintemp8 = ROUND($mintemp7['min(maple_house)'],2);
echo "<center>".$mintemp5.$mintemp8.PHP_EOL."</center>";

//echo "<center>".$maxtemp5.$maxtemp7['max(maple_house)'].PHP_EOL."</center>";
$maxtemp5 = "Maximum Maple Creek House Temperature March 2016 = ";
//$maxtemp6 = mysql_query("SELECT max(maple_house) FROM garage_temp WHERE date=CURDATE()");
$maxtemp6 = mysql_query("SELECT max(maple_house) FROM garage_temp WHERE YEAR(date)=2016 AND MONTH(date)=3");
$maxtemp7 = mysql_fetch_assoc($maxtemp6);
$maxtemp8 = ROUND($maxtemp7['max(maple_house)'],2);
echo "<center>".$maxtemp5.$maxtemp8.PHP_EOL."</center>";

//$result = mysql_query("SELECT * from garage_temp ORDER BY date DESC, time DESC LIMIT 20");
//$result = mysql_query("SELECT * from garage_temp WHERE date = CURDATE() ORDER BY time DESC");
//$result = mysql_query("SELECT * from garage_temp WHERE YEAR(date) = 2016 AND MONTH(date)=1 ORDER BY date ASC AND time DESC");
$result = mysql_query("SELECT * from garage_temp WHERE YEAR(date) = 2016 AND MONTH(date)=3 ORDER BY date ASC");

//Table starting tag and header cells
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Date</th><th>Time</th><th>Outside Temp</th><th>Desk Temp</th></th><th>Ceiling Temp</th><th>Attic Temp</th><th>House Temp</th><th>Office Temp</th><th>Maple Creek</th></tr>";
while($row = mysql_fetch_array($result)){
   //Display the results in different cells
   echo "<tr><td>" . $row['date'] . "</td><td>" . $row['time'] . "</td><td>" . $row['outside_temp'] . "</td><td>" . $row['desk_temp'] . "</td><td>" . $row['ceiling_temp'] . "</td><td>" . $row['attic_temp'] . "</td><td>" . $row['house_temp'] . "</td><td>" . $row['office_temp'] . "</td><td>" . $row['maple_house'] . "</td></tr>";
}
//Table closing tag
echo "</table>";

?>

<center><a href="index-temps.html">Back</a></center>


<br>

</body>
</html>


