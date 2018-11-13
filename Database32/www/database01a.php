
<?php
$servername = "localhost";
$username = "robin";
$password = "Micr0s0ft";

// Create Connection
$conn = new mysqli($servername, $username, $password);

// Check Connection
if ($conn->connect_error) {
    die("Connection Failed: ",$conn->connect_error);
}
echo "<p>Connected Successfully</p>";
?>
