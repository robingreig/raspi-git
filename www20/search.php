<?php
  include("./connect.php");

  $name=$_GET['title'];


  echo $name"\n";

  $query = "SELECT * FROM `books` WHERE title='$name'";
  $results= mysql_query($query);


  if (!empty($results)){
    echo "query successful" ;
    exit;
   }
  $row=mysql_fetch_assoc($results);
  echo "Title:".$row['title'];
  echo "Series:".$row['series'];
 ?>
