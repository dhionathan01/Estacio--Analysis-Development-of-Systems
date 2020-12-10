<section class="form">
			<fieldset>
				<legend>Avaliação da Disciplina</legend>
				<form action="form.php" method="POST">
        <label for="disciplina_selecionada" class="obrigatorio">Lista das disciplinas que você cursa:</label> 
          <select name="disciplina_selecionada" class="obrigatorio" id="cursos_list">
            
            <script>      
                    $(document).ready(function () {
                      
                      $.ajax({
                      url: "cursos.json", 
                      success: function(cursos_list){
                       var exibir = "";

                      for(var i=0; i<5;i++){
                        
                        exibir += '<option value="'+cursos_list[i].value+'">'+cursos_list[i].curso+'</option>'    
                      }
                      
                    
                               
                      $("#cursos_list").html(exibir);
                                  
                      },
                      error:function(result){
                        console.error("Falha ao recuperar arquivo")
                      },
                      });
                                   
                               
                      
                                  
                    });

                    

                  </script>
          </select>
          <BR>
          <BR>
          <label for="nome" class="obrigatorio">Nome do Professor: </label>
          <select name="nome" class="obrigatorio" id="JQ">
            
            <script>      
                    $(document).ready(function () {
                      
                      $.ajax({
                      url: "Professores.json", 
                      success: function(Professorres){
                       var exibir = "";

                      for(var i=0; i<4;i++){
                        
                        
                        exibir += '<option value="'+Professorres[i].value+'">'+Professorres[i].nome+'</option>'     
                      }
                      
                    
                               
                      $("#JQ").html(exibir);
                                  
                      },
                      error:function(result){
                        console.error("Falha ao recuperar arquivo")
                      },
                      });
                                   
                               
                      
                                  
                    });

                    

                  </script>
          </select> 

              
          <label for="hora_inicio" class="obrigatorio"> <BR>Hórario da Aula: <BR> Início: </label>
              <input type="time" name="hora_inicio" id="hora_inicio" required>
          <label for="hora_termino" class="obrigatorio">Fim</label>
              <input type="time" name="hora_termino" id="hora_término" required>
          <BR>
          <label for="ultimo_dia_presente" class="obrigatorio">Último dia que assistiu a aula:</label>
              <input type="date" name="ultimo_dia_presente" id="ultimo_dia_presente" required>
          <BR>
          <label for="numero_de_alunos">Número de Alunos:</label>
              <input type="number" min="1" max="100" name="numero_de_alunos" id="numero_de_alunos" class="inputcolor">
          <BR>
          <label>Nota para a Disciplina entre 1 e 5:</label>
              <input type="radio" name="nota" value="1" id="1"> <label for="nota">1</label>
              <input type="radio" name="nota" value="2" id="2"> <label for="nota">2</label>
              <input type="radio" name="nota" value="3" id="3"> <label for="nota">3</label>
              <input type="radio" name="nota" value="4" id="4"> <label for="nota">4</label>
              <input type="radio" name="nota" value="5" id="5"> <label for="nota">5</label>
          <BR>
          <label>Provas Realizadas:</label>
              <input type="checkbox" name="provas_realizadas1" value="AV1" id="AV1"><label for="AV1">1</label>
              <input type="checkbox" name="provas_realizadas2" value="AV2" id="AV2"><label for="AV2">2</label>
              <input type="checkbox" name="provas_realizadas3" value="AV3" id="AV3"><label for="AV3">3</label>
          <BR>
          <label for="descreva">Descreva sua Opinião sobre a Disciplina :</label>
          <BR>
              <textarea name="descreva"class="textarea" cols="65" rows="15"></textarea>
          <BR>
              <button type="submit" class="button">Enviar</button>
        </form>				
			
			</fieldset>
      		
		
        </section>