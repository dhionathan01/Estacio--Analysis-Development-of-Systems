print("\n \n Alunos : Dhionathan L. Jobim | Cesar Augusto P. Machado | Marcos Eduardo Muller"
" |\n Rafael Teixeira Fernandes | Sara De Souza Mageste | Taylor Fidelis \n \n")

print("*******************************")
print("**********Exercício05**********")
print("*******************************\n \n")

saque = int(input("Valor mínimo saque: 10. \nValor máximo do saque: 600\nValor do saque: "))
while(saque !=0):
    if(saque<10 or saque>600):
        print("Valor inválido")
        saque = int(input("Valor mínimo saque: 10. \n Valor máximo do saque: 600\n Valor do saque: "))
    elif(saque>=10) and (saque<=600):
        resto_de_50 = saque % 100
        resto_de_10 = resto_de_50 % 50
        resto_de_5 = resto_de_10 % 10
        resto_de_1 = resto_de_5 % 5
        nota100=saque//100
        nota50=resto_de_50//50
        nota10=resto_de_10//10
        nota5=resto_de_5//5
        nota1 =resto_de_1//1
        print("Notas de 100:",nota100)
        print("Notas de 50:",nota50)
        print("Notas de 10:",nota10)
        print("Notas de 5",nota5)
        print("Notas de 1:",nota1)
        saque = int(input("Valor mínimo saque: 10. \n Valor máximo do saque: 600\n Valor do saque: "))
print("\n Operação Finalizada")