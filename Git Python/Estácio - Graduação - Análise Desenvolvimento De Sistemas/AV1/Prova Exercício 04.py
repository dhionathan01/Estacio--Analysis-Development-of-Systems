print("\n \n Alunos : Dhionathan L. Jobim | Cesar Augusto P. Machado | Marcos Eduardo Muller"
" |\n Rafael Teixeira Fernandes | Sara De Souza Mageste | Taylor Fidelis \n \n")

print("*******************************")
print("**********Exercício04**********")
print("*******************************\n \n")


tabuada=int(input("Montar a Tabuada de: "))
inicio=int(input("Começar por: "))
final=int(input("Terminar em: "))
if(inicio<final):
    print("Vou montar a tabuada de ", tabuada, "comecando em", inicio, "e terminando em ", final)
    while(inicio<=final):
        valort=tabuada*inicio
        print(tabuada,"x",inicio,"=",valort)
        inicio = inicio + 1

else:
    print("\n Opção Inválida \n O Valor Inicial informado é maior que o final")
