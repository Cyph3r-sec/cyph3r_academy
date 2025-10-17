<?php include 'php/navbar.php'; ?>
<link rel="stylesheet" href="css/style.css">
<section class="section">
    <h2>Agenda tu Asesoría</h2>
    <form action="php/agendar.php" method="POST" class="form">
        <input type="text" name="nombre" placeholder="Nombre completo" required>
        <input type="email" name="correo" placeholder="Correo electrónico" required>
        <input type="text" name="tema" placeholder="Tema o materia" required>
        <input type="date" name="fecha" required>
        <input type="time" name="hora" required>
        <textarea name="mensaje" placeholder="Mensaje o comentarios adicionales"></textarea>
        <button type="submit" class="btn">Agendar</button>
    </form>
</section>
