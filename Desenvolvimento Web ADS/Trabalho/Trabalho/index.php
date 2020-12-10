<?php
  error_reporting(E_ERROR);
  $page = $_GET["page"];
  ?>
<!DOCTYPE html>

<html>
     <head>
        <title>AV2 - Estácio Juiz de Fora</title>
        <meta charset="utf-8">
        <meta name="author" content="Dhionathan Lanzoni Jobim">
        <link rel="stylesheet" type="text/css" href="CSS/style.css">
        <link rel="stylesheet" type="text/css" href="CSS/smallscreen.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="CSS/print.css">

		

     </head>


     <body >
      <div id="background_body">
      <img src="https://portal.estacio.br/media/4683468/fapan.png" width="100%">
     

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        
	 
        <header id="titulo"> Projeto Web </header>
        </div>
     
    	<nav class="menuo">
            <ul>
              <li><a href="index.php?page=pagina_inicial">Página Inicial</a></li>
              <li><a href="index.php?page=horarios">Hórarios</a></li>
              <li><a href="index.php?page=av_professor">Avaliar Professor</a></li>
            </ul>
            <BR>
        </nav>
        <div class="allcontent">
        
        <div>

          <?php
                
                if($page == "horarios"){
                    include("horarios.php");
                }else if($page == "av_professor"){
                    include("av_professor.php");
                }else {
                  include("pagina_inicial.php");
                }

            ?>
		

		  </div>
      <div class="clear"></div>
    </div>
		
		
        <footer id="nome_professor"> Prof. Bruno Zonovelli </footer>
        
        <span>Conteúdo gerado para prova de AV1 e não pode ser reproduzido</span>
        </div>
     </body>
  </html>