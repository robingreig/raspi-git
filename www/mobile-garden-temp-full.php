<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>Garden Temps</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
<style>
h1{font-size:350%;}
</style>
<h1>
<center>
Garden Temps
</center>
</head>
<br>
<body>
<?php

//Connect to MySQL
mysql_connect('raspi34.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//Current House Temperature
$housetemp1 = "Inside Garden Temp:";
$housetemp2 = mysql_query("SELECT garden_temp1 from garden_temp ORDER BY date DESC, time DESC LIMIT 1");
$housetemp3 = mysql_fetch_assoc($housetemp2);
$housetemp4 = ROUND($housetemp3[garden_temp1],2);
echo "<center>".$housetemp1.PHP_EOL;
echo $housetemp4.PHP_EOL."</center>";
//echo "<center>".$housetemp1.$housetemp4.PHP_EOL."</center>";
echo "<br>";

//Current Garage Desk Temperature
$desktemp1 = "Outside Garden Temp:";
$desktemp2 = mysql_query("SELECT garden_temp2 from garden_temp ORDER BY date DESC, time DESC LIMIT 1");
$desktemp3 = mysql_fetch_assoc($desktemp2);
$desktemp4 = ROUND($desktemp3[garden_temp2],2);
echo "<center>".$desktemp1.PHP_EOL;
echo $desktemp4.PHP_EOL."</center>";
//echo "<center>".$desktemp1.$desktemp4.PHP_EOL."</center>";
echo "<br>";

//Current Outside Temperature
$currtemp1 = "Outside Temp:";
$currtemp2 = mysql_query("SELECT outside_temp from garage_temp ORDER BY date DESC, time DESC LIMIT 1");
$currtemp3 = mysql_fetch_assoc($currtemp2);
$currtemp4 = ROUND($currtemp3[outside_temp],2);
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
echo "<br>";

//Minimum Garden Temperature
$mintemp1 = "Minimum Garden Temp Today: ";
$mintemp2 = mysql_query("SELECT min(garden_temp1),1 FROM garden_temp WHERE date=CURDATE()");
$mintemp3 = mysql_fetch_assoc($mintemp2);
$mintemp4 = ROUND($mintemp3['min(garden_temp1)'],2);
echo "<center>".$mintemp1.$mintemp4.PHP_EOL."</center>";
echo "<br>";

//Maximum Garden Temperature
$maxtemp1 = "Maximum Garden Temp Today: ";
$maxtemp2 = mysql_query("SELECT max(garden_temp1) FROM garden_temp WHERE date=CURDATE()");
$maxtemp3 = mysql_fetch_assoc($maxtemp2);
$maxtemp4 = ROUND($maxtemp3['max(garden_temp1)'],2);
echo "<center>".$maxtemp1.$maxtemp4.PHP_EOL."</center>";
echo "<br>";

?>
<center><a href="mobile-menu.php">Back</a></center>
</h1>
</body>
</html>


