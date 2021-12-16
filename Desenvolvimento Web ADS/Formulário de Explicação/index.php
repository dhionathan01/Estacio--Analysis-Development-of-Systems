<?php
$page = $_GET["page"];
?>
<!DOCTYPE html>
<html lang="pt-br">
	<head> 
		<title>Manipulando Requisições</title>
		<meta name="author" content="Bruno Zonovelli">
		<meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
	 
	 
		<link rel='stylesheet' type='text/css' href='style.css'>
		<link rel="stylesheet" media="screen and (max-width: 600px)" href="smallscreen.css">
		<link rel="stylesheet" media="print" href="print.css">


	</head>
	
	<body>
	<header id="titulo"> Avaliação de aprendizado 1 </header>

	<nav>
		<ul>
		  <li><a href="index.php">Home</a></li>
		  <li><a href="index.php?page=formulario">Formulário</a></li>
		  <li><a href="index.php?page=tabela">Tabela</a></li>
		  <li><a href="index.php?page=lista">Listas</a></li>
		</ul>
	</nav>
	
	A pagina a ser exibida é: <h2><?php echo $page;?></h2>
		
		<?php
			if($page == "formulario"){​​
			include("formulario.php");
			}​​else if($page == "tabela"){​​
			include("tabela.php");
			}​​else if($page == "lista"){​​
			include("lista.php");
			}​​else{​​
			echo "<h2>Bem vindo</h2>";
			}​​
			?>
	
	</body>
</html>











