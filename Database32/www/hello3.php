<!DOCTYPE html>
<html>
<head>
<title>
HELLO 3
</title>
</head>
<body>
<?php
$x = 5;
function myTest() {;
    // using x inside this function will generate an error
    echo "<p>Variable x insdie the funciton is: $x</p>";
    }
myTest();

echo "<p>Variable x outside the funciton is: $x</p>";
?>
</body>
</html>
