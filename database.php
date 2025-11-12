<?php

$db = mysqli_connect("localhost","root","","connect");

if(!$db)
{
    die("Connection failed: " . mysqli_connect_error());
}

?>
