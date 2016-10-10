<html>
<body>
 
 
<?php
$con = mysql_connect("localhost","robin","Micr0s0ft");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
 
mysql_select_db("mediadb", $con);
 
$sql="INSERT INTO books (title, author, series, isbn, price, format)
VALUES
('$_POST[title]','$_POST[author]','$_POST[series]','$_POST[isbn]','$_POST[price]','$_POST[format]')";
 
if (!mysql_query($sql,$con))
  {
  die('Error: ' . mysql_error());
  }
echo "1 record added";
 
mysql_close($con)
?>
</body>
</html>
