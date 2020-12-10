numero=int(input("Digite o valor :"))
contadorpar=0
contadorimpar=0
contador=1
while(contador<=100):
    numero=numero+1
    if(numero%2==0):
        contadorpar=contadorpar+1
    else:
        contadorimpar=contadorimpar+1
    contador=contador+1

print("Existem :",contadorpar,"Números Par\n")
print("Existem:",contadorimpar,"Números Impar")


