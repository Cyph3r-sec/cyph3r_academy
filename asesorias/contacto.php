<?php include 'php/navbar.php'; ?>
<link rel="stylesheet" href="css/style.css">
<section class="section">
    <h2>Contacto</h2>
    <form action="php/contacto.php" method="POST" class="form">
        <input type="text" name="nombre" placeholder="Tu nombre" required>
        <input type="email" name="correo" placeholder="Tu correo" required>
        <input type="text" name="asunto" placeholder="Asunto" required>
        <textarea name="mensaje" placeholder="Tu mensaje" required></textarea>
        <button type="submit" class="btn">Enviar</button>
    </form>
</section>
