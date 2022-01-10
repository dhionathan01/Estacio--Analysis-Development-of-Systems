# jogos.py
import forca
import Exercicio03


print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")
print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual jogo? "))
if (jogo == 1):
    print("Jogando forca")
    forca.jogar(20)
elif (jogo == 2):
    print("Jogando adivinhação")
    Exercicio03.jogar(23)