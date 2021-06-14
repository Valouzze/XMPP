<!DOCTYPE html>
<html>
<head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<body>

<h2>Historique de tout les evenements</h2>
<p><a href="/index.php">Accueil</a></p>
</body>
</html>


<?php
  include("evenements.php");
  $request_method = $_SERVER["REQUEST_METHOD"];

  switch($request_method)
  {
    case 'GET':
        getHistorique();
        break;
    default:
      header("HTTP/1.0 405 Method Not Allowed");
      break;
  }




?>