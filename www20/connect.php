<?php
  $dbhost = 'localhost:3036';
  $dbuser = 'robin';
  $dbpass = 'Micr0s0ft';
  $conn = mysql_connect($dbhost, $dbuser, $dbpass);
  
  if(!$conn){
   die('Could not connect'.mysql_error() );  
  }

  $db_selected = mysql_select_db('mediadb');  

  if(!$db_selected){
   die('wrong'.mysql_error() );
  }
echo "DB selected";
?>
