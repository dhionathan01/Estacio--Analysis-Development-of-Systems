import random
gerador = []
cartasJ =[]
jogador = 0
maquina = 0
cartasM = []
i = 0
print("\nBem vindo ao Jogo de Advinhação com Cartas\n")
while ( i < 5):
    valor = random.randrange(1, 13+1)
    if(not valor in gerador):
        gerador.append(valor)
        i = i + 1
cont=1
while (cont <=3):
    escolha=int(input("Escolha uma Carta (1 a 13) obs: A=1 J=11 Q=12 K= 13 :"))
    cont = cont + 1
    cartasJ.append(escolha)
    if(escolha in gerador):
        jogador=jogador+escolha
        print("Você acertou!")

    else:
        print("Você errou")

contm=1
while (contm <=3):
    escolha=random.randrange(1, 13+1)
    cartasM.append(escolha)
    print("Maquina escolheu: ",escolha)
    contm = contm + 1
    if(escolha in gerador):
        maquina=maquina+escolha
        print("Você acertou!")

    else:
        print("Você errou")

print("\n Cartas Aleatórias Geradas: ", gerador)
print("\n Cartas Escolhidas Pelo Jogador: ",cartasJ)
print("\n Cartas Escolhidas Pela Maquina: ",cartasM)
print("Placar \n Jogador {}x{} Maquina".format(jogador,maquina))
if(jogador>maquina):
    print("\n O Jogador Venceu a Disputa")
elif(maquina>jogador):
    print("\n A Maquina Venceu a Disputa")
elif(jogador==maquina):
    print("\n Os jogadores Empataram")