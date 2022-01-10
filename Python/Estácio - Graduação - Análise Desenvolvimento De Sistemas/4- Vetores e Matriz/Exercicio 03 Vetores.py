#vetor1=[5,10,15,20,25,30,35,40,45,50]
#vetor2=[7,14,21,28,35,42,49,56,63,70]
#vetor3=[]
#print("Vetor 1 : {}".format(vetor1))
#print("Vetor 2 : {}".format(vetor2))
#cont=0
#while (cont<=10):
#    vetor3.append(vetor1[cont])
#    vetor3.append(vetor2[cont])
 #   cont=cont+1
#print("Vetores intercalados : {}".format(vetor3))

vetor1 = []
vetor2 = []
vetor3 = []

print("Preenchendo o vetor 1")
for i in range(10):
    vetor1.append(float(input("Digite um valor: ")))

print("Preenchendo o vetor 2")
for j in range(10):
    vetor2.append(float(input("Digite um valor: ")))

print (vetor1)
print (vetor2)

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print (vetor3)
