<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Temps</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
<style>
h1{font-size:350%;}
</style>
<h1>
<center>
Irricana Temps
</center>
</head>
<br>
<body>
<?php

//Connect to MySQL
mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//Current House Temperature
$housetemp1 = "House Temp:";
$housetemp2 = mysql_query("SELECT house_temp from garage_temp ORDER BY date DESC, time DESC LIMIT 1");
$housetemp3 = mysql_fetch_assoc($housetemp2);
$housetemp4 = ROUND($housetemp3[house_temp],2);
echo "<center>".$housetemp1.PHP_EOL;
echo $housetemp4.PHP_EOL."</center>";
//echo "<center>".$housetemp1.$housetemp4.PHP_EOL."</center>";
echo "<br>";

//Current Garage Desk Temperature
$desktemp1 = "Garage Desk Temp:";
$desktemp2 = mysql_query("SELECT desk_temp from garage_temp ORDER BY date DESC, time DESC LIMIT 1");
$desktemp3 = mysql_fetch_assoc($desktemp2);
$desktemp4 = ROUND($desktemp3[desk_temp],2);
echo "<center>".$desktemp1.PHP_EOL;
echo $desktemp4.PHP_EOL."</center>";
//echo "<center>".$desktemp1.$desktemp4.PHP_EOL."</center>";
echo "<br>";

//Current Attic Temperature
$attictemp1 = "Garage Attic Temp:";
$attictemp2 = mysql_query("SELECT attic_temp from garage_temp ORDER BY date DESC, time DESC LIMIT 1");
$attictemp3 = mysql_fetch_assoc($attictemp2);
$attictemp4 = ROUND($attictemp3[attic_temp],2);
echo "<center>".$attictemp1.PHP_EOL;
echo $attictemp4.PHP_EOL."</center>";
//echo "<center>".$attictemp1.$attictemp4.PHP_EOL."</center>";
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

//Minimum Outside Temperature
$mintemp5 = "Minimum Carefree Temp Today: ";
$mintemp6 = mysql_query("SELECT min(maple_house),1 FROM garage_temp WHERE date=CURDATE()");
$mintemp7 = mysql_fetch_assoc($mintemp6);
$mintemp8 = ROUND($mintemp7['min(maple_house)'],2);
echo "<center>".$mintemp5.$mintemp8.PHP_EOL."</center>";
echo "<br>";

//Maximum Outside Temperature
$maxtemp5 = "Maximum Carefree Temp Today: ";
$maxtemp6 = mysql_query("SELECT max(maple_house) FROM garage_temp WHERE date=CURDATE()");
$maxtemp7 = mysql_fetch_assoc($maxtemp6);
$maxtemp8 = ROUND($maxtemp7['max(maple_house)'],2);
echo "<center>".$maxtemp5.$maxtemp8.PHP_EOL."</center>";
?>
<center><a href="mobile-menu.php">Back</a></center>
</h1>
</body>
</html>


