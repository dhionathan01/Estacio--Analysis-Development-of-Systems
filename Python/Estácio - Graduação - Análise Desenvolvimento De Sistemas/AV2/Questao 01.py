numeros=[]
total=0
for i in range (1,6):
    valor=int(input("Digite o {}° valor: ".format(i)))
    numeros.append(valor)
    total=total+valor


print("Maior Numero Digitado: ",max(numeros))
print("Menor Numero Digitado: ",min(numeros))
print("Média dos Numeros digitados: ",total/5)
