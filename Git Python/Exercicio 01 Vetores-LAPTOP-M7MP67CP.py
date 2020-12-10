principal = []
par = []
impar = []
for i in range (0,10):
    numero = int(input("Digite um numero: "))
    principal.append(numero)
    if(numero%2 == 0):
        par.append(numero)
    else:
        impar.append(numero)
print (principal)
print(par)
print(impar)