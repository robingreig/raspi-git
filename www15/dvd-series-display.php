<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View DVDs by Max Season</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<div style="text-align: center;"><img
style="width: 125px; height: 125px;" alt="Raspberrypi"
src="large_logo_pi.png"></div>
<br>

<center><a href="index-dvds.html">Back</a></center>

<?php

//Connect to MySQL
mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('mediadb') or die (mysql_error());

//echo "<center>".$mintemp1.$mintemp3['min(outside_temp)'],.PHP_EOL."</center>";
//echo "<center>".$mintemp1.$mintemp4.PHP_EOL."</center>";


//$result = mysql_query("SELECT * from dvds ORDER BY series ASC, max(season)");
//$result = mysql_query("SELECT * from dvds ORDER BY series ASC, where max(season)";
//$result = mysql_query("SELECT distinct(series) from dvds ORDER BY series ASC, where max(season)";
//$result = mysql_query("SELECT distinct(series) from dvds ORDER BY series ASC");
//$result = mysql_query("SELECT * from dvds GROUP BY series ASC WHERE season=max(season)");
//$result = mysql_query("SELECT * from dvds GROUP BY series ASC HAVING max(season)");
$result = mysql_query("SELECT * from (select * from dvds ORDER BY season DESC) dvds GROUP BY series ASC");

//Table starting tag and header cells
//echo "<center> <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Series</th><th>Season</th></tr></center>";
echo "<table style='width: 20%; text-align: center; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Series</th><th>Max Season</th></tr>";
while($row = mysql_fetch_array($result)){
   //Display the results in different cells
   echo "<tr><td>" . $row['series'] . "</td><td>" . $row['season'] . "</td></tr>";
}
//Table closing tag
echo "</table>";

?>

<center><a href="index-dvds.html">Back</a></center>

<br>

</body>
</html>


