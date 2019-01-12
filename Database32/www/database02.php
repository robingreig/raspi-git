<!DOCTYPE html>
<html>
<head>
<title>
DATABASE 2
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
    foreach($conn->query('SELECT * from attendance where attendID = 112') as $row) {
        print_r($row);
//        print($row);
    }
    $conn = null;
}catch(PDOException $e)
    {
    echo "Error: " .  $e->getMessage() . "<br/>";
    die();
}
?>
</body>
</html>
