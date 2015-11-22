
<?php
$link = mysql_connect('localhost', 'robin', 'Micr0s0ft');
if (!$link) {
    die('Could not connect: ' . mysql_error());
}
echo 'Connected successfully';
mysql_close($link);
?>

