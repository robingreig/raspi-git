<!DOCTYPE html>
<html>
<head>
<title>
DATABASE 2
</title>
</head>
<body>
<?php
echo "<table style='border: solid 1px black;'>"
echo "<tr><th>SAIT ID</th><th>Date</th><th>Time In</th></tr>";

class TableRows extends RecursiveIteratorIterator {
//class TableRows extends RecursiveIterator {
    function __construct($it) {
        parent::__construct($it, self::LEAVES_ONLY);
    }

    function current() {
        return "<td style='width:150px; border:1px solid black;'>".parent::current()."</td>";
    }

    function beginChildren() {
        echo "<tr>";
    }

    function endChildren() {
        echo "</tr>"."\n";
    }

}


$servername = "localhost";
$username = "robin";
$password = "Micr0s0ft";
$dbname = "makerspace";

// Create Connection
try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("SELECT saitID, date, timeIN FROM attendance");
    $stmt->execute();

    // Set the resulting array to associative
    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC);
    foreach(new TableRows(new RecursiveArrayIterator($stmt->fetchAll())) as $k=>$v) {
        echo $v;
    }
}

catch(PDOException $e) {
    echo "Error: ". $e->getMessage();
    }
$conn = null;
echo "</table>";

?>
</body>
</html>
