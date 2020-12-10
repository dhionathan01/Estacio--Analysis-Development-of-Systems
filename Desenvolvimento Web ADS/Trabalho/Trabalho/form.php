<?php
error_reporting(E_ERROR);
$curso_nome 		 = $_POST['disciplina_selecionada'];
$nome_professor 	 = $_POST['nome'];
$hora_inicio 		 = $_POST['hora_inicio'];
$hora_termino		 = $_POST['hora_termino'];
$ultimo_dia_presente = $_POST['ultimo_dia_presente'];
$numero_de_alunos	 = $_POST['numero_de_alunos'];
$nota_disciplina	 = $_POST['nota'];
$av_realizadas1		 = $_POST['provas_realizadas1'];
$av_realizadas2		 = $_POST['provas_realizadas2'];
$av_realizadas3		 = $_POST['provas_realizadas3'];
$provas_concluidas = $av_realizadas1 . ',' . $av_realizadas2 . ',' . $av_realizadas3;
$textarea			 = $_POST['descreva'];
?>

			

<head>
	<meta charset="utf-8">
	<meta name="author" content="Dhionathan Lanzoni Jobim">
	<link rel="stylesheet" type="text/css" href="CSS/style.css">
	<link rel="stylesheet" type="text/css" href="CSS/smallscreen.css">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="CSS/print.css">
</head>
<b>
	<h3 style="text-align: center;">Confirmação de Envio do Formulário</h3>
</b>
<section class="form">
	<fieldset>
		<legend>Avaliação da Disciplina</legend>
		<form action="autentication.php" method="POST">
			<label for="disciplina_selecionada" class="obrigatorio">Lista das disciplinas que você cursa:</label>
			<select name="disciplina_selecionada" class="obrigatorio" id="cursos_list" disabled>
				<option><?= $curso_nome ?></option>
			</select>
			<BR>
			<BR>
			<label for="nome" class="obrigatorio">Nome do Professor: </label>
			<select name="nome" class="obrigatorio" id="JQ" disabled>
				<option><?= $nome_professor ?></option>
			</select>
			<label for="hora_inicio" class="obrigatorio"> <BR>Hórario da Aula: <BR> Início: </label>
			<input value="<?= $hora_inicio ?>" type="time"  id="hora_inicio" disabled required>
			<label for="hora_termino" class="obrigatorio">Fim</label>
			<input value="<?= $hora_termino ?>" type="time" id="hora_término" disabled required>
			<BR>
			<label for="ultimo_dia_presente" class="obrigatorio">Último dia que assistiu a aula:</label>
			<input value="<?= $ultimo_dia_presente ?>" type="date" name="ultimo_dia_presente" id="ultimo_dia_presente" disabled required>
			<BR>
			<label for="numero_de_alunos">Número de Alunos:</label>
			<input value="<?= $numero_de_alunos ?>" type="number" min="1" max="100" name="numero_de_alunos" id="numero_de_alunos" class="inputcolor" disabled>
			<BR>
			<label>Nota para a Disciplina entre 1 e 5:</label>
			<input type="radio" name="nota" id="1" checked disabled> <label for="nota"><?= $nota_disciplina ?></label>
			<BR>
			<label>Provas Realizadas:</label>
			<input disabled type="checkbox" name="provas_realizadas1" value="AV1" id="AV1" <?= isset($av_realizadas1) ? 'checked' : '' ?>><label for="AV1">1</label>
			<input disabled type="checkbox" name="provas_realizadas2" value="AV2" id="AV2" <?= isset($av_realizadas2) ? 'checked' : '' ?>><label for="AV2">2</label>
			<input disabled type="checkbox" name="provas_realizadas3" value="AV3" id="AV3" <?= isset($av_realizadas3) ? 'checked' : '' ?>><label for="AV3">3</label>
			<BR>
			<label for="descreva">Descreva sua Opinião sobre a Disciplina :</label>
			<BR>
			<textarea disabled  class="textarea" cols="65" rows="15"><?= $textarea ?></textarea>
			<BR>
			<input type="hidden" value="<?= $curso_nome ?>" name="disciplina_selecionada"/>
			<input type="hidden" value="<?= $nome_professor ?>" name="nome"/>
			<input type="hidden" value="<?= $hora_inicio ?>" name="hora_inicio"/>
			<input type="hidden" value="<?= $hora_termino ?>" name="hora_termino"/>
			<input type="hidden" value="<?= $ultimo_dia_presente ?>" name="ultimo_dia_presente"/>
			<input type="hidden" value="<?= $numero_de_alunos ?>" name="numero_de_alunos"/>
			<input type="hidden" value="<?= $nota_disciplina ?>" name="nota_disciplina"/>
			<input type="hidden" value="<?= $provas_concluidas ?>" name="provas_concluidas"/>
			<input type="hidden" value="<?= $textarea ?>" name="descreva"/>
			<input name="enviar" type="submit" class="button">
			<button class="button"><a href="#" onClick="voltarPagina()">Cancelar</a></button>
		</form>
	</fieldset>
</section>

<script ipt>
	function voltarPagina() {
		var resultado = confirm("Tem certeza que deseja voltar ao formulário?");
		if (resultado == true) {
			JavaScript: window.history.back();
		}
	}

	var input = document.querySelector('input'),
		form = document.querySelector('form');

	form.addEventListener('submit', enviarDados, false);

	function enviarDados(event) {
		event.preventDefault();

		var resultado = confirm("Tem certeza que deseja enviar?");

		if (resultado == true) {
			form.submit();
			console.log('teste1');
		}
		console.log('teste2');
	}
</script>