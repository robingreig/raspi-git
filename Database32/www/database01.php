<!DOCTYPE html>
<html>
<head>
<title>
DATABASE 1
</title>
</head>
<body>
<?php

$servername = "localhost";
$username = "robin";
$password = "Micr0s0ft";

// Create Connection
$conn = mysqli_connect($servername, $username, $password);
//mysqli_connect($servername, $username, $password) or die(mysqli_connect);

// Check Connection
if (!$conn) {
    die("Connection Failed: ",mysqli_connect_error());
}
echo "<p>Connected Successfully</p>";
?>
</body>
</html>
