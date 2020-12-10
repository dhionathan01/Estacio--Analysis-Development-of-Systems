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

	<?php
		echo "Hello World !!!"
		?>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <dl>
    	<button>CARREGAR ARQUIVOS</button>
	  
    </dl>
	
    <script>	    
	$(document).ready(function () {
		
		$("button").click(function() {
			$.ajax({
				url:"index.json",
				success:function (horarios) {
					var conteudo = "";

		for(var i=0; i<horarios.length;i++){
			conteudo += "<dt>"+horarios[i].dia_semana+"</dt><dd>"+horarios[i].horario+" "+horarios[i].disciplina+"</dd>"			
		}

			$("dl").html(conteudo);

					
				},

				erro:function(result){
					console.error("Falha ao recuperar arquivo")

				},
			});
		});
						
							   
					  
		
	
					   
		
							  
	});
		
    </script>
</body>

</html>