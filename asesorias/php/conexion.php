<?php
$host = "localhost";
$db   = "asesorias_db";
$user = "root";
$pass = "OuHrKuB1PHmEBWLM03IL";

try {
    // Crear conexión PDO
    $conn = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    
    // Configurar para mostrar errores como excepciones
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Error de conexión: " . $e->getMessage());
}
?>
