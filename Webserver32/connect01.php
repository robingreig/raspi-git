<html>
<br>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>View All</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<div style="text-align: center;"><img
style="width: 125px; height: 125px;" alt="Raspberrypi"
src="large_logo_pi.png"></div>
<br>

<center><a href="index-sait.html">Back</a></center>


<?php
$servername = "localhost";
$username = "robin";
$password = "Micr0s0ft";
$dbname = "makerspace";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

//$sql = "SELECT userID, firstName, lastName, saitID, phone, email1, school, program, active, waiver, mentor FROM users";
$sql = "SELECT * FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    //Table starting tag and header cells
    echo " <table style='width: 80%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>UserID</th><th>Name</th><th>SAIT ID</th><th>Phone</th><th>SAIT Email</th><th>School</th><th>Program</th><th>Active</th><th>Waiver</th><th>Mentor</th><th>3DPrint</th><th>Router</th><th>Solder</th><th>DrillPress</th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row['userID'] . "</td><td>" . $row['firstName'] ." ". $row['lastName'] ."</td><td>". $row['saitID'] ."</td><td>". $row['phone'] ."</td><td>". $row['email1'] ."</td><td>". $row['school'] ."</td><td>". $row['program'] ."</td><td>". $row['active'] ."</td><td>". $row['waiver'] ."</td><td>". $row['mentor'] ."</td><td>". $row['3dprint'] ."</td><td>". $row['router'] ."</td><td>". $row['solder'] ."</td><td>". $row['drillpress']."<br>";
//        echo "id: " . $row["userID"]. " - Name: " . $row["firstName"]. " " . $row["lastName"]. " ". " - SAIT ID: ".$row["saitID"]."<br>";
    }
    echo "</table>";

} else {
    echo "0 results";
}
$conn->close();
?>
<br>
<center><a href="index-sait.html">Back</a></center>
</body>
</html>
