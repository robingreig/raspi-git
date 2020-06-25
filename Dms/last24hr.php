<?php include 'assets/header.php'; ?>
<?php include 'assets/aside.php'; ?>
<div id="maindata">
<?php
    $result = mysql_query("SELECT * from dms_temp ORDER BY date DESC, time DESC LIMIT 144");
?>
<table>
<tr>
    <th>Date</th><th>Time</th><th>DMS Temp (&deg;C)</th><th>E119 Temp (&deg;C)</th><th>E501 Temp (&deg;C)</th>
</tr>
<?php
while($row = mysql_fetch_array($result)){
   //Display the results in different cells
    include 'assets/tablerow.php';
}
?>
</table>
</div>
<?php include 'assets/footer.php'; ?>