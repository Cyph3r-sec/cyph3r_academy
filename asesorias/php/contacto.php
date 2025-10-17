<?php
include 'conexion.php';

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $asunto = $_POST['asunto'];
    $mensaje = $_POST['mensaje'];

    $sql = "INSERT INTO contacto (nombre, correo, asunto, mensaje)
            VALUES ('$nombre', '$correo', '$asunto', '$mensaje')";

    if ($conn->query($sql)) {
        echo "<script>alert('📩 Mensaje enviado con éxito'); window.location='../contacto.php';</script>";
    } else {
        echo "<script>alert('❌ Error: ".$conn->error."'); window.history.back();</script>";
    }
}
?>
