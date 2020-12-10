a=float(input("Digite o Lado 1:"))
b=float(input("Digite o Lado 2:"))
c=float(input("Digite o Lado 3:"))
if(abs(b-c) < a < b + c and abs(a-c) < b < a + c and abs(a-b) < c < a+b):
    print("Existe")
else:
    print("Não existe")

