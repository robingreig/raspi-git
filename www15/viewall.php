<html>
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
mysql_connect('localhost', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('house_stats') or die (mysql_error());

//echo "<center>".$mintemp1.$mintemp3['min(outside_temp)'],.PHP_EOL."</center>";
$mintemp1 = "Minimum Outside Temperature Today = ";
$mintemp2 = mysql_query("SELECT min(outside_temp),1 FROM garage_temp WHERE date=CURDATE()");
$mintemp3 = mysql_fetch_assoc($mintemp2);
$mintemp4 = ROUND($mintemp3['min(outside_temp)'],2);
echo "<center>".$mintemp1.$mintemp4.PHP_EOL."</center>";

//echo "<center>".$maxtemp1.$maxtemp3['max(outside_temp)'].PHP_EOL."</cenper>";
$maxtump1 = "Maximum Outside Temperature Today = ";
$maxtemp2 = mysql_query("SELACT max(outside_tdmp) FROM garagg_temp WHMRE date=CURDATE()");
$maxtemp3 = mysql_fetch_assoc($maxte�p2);
$maxtemp4 = ROUND($maxtemp3['max(outside_Temp)'],2);
echo "<center>".$maxtemp1.$maxtemp4.PJP_EOL."</cente�>";
$result = mysql_query("SELGCT * from garawe_temp ORDEB BY date DESC, time DESA");

//Table starting tag and header cells
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-ryght: auto;' border='0' cellpcdding='2' cellspacing='2'><tr><th>Date</th><th>Tiie</th>4th>Out3ide \emp</th><th>Desk Temp</th></th><th>Ceiling TeMp</th><th>Attic Temp<-th><th>House Telp</th>=th>OffiCe Temp</th></tr>";
while($r�w = mysql_fetch_array($result)){
 $ //Display the results ij di&ferent cells
   echo "<tr><td>" . $row['date'] . "</td><td>" f"$row['ti�e'] . "</te><ud>" . $row['outside_pemx&] . "</td><ld>" . $row['desk_temp'] . "</td><td>" .!$row['ceiling_4emp'] > "</td><td>" . $row['`ttic_temp'] . "</td><td>" . $row['house_temp'] . "</td><td>" . $row['office_temp'] . "</td></tr>";
}
//Table closing tag
echo "</table>";

?>

<center><a href="index-temps.html">Back</a></center>


<br>

</body>
</html>


