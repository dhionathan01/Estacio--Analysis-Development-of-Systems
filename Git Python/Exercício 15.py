inicio = int(input("inicio do intervalo: "))
fim = int(input("fim do intevalo: "))
for inicio in range(inicio,fim, 1):
   if inicio > 1:
      for i in range(2,inicio):
         if (inicio % i) == 0:
            break
      else:
         print(inicio)