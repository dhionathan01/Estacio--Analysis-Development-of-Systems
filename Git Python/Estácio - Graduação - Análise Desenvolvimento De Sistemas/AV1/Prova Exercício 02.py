print("\n \n Alunos : Dhionathan L. Jobim | Cesar Augusto P. Machado | Marcos Eduardo Muller"
" |\n Rafael Teixeira Fernandes | Sara De Souza Mageste | Taylor Fidelis \n \n")

print("*******************************")
print("**********Exercício02**********")
print("*******************************\n \n")

funcionario=input("Digite o Código da Provisão: \n D - Desenvolvedores \n T - Trainees \n A - Analista \n O - Outros \n : ")
salario=float(input("Digite o Salário Atual : "))
if(funcionario=="D"):
    valortotal=salario*1.15
elif(funcionario=="T"):
    valortotal=salario*1.10
elif(funcionario=="A"):
    valortotal=salario*1.07

else:
    valortotal=salario*1.05
print("Valor do Novo Salário:",valortotal)

