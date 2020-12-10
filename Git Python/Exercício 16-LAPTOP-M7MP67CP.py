maioridade=0
pessoa = 1
for i in range(0,10,1):
    idade=int(input("Digite a idade da {}° Pessoa: ".format(pessoa)))
    pessoa=pessoa+1
    if idade >=18 :
        maioridade=maioridade+1


print("Numero de Pessoas que tem maioridade : {}".format(maioridade))