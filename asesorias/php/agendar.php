<?php
include 'conexion.php';

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $tema = $_POST['tema'];
    $fecha = $_POST['fecha'];
    $hora = $_POST['hora'];
    $mensaje = $_POST['mensaje'];

    $sql = "INSERT INTO agenda (nombre, correo, tema, fecha, hora, mensaje)
            VALUES ('$nombre', '$correo', '$tema', '$fecha', '$hora', '$mensaje')";

    if ($conn->query($sql)) {
        echo "<script>alert('✅ Asesoría agendada con éxito'); window.location='../agenda.php';</script>";
    } else {
        echo "<script>alert('❌ Error: ".$conn->error."'); window.history.back();</script>";
    }
}
?>
