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
Irricana Voltages
</center>
</head>
<br>
<body>
<?php

//Connect to MySQL
mysql_connect('localhost', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//Current APRX Voltage
$voltage0 = "APRX Voltage:";
$voltage00 = mysql_query("SELECT voltage0 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage000 = mysql_fetch_assoc($voltage00);
$voltage0000 = ROUND($voltage000[voltage0],2);
echo "<center>".$voltage0.PHP_EOL;
echo $voltage0000.PHP_EOL."</center>";
echo "<br>";

//Current Black Truck Voltage
$voltage1 = "Black Truck Voltage:";
$voltage11 = mysql_query("SELECT voltage1 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage111 = mysql_fetch_assoc($voltage11);
$voltage1111 = ROUND($voltage111[voltage1],2);
echo "<center>".$voltage1.PHP_EOL;
echo $voltage1111.PHP_EOL."</center>";
echo "<br>";

//Current Grey Truck Voltage
$voltage2 = "Grey Truck Voltage:";
$voltage22 = mysql_query("SELECT voltage2 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage222 = mysql_fetch_assoc($voltage22);
$voltage2222 = ROUND($voltage222[voltage2],2);
echo "<center>".$voltage2.PHP_EOL;
echo $voltage2222.PHP_EOL."</center>";
echo "<br>";

//Current Bank 1 Voltage
$voltage3 = "Bank 1 Voltage:";
$voltage33 = mysql_query("SELECT voltage3 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage333 = mysql_fetch_assoc($voltage33);
$voltage3333 = ROUND($voltage333[voltage3],2);
echo "<center>".$voltage3.PHP_EOL;
echo $voltage3333.PHP_EOL."</center>";
echo "<br>";

//Current Bank 2 Voltage
$voltage4 = "Bank 2 Voltage:";
$voltage44 = mysql_query("SELECT voltage4 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage444 = mysql_fetch_assoc($voltage44);
$voltage4444 = ROUND($voltage444[voltage4],2);
echo "<center>".$voltage4.PHP_EOL;
echo $voltage4444.PHP_EOL."</center>";
echo "<br>";

//Current Bank 3 Voltage
$voltage5 = "Bank 3 Voltage:";
$voltage55 = mysql_query("SELECT voltage5 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage555 = mysql_fetch_assoc($voltage55);
$voltage5555 = ROUND($voltage555[voltage5],2);
echo "<center>".$voltage5.PHP_EOL;
echo $voltage5555.PHP_EOL."</center>";
echo "<br>";

//Current Bank 4 Voltage
$voltage6 = "Bank 4 Voltage:";
$voltage66 = mysql_query("SELECT voltage6 from voltages ORDER BY date DESC, time DESC LIMIT 1");
$voltage666 = mysql_fetch_assoc($voltage66);
$voltage6666 = ROUND($voltage666[voltage5],2);
echo "<center>".$voltage6.PHP_EOL;
echo $voltage6666.PHP_EOL."</center>";
echo "<br>";

?>
<center><a href="mobile-menu.php">Back</a></center>
</h1>
</body>
</html>


