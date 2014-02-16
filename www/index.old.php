<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Temps</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
<style>
h1{font-size:600%;}
h2{font-size:400%;}
</style>
<h1>
<center>
Irricana Temps
</center>
</h1>
</head>
<body>
<h2>
<?php

//Connect to MySQL
mysql_connect('localhost', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//Current Outside Temperature
$currtemp1 = "Outside Temp:";
$currtemp2 = mysql_query("SELECT outside_temp from garage_temp ORDER BY date DESC, time DESC LIMIT 1");
$currtemp3 = mysql_fetch_assoc($currtemp2);
$currtemp4 = ROUND($currtemp3[outside_temp],2);
echo "<h1>";
echo "<center>".$currtemp1.PHP_EOL;
echo $currtemp4.PHP_EOL."</center>";
//echo "<center>".$currtemp1.$currtemp4.PHP_EOL."</center>";
echo "<br>";

//Minimum Outside Temperature
$mintemp1 = "Minimum Outside Temp Today: ";
$mintemp2 = mysql_query("SELECT min(outside_temp),1 FROM garage_temp WHERE date=CURDATE()");
$mintemp3 = mysql_fetch_assoc($mintemp2);
$mintemp4 = ROUND($mintemp3['min(outside_temp)'],2);
echo "<center>".$mintemp1.$mintemp4.PHP_EOL."</center>";
echo "<br>";

//Maximum Outside Temperature
$maxtemp1 = "Maximum Outside Temp Today: ";
$maxtemp2 = mysql_query("SELECT max(outside_temp) FROM garage_temp WHERE date=CURDATE()");
$maxtemp3 = mysql_fetch_assoc($maxtemp2);
$maxtemp4 = ROUND($maxtemp3['max(outside_temp)'],2);
echo "<center>".$maxtemp1.$maxtemp4.PHP_EOL."</center>";
echo "</h1>";
?>
</h2>
<br>
</body>
</html>


