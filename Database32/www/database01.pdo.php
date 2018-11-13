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
$dbname = "makerspace";

// Create Connection
try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
//mysqli_connect($servername, $username, $password) or die(mysqli_connect);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "<p>Connected Successfully</p>";
    }
catch(PDOException $e)
    {
    echo "Connection Failed: ", $e->getMessage();
    }
?>
</body>
</html>
