
matriz=[]
pontos=[]
Interface = ["Nome","Pontuação ","Partidas Jogadas ","Número de Vitórias ", "Numero de Empates ", "Numero de Derrotas ", "Gols a Favor ", "Gols Contra ", "Saldo de Gols "]
numero_de_times=int(input("Digite o quantos times devem ser representados na Tabela: "))


for i in range (numero_de_times):
    times = []

    for i in range (9):
        time = input ("Digite {} do time :" .format(Interface[i]))
        times.append(time)
    matriz.append(times)


for contador in matriz:
        for exibir in times:
            print (exibir,end=" ")
        print()


