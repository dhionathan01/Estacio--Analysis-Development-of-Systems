<h2 id='titulo' class="verde">Formulário de cadastro de Aluno</h2>
	

<form action="#" method="POST" autocomplete="off">
	<label for="nome" class="obrigatorio">Nome:</label> 
	<input type="text" id="nome" name="nome" size="50" maxlength="100"> <BR><BR>
	
	<label for="email">Email:</label> 
	<input type="email"  
				  name="email" 
				  id="email" 
				  placeholder="email@dom.com" autocomplete="off"> <BR><BR>
	
	<label for="data_nascimento">Data de Nascimento:</label> 
	<input type="date" 
		   id="data_nascimento"
		   name="data_nascimento"> <BR><BR>

	<label for="matricula" class="obrigatorio">Número Matricula:</label> 
	<input type="number" 
			id="matricula"
			min="0" 
			name="matricula"
			required> <BR><BR>

	 <label for="celular">Celular:</label> 
	 <input name="celular" id="celular" > <BR><BR>
	
	 <label for="endereco">Endereço:</label> 
	 <input type="text" name="endereco" id="endereco"> <BR><BR>
	
	 
	 <label for="CPF">CPF:</label> 
	 <input type="text" name="CPF" id="CPF"> <BR><BR>

	<label for="senha">Senha:</label> 
	<input type="password" name="senha" id="senha"> <BR><BR>
	
	<label>Sexo:</label> <input type="radio" 
				 name="sexo" 
				 id="masculino"    
				 value="M"> <label for="masculino">Masculino</label>
		  <input type="radio" name="sexo" id="feminino"     value="F" style="width: 30px;"> <label for="feminino">Feminino</label>
		  <input type="radio" name="sexo" id="naodeclarado" value="N" style="width: 30px;"> <label for="naodeclarado">Não Declarar</label>
	 <BR><BR>
	
	<label for="curso">Curso:</label> 
	<select name="curso">
			<option value="">Selecione o seu curso...</option>
			<option value="ADM">Administração.</option>
			<option value="ADS">Análise e Desenvolvimento de Sistemas.</option>
			<option value="CC">Ciências Contábeis.</option>
			<option value="CE">Comércio Exterior.</option>
			<option value="DM">Design de Moda.</option>
			<option value="DG">Design Gráfico.</option>
			<option value="DR">Direito.</option>
			<option value="EF">Educação Física.</option>
			<option value="REDES">Redes</option>
		   </select>
		   
	<BR><BR>

	<label>Períodos Matriculado:</label> <input type="checkbox" name="periodo" value="1" id="p1"> <label for="p1">1</label>
						  <input type="checkbox" name="periodo" value="2" id="p2"> <label for="p2">2</label>
						  <input type="checkbox" name="periodo" value="3" id="p3"> <label for="p3">3</label>
						  <input type="checkbox" name="periodo" value="4" id="p4"> <label for="p4">4</label>
						  <input type="checkbox" name="periodo" value="5" id="p5"> <label for="p5">5</label>
	<BR><BR>
	
	<label for="comentario">Deixe o seu comentário:</label> <BR>
	<textarea name="comentario" id="comentario" cols="50" rows="10"></textarea>

	<BR><BR>
	<button> Enviar </button>
</form>		









