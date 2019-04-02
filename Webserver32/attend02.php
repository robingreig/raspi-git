<style>
.error {color: #FF0000;}
</style>

<?php
// define variables and set to empty values
$saitIDErr = "";
$saitID = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["saitID"])) {
    $saitIDErr = "SAIT ID is required";
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
<a href="attend01.php">Back</a>
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
    // output Welcome
    $row = mysqli_fetch_assoc($result);
      printf ("<h1>Welcome to the SAIT MakerSpace %s %s</h1>",$row['firstName'],$row['lastName']);
      sleep(2);
} else {
    echo "<h1>I cannot find you, please check with the MakerSpace volunteers</h1>";
    sleep(2);
}
$conn->close();

?>
