<html>
<head>
<title>Search the books database</title>
</head>
<body>
<?php
$dbhost = 'localhost:3036';
$dbuser = 'robin';
$dbpass = 'Micr0s0ft';
$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
?>

<form name="input" action="book-search-02.php" method="post">
  Title <input type="text" name="name" >
  Search<input type="submit" name="submit" Value="Submit">
</form>
</body>
</html>
