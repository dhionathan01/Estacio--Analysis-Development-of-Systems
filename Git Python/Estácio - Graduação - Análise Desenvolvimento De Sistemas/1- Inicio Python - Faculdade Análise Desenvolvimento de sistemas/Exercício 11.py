numero = int(input("Digite um número: "))
soma = 0
media = 0
contador = 0
while(numero != -1):
    soma = soma + numero
    contador = contador + 1
    numero = int(input("Digite um número: "))

media = soma/contador
print("O valor da média é: ", media)