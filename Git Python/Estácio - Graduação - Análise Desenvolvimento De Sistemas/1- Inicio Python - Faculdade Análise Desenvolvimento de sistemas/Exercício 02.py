comprimento_area = float(input("Digite comprimento terreno: "))
largura_area = float(input("Digite largura do terreno: "))
comprimento_casa = float(input("Digite comprimento casa: "))
largura_casa = float(input("Digite largura casa: "))
areatotal=comprimento_area*largura_area
casatotal=largura_casa*comprimento_casa
area_livre = areatotal-casatotal
valor_total=(area_livre*100)/areatotal
print(valor_total)

