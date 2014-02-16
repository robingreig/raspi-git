<?php

  $req=$_REQUEST['name'];
  echo $req."<br/>";

  $username="robin";
  $password="Micr0s0ft";
  $database="mediadb";

  mysql_connect("localhost",$username,$password);
  mysql_select_db($database) or die ("Unable to select database");

  $query = "SELECT * FROM books WHERE title='$req'";
  echo $query."<br/>";

  $result= mysql_query($query);
  echo $result."<br/>";

  $num=mysql_numrows($result);
//  mysql_query($result);
  mysql_close();

  $i=0

//  for ($i; $i < $num; $i++){
//    $f12=mysql_result($result,$i,"title");
//    $f11=mysql_result($result,$i,"series");
//    $f10=mysql_result($result,$i,"season");
//    echo $f12." ".$f11" ".$f10."<br />";
//    }
?>
