<?php
$dbhost = 'localhost:3036';
$dbuser = 'robin';
$dbpass = 'Micr0s0ft';
$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
$sql = 'SELECT * FROM books';

mysql_select_db('mediadb');
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not get data: ' . mysql_error());
}
while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
{
    echo "Book Name : {$row['title']}  <br> ".
         "Book Author : {$row['author']} <br> ".
         "Book Series : {$row['series']} <br> ".
         "Book ISBN : {$row['isbn']} <br> ".
         "Book Price : {$row['price']} <br> ".
         "--------------------------------<br>";
} 
echo "Fetched data successfully\n";
mysql_close($conn);
?>
