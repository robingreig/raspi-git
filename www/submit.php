<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"  http-equiv="content-type">
  <title>User Added</title>
  <link rel="stylesheet" type="text/css"  href="default.css">
</head>
<body>
<?
//the example of inserting data with variable from HTML form
//input.php
mysql_connect('localhost', 'root', 'Micr0s0ft') or die (mysql_error());
//mysql_connect('192.168.200.22, 'root', 'Micr0s0ft') or die (mysql_error());
mysql_select_db('raspberrypidb') or die (mysql_error());

$title = $_REQUEST['Title'];
$fname = $_REQUEST['fname'];
$sname = $_REQUEST['sname'];
$age = $_REQUEST['age'];
$email = $_REQUEST['email'];
		
mysql_query("INSERT INTO users(title, fname, sname, age, email) VALUES('$title', '$fname', '$sname', '$age', '$email')"); 

Print "Your table has been populated : ";

?>
<a href="index.html">Back</a>
</body>
</html>
