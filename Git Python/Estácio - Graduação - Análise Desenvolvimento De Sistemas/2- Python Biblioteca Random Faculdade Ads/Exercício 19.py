import random
gerador_1 = random.randrange(0,10)
gerador_2 = random.randrange(0,10)
gerador_3 = random.randrange(0,10)
gerador_4 = random.randrange(0,10)
gerador_5 = random.randrange(0,10)

contador_de_acertos = 0
for i in range (1,5+1):
    user=int(input("Digite um valor: "))
    if(gerador_1==user or gerador_2 == user or gerador_3 == user or gerador_4 == user or gerador_5 == user):
        print("Você Acertou")
        contador_de_acertos = contador_de_acertos + 1

print("O usuário teve :", contador_de_acertos, "Acertos")

