print("Responda as questões abaixo com S ou N \n")
contador=0
R1=input("\n Telefonou para a vítima ? :")
if(R1=="S"):
    contador=contador+1
R2=input("\n Esteve no local do Crime ? :")
if(R2=="S"):
    contador=contador+1
R3=input("\n Mora perto da vítima ? :")
if(R3=="S"):
    contador = contador + 1
R4=input("\n Devia para a vítima ? :")
if(R4=="S"):
    contador = contador + 1
R5=input("\n Já trabalhou com a vítima? :")
if(R5=="S"):
    contador = contador + 1
if(contador==2):
   print("A pessoa é : Suspeita")
elif (contador >= 3 and contador <=4):
       print("A pessoa é : Cúmplice")
elif (contador >= 5):
        print("A pessoa é : Assasino")
else:
    print("A Pessoa é :Inocente")

