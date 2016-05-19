<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View Min/Max Temps</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<div style="text-align: center;"><img
style="width: 125px; height: 125px;" alt="Raspberrypi"
src="large_logo_pi.png"></div>
<br>

<center><a href="index-temps.html">Back</a></center>

<br>
<center><font size = "6">Daily Minimum / Maximum Temperatures</font></center>
<br>


<?php

//Connect to MySQL
mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//Table starting tag and header cells
//echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Date</th><th>Outside Temp</th><th>Desk Temp</th></th><th>Ceiling Temp</th><th>Attic Temp</th><th>House Temp</th><th>Office Temp</th><th>Maple Creek</th></tr>";
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Date</th><th>Outside Temp</th><th>Desk Temp</th></th><th>Ceiling Temp</th><th>Attic Temp</th><th>House Temp</th><th>Office Temp</th></tr>";

// For loop to scroll through todays values & 9 previous by incrementing the interval of the CURDATE below
for ($i = 0; $i <=15; $i++){

 $mintemp00 = mysql_query("SELECT date, min(outside_temp), min(desk_temp), min(ceiling_temp), min(attic_temp), min(house_temp), min(office_temp), min(maple_house) FROM garage_temp WHERE date= (CURDATE() - INTERVAL $i DAY)");
 $maxtemp00 = mysql_query("SELECT date, max(outside_temp), max(desk_temp), max(ceiling_temp), max(attic_temp), max(house_temp), max(office_temp), max(maple_house) FROM garage_temp WHERE date= (CURDATE() - INTERVAL $i DAY)");
// While loop to pull out the min & max values of each voltage
 while(($row = mysql_fetch_array($mintemp00))and ($row1 = mysql_fetch_array($maxtemp00))){
   $slash = " / ";
   $mintemp0 = ROUND($row['min(outside_temp)'],2);
   $mintemp1 = ROUND($row['min(desk_temp)'],2);
   $mintemp2 = ROUND($row['min(ceiling_temp)'],2);
   $mintemp3 = ROUND($row['min(attic_temp)'],2);
   $mintemp4 = ROUND($row['min(house_temp)'],2);
   $mintemp5 = ROUND($row['min(office_temp)'],2);
//   $mintemp6 = ROUND($row['min(maple_house)'],2);
   $maxtemp0 = ROUND($row1['max(outside_temp)'],2);
   $maxtemp1 = ROUND($row1['max(desk_temp)'],2);
   $maxtemp2 = ROUND($row1['max(ceiling_temp)'],2);
   $maxtemp3 = ROUND($row1['max(attic_temp)'],2);
   $maxtemp4 = ROUND($row1['max(house_temp)'],2);
   $maxtemp5 = ROUND($row1['max(office_temp)'],2);
//   $maxtemp6 = ROUND($row1['max(maple_house)'],2);
//  echo "<tr><td>" . $row['date'] . "</td><td>" . ($mintemp0.$slash.$maxtemp0) . "</td><td>" . ($mintemp1.$slash.$maxtemp1) . "</td><td>" .($mintemp2.$slash.$maxtemp2) . "</td><td>" . ($mintemp3.$slash.$maxtemp3) . "</td><td>" . ($mintemp4.$slash.$maxtemp4) . "</td><td>" . ($mintemp5.$slash.$maxtemp5) . "</td><td>" . ($mintemp6.$slash.$maxtemp6) . "</td></tr>";
  echo "<tr><td>" . $row['date'] . "</td><td>" . ($mintemp0.$slash.$maxtemp0) . "</td><td>" . ($mintemp1.$slash.$maxtemp1) . "</td><td>" .($mintemp2.$slash.$maxtemp2) . "</td><td>" . ($mintemp3.$slash.$maxtemp3) . "</td><td>" . ($mintemp4.$slash.$maxtemp4) . "</td><td>" . ($mintemp5.$slash.$maxtemp5) . "</td></tr>";
 }
}

//Table closing tag
echo "</table>";

?>

<br>
<center><a href="index-temps.html">Back</a></center>

</body>
</html>
