<!doctype html>
<html>

<head>
    <meta charset="utf-8">
    <title>Introdução ao JQuery</title>
	
	<style>
	
	.negrito{
	   background-color:gray; 
	   color:pink;
	}
	
	</style>
	
</head>

<body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


	<?php
		echo "Hello World!!";
	?>
	



    <button>Carregar Horário</button>
	
    
    <dl>
	  Clique no Botão

    </dl>
	
    <script>	    
	$(document).ready(function () {
		
	 $("button").click(function(){
		$.ajax({
			url: "horarios.json", 
			success: function(horarios){
			  var conteudo = "";

			  for(var i=0; i<horarios.length;i++){
				conteudo += "<dt>"+horarios[i].dia_semana+"</dt><dd>"+horarios[i].horario+" "+horarios[i].disciplina+"</dd>"			
			  }
							   
			  $("dl").html(conteudo);
			},
			error:function(result){
			  console.error("Falha ao recuperar arquivo")
			},
		  });
		
	 });
	  		
							  
	});
		
    </script>
</body>

</html>