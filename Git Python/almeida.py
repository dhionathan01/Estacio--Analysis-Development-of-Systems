import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
vetor5 = []
vetor6 = []

quantidade = 0
soma = 0
item = 0
escolha = 0

id = 100
nome = 'Cachorro Quente'
preco = 3.00
vetor1.append(id)
vetor1.append(nome)
vetor1.append(preco)
vetor1.append(soma)
vetor1.append(quantidade)

id = 101
nome = 'Bauru Simples'
preco = 2.50
vetor2.append(id)
vetor2.append(nome)
vetor2.append(preco)
vetor2.append(soma)
vetor2.append(quantidade)

id = 102
nome = 'Bauru com ovo'
preco = 4.50
vetor3.append(id)
vetor3.append(nome)
vetor3.append(preco)
vetor3.append(soma)
vetor3.append(quantidade)

id = 103
nome = 'Hamburguer'
preco = 7.00
vetor4.append(id)
vetor4.append(nome)
vetor4.append(preco)
vetor4.append(soma)
vetor4.append(quantidade)

id = 104
nome = 'XTudo'
preco = 11.00
vetor5.append(id)
vetor5.append(nome)
vetor5.append(preco)
vetor5.append(soma)
vetor5.append(quantidade)

id = 105
nome = 'Refrigerante'
preco = 5.00
vetor6.append(id)
vetor6.append(nome)
vetor6.append(preco)
vetor6.append(soma)
vetor6.append(quantidade)

print("Itens: \n Cachorro Quente: 100 \n Bauru Simples: 101 \n")

while (escolha != -1):
    item = int(input("Digite o código do item que deseja \n \n"))
    if(item == 100):
        print("Você selecionou: Cachorro Quente \n")
        quantidade = int(input("Digite a quantidade que deseja \n"))
        soma = soma + (quantidade * vetor1[2])
        vetor1.append(soma)
        vetor1.append(quantidade)
    if(item == 101):
        print("Você selecionou: Bauru Simples \n")
        quantidade = int(input("Digite a quantidade que deseja \n"))
        soma = soma + (quantidade * vetor2[2])
        vetor2.append(soma)
        vetor2.append(quantidade)
    if(item == 102):
        print("Você selecionou: Bauru com ovo \n")
        quantidade = int(input("Digite a quantidade que deseja \n"))
        soma = soma + (quantidade * vetor3[2])
        vetor3.append(soma)
        vetor3.append(quantidade)
    if(item == 103):
        print("Você selecionou: Hambúrguer \n")
        quantidade = int(input("Digite a quantidade que deseja \n"))
        soma = soma + (quantidade * vetor4[2])
        vetor4.append(soma)
        vetor4.append(quantidade)    
    if(item == 104):
        print("Você selecionou: XTudo \n")
        quantidade = int(input("Digite a quantidade que deseja \n"))
        soma = soma + (quantidade * vetor5[2])
        vetor5.append(soma)
        vetor5.append(quantidade)
    if(item == 105):
        print("Você selecionou: Refrigerante \n")
        quantidade = int(input("Digite a quantidade que deseja \n"))
        soma = soma + (quantidade * vetor6[2])
        vetor6.append(soma)
        vetor6.append(quantidade)
    escolha = item
  

print("Fim da compra")
valor = 0
total = 0
valor = locale.currency((vetor1[2]), grouping=True, symbol=None)
total = locale.currency((vetor1[5]), grouping=True, symbol=None)

print("Especificação", "    Código", "    Preço", "    Quantidade", "    Total p/ Item")
print("%s    " % vetor1[1], "%d     " % (vetor1[0]), "R$ %s          " % valor, "%d" % (vetor1[6]), "        R$ %s" % total)
print("%s    " % vetor2[1], "%d     " % (vetor2[0]), "R$ %s          " % valor, "%d" % (vetor2[6]), "        R$ %s" % total)
print("%s    " % vetor3[1], "%d     " % (vetor3[0]), "R$ %s          " % valor, "%d" % (vetor3[6]), "        R$ %s" % total)
print("%s    " % vetor4[1], "%d     " % (vetor4[0]), "R$ %s          " % valor, "%d" % (vetor4[6]), "        R$ %s" % total)
print("%s    " % vetor5[1], "%d     " % (vetor5[0]), "R$ %s          " % valor, "%d" % (vetor5[6]), "        R$ %s" % total)
print("%s    " % vetor6[1], "%d     " % (vetor6[0]), "R$ %s          " % valor, "%d" % (vetor6[6]), "        R$ %s" % total)

