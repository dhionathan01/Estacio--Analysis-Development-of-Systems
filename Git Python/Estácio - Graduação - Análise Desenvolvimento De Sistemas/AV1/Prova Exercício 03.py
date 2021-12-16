print("\n \n Alunos : Dhionathan L. Jobim | Cesar Augusto P. Machado | Marcos Eduardo Muller"
" |\n Rafael Teixeira Fernandes | Sara De Souza Mageste | Taylor Fidelis \n \n")

print("*******************************")
print("**********Exercício03**********")
print("*******************************\n \n")

option = 1
valort = 0.0
contador = 1
while(option != 0):
    print("Loja do Sr. Manoel")
    valort = 0.0
    contador= 1
    print("Produto", contador, ":")
    contador=contador+1
    valor = float(input())
    while(valor != 0):
        valort=valort+valor
        print("Produto", contador, ":")
        contador = contador + 1
        valor = float(input())
    print("Valor Total da Compra :",valort)
    dinheiro=float(input("Digite o Valor Pago:"))
    troco=dinheiro-valort
    print("Troco:",troco)
    print("Operação Finalizada \n \n")