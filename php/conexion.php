<?php
$host = "localhost";
$user = "root";
$pass = "OuHrKuB1PHmEBWLM03IL";
$db = "asesorias_db";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}
?>
