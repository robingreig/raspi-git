<?php include 'assets/header.php'; ?>
<?php include 'assets/aside.php'; ?>
<div id="maindata">
<?php
    $result = mysql_query("SELECT * from dms_temp ORDER BY date DESC, time DESC LIMIT 1008");
?>
<table>
<?php
include 'assets/tablehead.php';

while($row = mysql_fetch_array($result)){
   //Display the results in different cells
    include 'assets/tablerow.php';
}
?>
</table>
</div>
<?php include 'assets/footer.php'; ?>