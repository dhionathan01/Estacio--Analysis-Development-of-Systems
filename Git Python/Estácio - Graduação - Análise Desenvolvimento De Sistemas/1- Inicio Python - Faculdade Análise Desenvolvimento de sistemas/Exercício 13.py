valort=0
contador=0
numero=float(input("Digite as notas do aluno: "))
while(numero != -1):
    valort=valort+numero
    contador=contador + 1
    numero=float(input("Digite as notas do aluno "))

media=valort/contador
print("O valor da média é: ", media)

        if(media<6):
            print("Reprovado")
        else:
            print("Aprovado")