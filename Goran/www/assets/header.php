<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
    <title>EE building - RPi temperature monitor</title>
<style type="text/css">
@import url('style.css');
</style>
</head>
<body>

<div id="header">
    <h1>
     RaspberryPi Temperature Monitor
    </h1>
    <h2>Temperature monitoring for DMS room, E119, and E501</h2>
</div>

<div id="nav">
    <ul>
    <!--<li><a href="view1.php">Current temperature - last measurement</a></li>-->
    <li><a href="index.php" title="Shows last 30 measurements.">Main page</a></li>
    <li><a href="last24hr.php" title="Shows last 24 hours or last 144 measurements.">View last 24 hours</a></li>
    <li><a href="last7days.php" title="Shows last 7 days or last 1k measurements.">View last 7 days</a></li>
    <li><a href="viewall.php" title="Dumps out whole database. Takes some time to load the page.">View all</a></li>
    <li><a href="about.php" title="Behind the scene">About</a></li>
    </ul>
</div>
<?php
//Connect to MySQL
mysql_connect('localhost', 'robin', 'raspberry') or die (mysql_error());
//Select database
mysql_select_db('dms_stats') or die (mysql_error());
?>
<div id="content">
