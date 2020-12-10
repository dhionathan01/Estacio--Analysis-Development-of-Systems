<!doctype html>

<html lang="pt-br">
	<head> 
		<title>Formulários</title>
		<meta name="author" content="Dhionathan Lanzoni Jobim">
		<meta charset="utf-8">
	</head>

	<link href="C:\Program Files/XAMPP/htdocs/estacio/Formulário Aula Inicio/css/style.css" type="text/css" rel="stylesheet">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
 
	
	 
	<body background="1.png" background-position="">
		
	
		<h2 id='titulo'>Formulário de cadastro de Aluno</h2>
		<div id="container-imagem"></div>
		
		<form action="#" method="POST">
			<label for="nome" class="obrigatorio" >Nome:</label> 
			<input type="text" class="b" id="nome" name="nome" size="50" maxlength="100"> <BR><BR>
			
			<label for="email" class="obrigatorio">Email:</label> <input class="b" type="email" id="email"  name="email" placeholder="email@dom.com"> <BR><BR>
			
			<label for="data"  class="obrigatorio">Data de Nascimento:</label> <input type="date"  id="data" name="data_nascimento"> <BR><BR>
			
			<label for="matricula" class="obrigatorio">Número Matricula:</label> <input type="number" class="b"  id="matricula" min="0" name="matricula"> <BR><BR>
			
			<label for="celular">Celular:</label> <input class="b" name="celular" id="celular"> <BR><BR>
			
			<label for="endereco">Endereço:</label> <input type="text" class="b" id="endereco" name="endereco"> <BR><BR>
			
			<label for="cpf">CPF</label><input type="text" class="b" id="cpf" name="CPF"> <BR><BR>

			<label for="senha"> Senha:</label> <input type="password" class="b" id="senha" name="senha"> <BR><BR>
			
			<label for="sexo">Sexo</label>
				
				  <input type="radio" name="sexo" id="masculino"    value="M"> <label for="masculino">Masculino</label>
				  <input type="radio" name="sexo" id="feminino"     value="F"> <label for="feminino">Feminino</label>
				  <input type="radio" name="sexo" id="naodeclarado" value="N"> <label for="naodeclarado">Não Declarar</label>
			 <BR><BR>
			
			Curso: <select class="b" name="curso">
				    <option class="b" value="">Selecione o seu curso...</option>
				    <option class="b" value="ADM">Administração.</option>
					<option class="b" value="ADS">Análise e Desenvolvimento de Sistemas.</option>
					<option class="b" value="CC">Ciências Contábeis.</option>
					<option class="b" value="CE">Comércio Exterior.</option>
					<option class="b" value="DM">Design de Moda.</option>
					<option class="b" value="DG">Design Gráfico.</option>
					<option class="b" value="DR">Direito.</option>
					<option class="b" value="EF">Educação Física.</option>
					<option class="b" value="REDES">Redes</option>
			       </select>
			       
			<BR><BR>

			Períodos Matriculado: <input type="checkbox" name="periodo" value="1"> 1
					  			  <input type="checkbox" name="periodo" value="2"> 2
								  <input type="checkbox" name="periodo" value="3"> 3
								  <input type="checkbox" name="periodo" value="4"> 4
								  <input type="checkbox" name="periodo" value="5"> 5
			<BR><BR>
			
			Deixe o seu comentário: <BR>
				<textarea class="b" name="comentario" cols="50" rows="10"></textarea>
				<br>
				<button style="background-color:blue; color:black" >enviar</button>


		</form>
		
		
	</body>

</html>


















<?php
/*

	$nome = "Dhionathan L Jobim";
	$idade = 30;

	echo $nome, " é ";

	if($idade>18){

		print ("Maior de 18 anos");
	}

		else{

			print ("Menor que 18 anos");
		}

		for($i=0;$i<$idade;$i++){

			if ($i == 0 ) echo "Parabéns ", " Pelo seus ", $i+1," anos","<BR>";
			elseif ( $i <= 18) echo "<i>", "Parabéns ", " Pelo seus ", $i+1," anos","<BR>", "</i>";	
			elseif ($i >=19) echo "<b>", "Parabéns ", " Pelo seus ", $i+1," anos","<BR>", "</b>";
		}

		/*?>

