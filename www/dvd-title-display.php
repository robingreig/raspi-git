<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View DVDs by Title</title>
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
mysql_connect('localhost', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('mediadb') or die (mysql_error());

$result = mysql_query("SELECT * from dvds ORDER BY title ASC, season ASC");

//Table starting tag and header cells
echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Title</th><th>Series</th><th>Season</th></tr>";
while($row = mysql_fetch_array($result)){
   //Display the results in different cells
   echo "<tr><td>" . $row['title'] . "</td><td>" . $row['series'] . "</td><td>" . $row['season'] . "</td></tr>";
}
//Table closing tag
echo "</table>";

?>

<center><a href="index-dvds.html">Back</a></center>


<br>

</body>
</html>


