<html>
<head>
<title>Add New Record in Books Database</title>
</head>
<body>
<?php
if(isset($_POST['add']))
{
$dbhost = 'localhost:3036';
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
   $author = addslashes ($_POST['author']);
   $series = addslashes ($_POST['series']);
   $isbn = addslashes ($_POST['isbn']);
   $price = addslashses ($_POST['price']);
}
else
{
   $title = $_POST['title'];
   $author = $_POST['author'];
   $series = $_POST['series'];
   $isbn = $_POST['isbn'];
   $price = $_POST['price'];
}
$format = $_POST['format'];

echo "Made it thru magic quotes\n";

$sql = "INSERT INTO books ".
       "(title, author, series, isbn, price, format) ".
       "VALUES('$title','$author','$series', '$isbn', '$price', $format)";
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
<td width="100">Book Name</td>
<td><input name="title" type="text" id="title"></td>
</tr>
<tr>
<td width="100">Book Author</td>
<td><input name="author" type="text" id="author"></td>
</tr>
<tr>
<td width="100">Book Series</td>
<td><input name="series" type="text" id="series"></td>
</tr>
<tr>
<td width="100">Book ISBN</td>
<td><input name="isbn" type="text" id="isbn"></td>
</tr>
<tr>
<td width="100">Book Price</td>
<td><input name="price" type="text" id="price"></td>
</tr>
<tr>
<td width="100">Book Format (Paper or eBook)</td>
<td><input name="format" type="text" id="format"></td>
</tr>
<tr>
<td width="100"> </td>
<td> </td>
</tr>
<tr>
<td width="100"> </td>
<td>
<input name="add" type="submit" id="add" value="Add Book">
</td>
</tr>
</table>
</form>
<?php
}
?>
<br>
<a href="index-books.html">Back</a>
</body>
</html>

