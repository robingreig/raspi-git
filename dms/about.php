<?php include 'assets/header.php'; ?>
<?php include 'assets/aside.php'; ?>
<div id="maindata">
<h3>Welcome to our temperature monitoring system!</h3>
<p>This system consists of an Raspberry Pi board located in room E119. It has three One-Wire temperature sensors Dallas DS18B20 attached to the RasPi. Sensors are located in the DMS room, E119, and E501. Cron job on the RasPi runs the python sript every 10 minutes. Script takes measurements from each of the sensors and records date, time, and temperatures in a MySQL database.</p>
<p>If temperature in the DMS room reaches 25&deg;C, script sends an email to the <i>ICT.Electronics</i> group. </p>
<p>When the web page is accessed, PHP connects to the same MySQL database, pulls the requested data and displays it in the table.</p>
<p>The biggest credit for this goes to Robin Greig, who initiated the project and did the setup of the LAMP (Linux/Apache/MySQL/PHP) server on the RasPi board. He also wired the sensors and wrote the python script. I did minor improvements in the python and PHP code and did the CSS code. </p>
<p class="signature">Cheers,<br />Goran P.</p>
</div>
<?php include 'assets/footer.php'; ?>