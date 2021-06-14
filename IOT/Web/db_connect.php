<?php
$dbconn = pg_connect("host=localhost dbname=save user=postgres password=test")
    or die('Connexion impossible : ' . pg_last_error());
?>