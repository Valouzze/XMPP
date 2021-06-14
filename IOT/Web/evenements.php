<?php
  include("db_connect.php");
  $request_method = $_SERVER["REQUEST_METHOD"];

  function affichage($donnees){
    echo "\t<tr>\n";
    $cpt = 0;
    foreach ($donnees as $col_value) {
        if($cpt==2){
            if($col_value=='5'){echo "\t\t<td>Véhicule ordinaire</td>\n";}
            else if($col_value=='10'){echo "\t\t<td>Véhicule d'urgence</td>\n";}
            else if($col_value=='15'){echo "\t\t<td>Véhicule opérateur routier</td>\n";}
            else{echo "\t\t<td>Autre</td>\n";}
        }else if($cpt==3){
            if($col_value=='4'){echo "\t\t<td>Accident</td>\n";}
            else if($col_value=='5'){echo "\t\t<td>Embouteillage</td>\n";}
            else{echo "\t\t<td>Autre</td>\n";}
        }else if($cpt==4){
            echo "\t\t<td>".date('m/d/Y H:i:s', $col_value)."</td>\n";
        }else{
            echo "\t\t<td>$col_value</td>\n";
        }
        $cpt = $cpt+1;
    }
  }

  function getHistorique()
  {
    $query = 'SELECT * FROM evenements';
    $result = pg_query($query) or die('Échec de la requête : ' . pg_last_error());

    // Affichage des résultats en HTML
    echo "<table>\n<tr>
    <th>ID</th>
    <th>Identifiant du véhicule</th>
    <th>Type de Véhicule</th>
    <th>Cause</th>
    <th>Date</th>
  </tr>";

    while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
        affichage($line);
        echo "\t</tr>\n";
    }
    echo "</table>\n";

    // Libère le résultat
    pg_free_result($result);

    // Ferme la connexion
    pg_close($dbconn);
  }



?>