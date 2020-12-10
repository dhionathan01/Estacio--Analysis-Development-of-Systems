<?php
error_reporting(E_ERROR);
include("start_connectio_bd.php");

	$curso_nome 		 = $_POST['disciplina_selecionada'];
	$nome_professor 	 = $_POST['nome'];
	$hora_inicio 		 = $_POST['hora_inicio'];
	$hora_termino		 = $_POST['hora_termino'];
	$ultimo_dia_presente = $_POST['ultimo_dia_presente'];
	$numero_de_alunos	 = $_POST['numero_de_alunos'];
	$nota_disciplina	 = $_POST['nota_disciplina'];
	$provas_concluidas = $_POST['provas_concluidas'];
	$textarea			 = $_POST['descreva'];


$sql = "INSERT INTO avaliacao (id, materia_curso, prof_curso, hora_inicio,hora_fim, ultima_aula, num_alunos_turma, nota_disciplina, provas_feitas, descreva_experiencia) VALUES (null, '$curso_nome', '$nome_professor', '$hora_inicio','$hora_termino', '$ultimo_dia_presente', '$numero_de_alunos', '$nota_disciplina', '$provas_concluidas', '$textarea')";
$concluir = $conectar->query($sql);

if ($concluir) {
	echo '<script>alert("Conluido !!!")</script>';
	echo '<script> window.location.href = "sucesso.php" </script>';
} else {
	echo '<script>alert("Falha !!!")</script>';
}
