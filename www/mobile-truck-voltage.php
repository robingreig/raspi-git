<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Temps</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
<style>
h1{font-size:450%;}
</style>
<h1>
<center>
Black Truck Voltages
</center>
</head>
<br>
<body>
<?php

//Connect to MySQL
mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//Current Black Truck Voltage
$voltage0 = "Min Voltage Today: ";
$voltage00 = mysql_query("SELECT min(voltage1) from voltages WHERE date=CURDATE()");
$voltage000 = mysql_fetch_assoc($voltage00);
$voltage0000 = ROUND($voltage000['min(voltage1)'],2);
echo "<center>".$voltage0.$voltage0000.PHP_EOL."</center>";
echo "<br>";

// Black Truck Voltage - 1 day
$voltage1 = " = ";
$voltage11 = mysql_query("SELECT date, min(voltage1) from voltages WHERE date = DATE_SUB(CURDATE(), INTERVAL 1 DAY)");
$voltage111 = mysql_fetch_assoc($voltage11);
$voltage1111 = ROUND($voltage111['min(voltage1)'],2);
echo "<center>".$voltage111[date].$voltage1.$voltage1111.PHP_EOL."</center>";
echo "<br>";

// Black Truck Voltage - 2 day
$voltage2 = " = ";
$voltage22 = mysql_query("SELECT date, min(voltage1) from voltages WHERE date = DATE_SUB(CURDATE(), INTERVAL 2 DAY)");
$voltage222 = mysql_fetch_assoc($voltage22);
$voltage2222 = ROUND($voltage222['min(voltage1)'],2);
echo "<center>".$voltage222[date].$voltage2.$voltage2222.PHP_EOL."</center>";
echo "<br>";

// Black Truck Voltage - 3 day
$voltage3 = " = ";
$voltage33 = mysql_query("SELECT date, min(voltage1) from voltages WHERE date = DATE_SUB(CURDATE(), INTERVAL 3 DAY)");
$voltage333 = mysql_fetch_assoc($voltage33);
$voltage3333 = ROUND($voltage333['min(voltage1)'],2);
echo "<center>".$voltage333[date].$voltage3.$voltage3333.PHP_EOL."</center>";
echo "<br>";

// Black Truck Voltage - 4 day
$voltage4 = " = ";
$voltage44 = mysql_query("SELECT date, min(voltage1) from voltages WHERE date = DATE_SUB(CURDATE(), INTERVAL 4 DAY)");
$voltage444 = mysql_fetch_assoc($voltage44);
$voltage4444 = ROUND($voltage444['min(voltage1)'],2);
echo "<center>".$voltage444[date].$voltage4.$voltage4444.PHP_EOL."</center>";
echo "<br>";

// Black Truck Voltage - 5 day
$voltage5 = " = ";
$voltage55 = mysql_query("SELECT date, min(voltage1) from voltages WHERE date = DATE_SUB(CURDATE(), INTERVAL 5 DAY)");
$voltage555 = mysql_fetch_assoc($voltage55);
$voltage5555 = ROUND($voltage555['min(voltage1)'],2);
echo "<center>".$voltage555[date].$voltage5.$voltage5555.PHP_EOL."</center>";

?>
<center><a href="mobile-menu.php">Back</a></center>
</h1>
</body>
</html>


