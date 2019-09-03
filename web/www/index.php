<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>
<head><title>Database test page</title>
<style>
th { text-align: left; }

table, th, td {
  border: 2px solid grey;
  border-collapse: collapse;
}

th, td {
  padding: 0.2em;
}
</style>
</head>

<body>
<h1>Database test page</h1>

<p>Showing contents of papers table:</p>

<table border="1">
<tr><th>Players</th>
  <th>Wins</th>
  <th>Losses</th>
  <th>Draws</th>
  <th>Winrate</tr></tr>

<?php
 
$db_host   = '192.168.2.11';
$db_name   = 'tictac_db';
$db_user   = 'webserver';
$db_passwd = 'web_pw';
$pdo_dsn = "mysql:host=$db_host;dbname=$db_name";
$pdo = new PDO($pdo_dsn, $db_user, $db_passwd);

$q = $pdo->query(
  "SELECT ". 
  "id, win, loss, draw, ". 
  "((win*2)+draw)/((win+loss+draw)*2)*100 AS winrate".
  " FROM players");

while($row = $q->fetch()){
  echo "<tr><td>".$row["id"]."</td><td>".$row["win"]."</td>".
  "<td>".$row["loss"]."</td><td>".$row["draw"]."</td>".
  "<td>".$row["winrate"]."%</td></tr>\n";
}

?>
</table>
</body>
</html>