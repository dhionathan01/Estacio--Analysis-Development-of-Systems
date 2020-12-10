numeros=int(input("Quantos Numeros Deseja Inserir : "))
numeros_impares=0
contador=1
for i in range (0,numeros,1):
    valor=int(input("Digite {}° valor: " .format(contador)))
    contador=contador+1
    if(valor%2==0):
        numeros_impares=numeros_impares+0

    else:
        numeros_impares=numeros_impares+1

print("Quantidade de Numeros impares: ",numeros_impares)