<style>
.error {color: #FF0000;}
</style>

<?php
// define variables and set to empty values
$saitIDErr = "";
$saitID = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["saitID"])) {
    $firstNameErr = "SAIT ID is required";
  } else {
    $saitID = test_input($_POST["saitID"]);
    // check if name only contains letters and whitespace
    if (!preg_match("/^[0-9]*$/",$saitID)) {
      $saitIDErr = "Only numbers allowed in first name"; 
      $saitID = "";
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

<p><span class="error">* required field</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  SAIT ID: <input type="text" name="saitID" value="<?php echo $saitID;?>">
  <span class="error">* <?php echo $saitIDErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>
<br>

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
$sql = "SELECT * FROM users where saitID = '$saitID'";
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
