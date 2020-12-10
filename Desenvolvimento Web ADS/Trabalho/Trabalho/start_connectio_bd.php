


<?php 

    $host = 'localhost';
    $user = 'root';
    $pass = '';
    $dbname = 'formulario';

    try{
        $conectar = mysqli_connect($host, $user, $pass, $dbname);
    }catch(Exception $e){
        echo '<script>alert("Falha ao conectar o banco");</script>';
    }

?>