<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View DVDs by Max Season</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<style>
h1{font-size:400%;}
</style>
<body>

<h1><center><a href="mobile-menu.php">Back</a></center></h1>

<?php

//Connect to MySQL
mysql_connect('raspi15.local', 'robin', 'Micr0s0ft') or die (mysql_error());

//Select database
mysql_select_db('mediadb') or die (mysql_error());

$result = mysql_query("SELECT * from (select * from dvds ORDER BY season DESC) dvds GROUP BY series ASC");

//Table starting tag and header cells
//echo "<center> <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Series</th><th>Season</th></tr></center>";
echo "<table style='width: 100%; font-size: 500%; text-align: center; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>Series</th><th>Season</th></tr>";
while($row = mysql_fetch_array($result)){
   //Display the results in different cells
   echo "<tr><td>" . $row['series'] . "</td><td>" . $row['season'] . "</td></tr>";
}
//Table closing tag
echo "</table>";

?>

<h1><center><a href="mobile-menu.php">Back</a></center></h1>

</body>
</html>


