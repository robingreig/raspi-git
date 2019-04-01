<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$firstNameErr = $lastNameErr= "";
$firstName = $lastName = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["firstName"])) {
    $firstNameErr = "First Name is required";
  } else {
    $firstName = test_input($_POST["firstName"]);
    // check if name only contains letters and whitespace
    if (!preg_match("/^[a-zA-Z ]*$/",$firstName)) {
      $firstNameErr = "Only letters and white space allowed in first name"; 
      $firstName = "";
    }
  }
  
  if (empty($_POST["lastName"])) {
    $lastNameErr = "Last Name is required";
  } else {
    $lastName = test_input($_POST["lastName"]);
    // check if name only contains letters and whitespace
    if (!preg_match("/^[a-zA-Z ]*$/",$lastName)) {
      $lastNameErr = "Only letters and white space allowed in last name"; 
    }
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<h2>PHP Form Validation Example</h2>
<p><span class="error">* required field</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  First Name: <input type="text" name="firstName" value="<?php echo $firstName;?>">
  <span class="error">* <?php echo $firstNameErr;?></span>
  <br><br>
  Last Name: <input type="text" name="lastName" value="<?php echo $lastName;?>">
  <span class="error">* <?php echo $lastNameErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>
<br>

<?php
//echo "<h2>Your Input:</h2>";
//echo $firstName;
//echo "<br>";
//echo $lastName;
//echo "<br>";
?>

</body>
</html>
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

//$sql = "SELECT userID, firstName, lastname FROM users where firstName = 'Robin'";
$sql = "SELECT * FROM users where firstName = '$firstName'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    //Table starting tag and header cells
    echo " <table style='width: 90%; text-align: left; margin-left: auto; margin-right: auto;' border='0' cellpadding='2' cellspacing='2'><tr><th>UserID</th><th>Name</th><th>SAIT ID</th><th>Phone</th><th>SAIT Email</th><th>School</th><th>Program</th><th>Active</th><th>Waiver</th><th>Mentor</th><th>3dPrint</th><th>Router</th><th>Solder</th><th>Drillpress</th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row['userID'] . "</td><td>" . $row['firstName'] ." ". $row['lastName'] ."</td><td>". $row['saitID'] ."</td><td>". $row['phone'] ."</td><td>". $row['email1'] ."</td><td>". $row['school'] ."</td><td>". $row['program'] ."</td><td>". $row['active'] ."</td><td>". $row['waiver'] ."</td><td>". $row['mentor'] ."</td><td>". $row['3dprint'] ."</td><td>". $row['router'] ."</td><td>". $row['solder'] ."</td><td>". $row['drillpress'] ."<br>";
//        echo "id: " . $row["userID"]. " - Name: " . $row["firstName"]. " " . $row["lastName"]. " ". " - SAIT ID: ".$row["saitID"]."<br>";
    }
    echo "</table>";



//if ($result->num_rows > 0) {
    // output data of each row
//    while($row = $result->fetch_assoc()) {
//        echo "User ID: " . $row["userID"]. " - Name: " . $row["firstName"]. " " . $row["lastName"]. "<br>";
//    }
} else {
    echo "0 results";
}
$conn->close();

?>
