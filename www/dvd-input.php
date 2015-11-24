<html>
<head>
<title>Add New Record in DVD's Database</title>
</head>
<body>
<?php
if(isset($_POST['add']))
{
$dbhost = 'raspi15.local:3036';
$dbuser = 'robin';
$dbpass = 'Micr0s0ft';
$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}

if(! get_magic_quotes_gpc() )
{
   $title = addslashes ($_POST['title']);
   $series = addslashes ($_POST['series']);
   $season = addslashes ($_POST['season']);
   $isbn = addslashes ($_POST['isbn']);
}
else
{
   $title = $_POST['title'];
   $series = $_POST['series'];
   $season = $_POST['season'];
   $isbn = $_POST['isbn'];
}
$price = $_POST['price'];

$sql = "INSERT INTO dvds ".
       "(title, series, season, isbn, price) ".
       "VALUES('$title','$series','$season', '$isbn', '$price')";
mysql_select_db('mediadb');
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
echo "Entered data successfully\n";
mysql_close($conn);

}
else
{
?>
<form method="post" action="<?php $_PHP_SELF ?>">
<table width="400" border="0" cellspacing="1" cellpadding="2">
<tr>
<td width="100">DVD Name</td>
<td><input name="title" type="text" id="title"></td>
</tr>
<tr>
<td width="100">DVD Series</td>
<td><input name="series" type="text" id="series"></td>
</tr>
<tr>
<td width="100">DVD Season</td>
<td><input name="season" type="text" id="season"></td>
</tr>
<tr>
<td width="100">DVD ISBN</td>
<td><input name="isbn" type="text" id="isbn"></td>
</tr>
<tr>
<td width="100">DVD Price</td>
<td><input name="price" type="text" id="price"></td>
</tr>
<tr>
<td width="100"> </td>
<td> </td>
</tr>
<tr>
<td width="100"> </td>
<td>
<input name="add" type="submit" id="add" value="Add DVD">
</td>
</tr>
</table>
</form>
<?php
}
?>
<br>
<a href="index-dvds.html">Back</a>
</body>
</html>

