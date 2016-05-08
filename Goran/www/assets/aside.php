<?php
$min_query = mysql_query("SELECT min(dms_temp),1 FROM dms_temp WHERE date=CURDATE()");
$min_fetch = mysql_fetch_assoc($min_query);
$min_temp = ROUND($min_fetch['min(dms_temp)'],2);

$max_query = mysql_query("SELECT max(dms_temp) FROM dms_temp WHERE date=CURDATE()");
$max_fetch = mysql_fetch_assoc($max_query);
$max_temp = ROUND($max_fetch['max(dms_temp)'],2);
?>
<div id="aside">
<h4>Today's DMS extremes</h4>
<p>Min = <?php echo $min_temp; ?> &deg;C</p>
<p>Max = <?php echo $max_temp; ?> &deg;C</p>
</div>
