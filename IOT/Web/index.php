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

<h2>Accidents et Embouteillages</h2>
<p><a href="/log.php">Historique des evenements</a></p>
</body>
</html>


<?php

$strJsonFileContents = file_get_contents("events.json");
$date = date_create();
$json_decoded = json_decode($strJsonFileContents);
echo "<table>
  <tr>
    <th>Id véhicule</th>
    <th>Type de véhicule</th>
    <th>Type d'evenements</th>
    <th>Date</th>
  </tr>
 ";
foreach($json_decoded as $result){
        echo '<tr>';
        echo '<td>'.$result->station_id.'</td>';
        if($result->station_type=='5'){echo "<td>Véhicule ordinaire</td>";}
        else if($result->station_type=='10'){echo "<td>Véhicule d'urgence</td>";}
        else if($result->station_type=='15'){echo "<td>Véhicule opérateur routier</td>";}
        else{echo "<td>Autre</td>";}

        if($result->cause_code=='4'){echo "<td>Accident</td>";}
        else if($result->cause_code=='5'){echo "<td>Embouteillage</td>";}
        else{echo "<td>Autre</td>";}

        echo '<td>'.date('m/d/Y H:i:s', $result->time).'</td>';
        echo '</tr>';

}
echo '</table>';
?>