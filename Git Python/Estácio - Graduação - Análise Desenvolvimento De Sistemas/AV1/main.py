import math



a = int(input("Digite o valor o coeficiente a: "))

b = int(input("Digite o valor o coeficiente b: "))

c = int(input("Digite o valor o coeficiente c: "))

delta = b**2-4*a*c

print ("O valor de x1 é: ", (-b+math.sqrt(delta))/2*a)

print ("O valor de x2 é: ", (-b-math.sqrt(delta))/2*a)