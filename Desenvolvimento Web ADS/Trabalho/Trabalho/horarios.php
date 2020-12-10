
    
<?php
$table_horarios = array(
$table_horarios[0] = " Horas ",
$table_horarios[1] = "segunda",
$table_horarios[2] = "Banco de Dados",
$table_horarios[3] = "terça",
$table_horarios[4] = "Python",
$table_horarios[5] = "quarta",
$table_horarios[6] = "Desenvolvimento Web",
$table_horarios[7] = "quinta",
$table_horarios[8] = "Computação em Nuvem",
$table_horarios[9] = "sexta",
$table_horarios[10] = "-",
$table_horarios[11] = "18:55 - 19:45",
$table_horarios[12] = "19:45 - 20:35",
$table_horarios[13] = "intervalo",
$table_horarios[14] = "20:40 - 21:40",
    );
?>
 




  <div>
        <section class="tablet">
		
            <header> Quadro de Horários : <b>Dhionathan L. Jobim </b> </header>
            
			<article>
          <table>
                <?php

              echo "<tr>
                      <th>", $table_horarios[0], "</th>";

              for ($dias_da_semana = 1; $dias_da_semana <= 9; $dias_da_semana = $dias_da_semana + 2){
                  echo "<th>", $table_horarios[$dias_da_semana], "</th>";                  
              }

              echo "</tr><tr>";

              for ($horario_da_aula = 11; $horario_da_aula <= 14; $horario_da_aula++){

                  if($table_horarios[$horario_da_aula] == 'intervalo'){
                      echo "<td nowrap  style='color: blue;'>", $table_horarios[$horario_da_aula], "</td>";
                  }
                  else{
                      echo "<td nowrap>", $table_horarios[$horario_da_aula], "</td>";
                  }             

                  for ($materias_da_disciplina = 2; $materias_da_disciplina <= 10; $materias_da_disciplina = $materias_da_disciplina + 2){

                      if ($horario_da_aula == 13){
                          echo "<td style='color:blue;'> - </td>";
                      }
                      else{
                          echo "<td>", $table_horarios[$materias_da_disciplina], "</td>";
                      }
                        
                  }

                  echo "</tr>";
              }
          ?>
        </table>
      </article>
			 
            <footer> Dhionathan Lanzoni Jobim : <b><u>202001237331</b></u> </footer>
			
        </section>
        </div>

        <?php 

        $list_horarios = array(
        $list_horarios[0] = "segunda",
        $list_horarios[1] = "18:55 - 21:40",
        $list_horarios[2] = "Banco de dados",
        $list_horarios[3] = "terça",
        $list_horarios[4] = "18:55 - 21:40",
        $list_horarios[5] = "Python",
        $list_horarios[6] = "quarta",
        $list_horarios[7] = "18:55 - 21:40",
        $list_horarios[8] = "Desenvolvimento WEB",
        $list_horarios[9] = "quinta",
        $list_horarios[10] = "18:55 - 21:40",
        $list_horarios[11] = "Computação em nuvem",
        $list_horarios[12] = "sexta",
        $list_horarios[13] = "18:55 - 21:40",
        $list_horarios[14] = "Horario vago",
            );
            ?>

        <div class="oculte">
          <dl class='horariod'>
               <?php 
                    for ($dias_semana_list = 0; $dias_semana_list <= 12; $dias_semana_list = $dias_semana_list + 3){
                        echo "<dt>", $list_horarios[$dias_semana_list], "</dt><dd>", $list_horarios[$dias_semana_list+1], " : ", $list_horarios[$dias_semana_list+2], "</dd>";
                    }
                ?>

          </dl>
        </div>
