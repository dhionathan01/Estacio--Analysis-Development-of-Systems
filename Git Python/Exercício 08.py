valor=float(input("Digite o Preço da mercadoria:"))
if(valor<=2):
 valorf=valor+0.15
 print("Valor Final : ",valorf)
if(valor>2 and valor<=5):
 valorf=valor+(valor/100)*2
 print("Valor Final : ",valorf)
if(valor>5 and valor<=20):
 valorf = valor + (valor / 100) * 10
 print("Valor Final : ", valorf)
elif (valor > 20):
 valorf = valor + (valor / 100) * 8
 print("Valor Final : ", valorf)



