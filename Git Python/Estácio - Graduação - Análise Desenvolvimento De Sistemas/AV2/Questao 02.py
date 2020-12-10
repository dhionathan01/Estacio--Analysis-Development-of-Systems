exit="017000569999"
numero="0"
votos_florzinha=0
votos_dubai=0
votos_branco=0
votos_nulo=0
total_de_votos=0
print(" 1 - Candidato Florzinha \n 2 - Candidato Dubai \n 3 - Voto Branco \n Outro - Nulo")
while (numero != exit):
    numero=input("\n Digite o numero do candidato desejado: ")

    if (numero=="1"):
        print("Você votou no candidato Florzinha")
        votos_florzinha=votos_florzinha+1
        total_de_votos=total_de_votos+1

    elif (numero=="2"):
        print("Você votou no candidato Dubai")
        votos_dubai=votos_dubai+1
        total_de_votos=total_de_votos+1

    elif (numero=="3"):
        print("Você votou Branco")
        votos_branco=votos_branco+1
        total_de_votos=total_de_votos+1

    elif (numero!= exit):
        print("Você votou Nulo")
        votos_nulo=votos_nulo+1
        total_de_votos=total_de_votos+1

totaldvots=votos_florzinha+votos_dubai+votos_nulo+votos_branco
percentual_florzinha=(100*votos_florzinha)/total_de_votos
percentual_dubai=(100*votos_dubai)/total_de_votos
percentual_branco=(100*votos_branco)/total_de_votos
percentual_nulo=(100*votos_nulo)/total_de_votos
print("Votação encerrada")
print("Total de Votos: ",total_de_votos)
print("Total de Votos Florzinha: ",votos_florzinha)
print("Total de Votos Dubai: ", votos_dubai)
print("Total de Votos Branco: ", votos_branco)
print("Total de Votos Nulo: ", votos_nulo)
print("************ Tabela de Percentuais (%)*********   ")
print("Percetual de Votos Candidato Florzinha: {:.2f}%".format(percentual_florzinha))
print("Percetual de Votos Candidato Dubai: {:.2f}%".format(percentual_dubai))
print("Percetual de Votos Branco: {:.2f}%".format(percentual_branco))
print("Percetual de Votos Nulo: {:.2f}%".format(percentual_nulo))
