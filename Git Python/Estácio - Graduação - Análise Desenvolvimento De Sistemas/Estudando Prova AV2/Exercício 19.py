import random
N1=random.randrange(0,10)
N2=random.randrange(0,10)
N3=random.randrange(0,10)
N4=random.randrange(0,10)
N5=random.randrange(0,10)
print(N1,N2,N3,N4,N5)
acertos=0

for i in range (0,5,1):
    valor=int(input("Digite um Valor: "))
    if(valor==N1 or valor==N2 or valor==N3 or valor==N4 or valor==N5):
        acertos=acertos+1


print("Numero de Acertos: ", acertos)