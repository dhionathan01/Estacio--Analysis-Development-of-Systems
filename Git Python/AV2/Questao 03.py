cachorro_quente=3.00
q_cq=0
valortotalcq=0
bauru_simples=2.50
q_bs=0
valortotalbs=0
bauru_com_ovo=4.50
q_bo=0
valortotalbo=0
hamburguer=7.00
q_h=0
valortotalh=0
xtudo=11.00
q_x=0
valortotalx=0
refrigerante=5.00
q_r=0
valortotalr=0
quantidade=0
pedido=0
print("\n__________Cardapio_____________\n")
print("\nEspecificação           Código         Preço\n")
print("Cachorro Quente          100           R$ 3,00 \n")
print("Bauru Simples            101           R$ 2.50 \n")
print("Bauru com ovo            102           R$ 4.50 \n")
print("Hambúrguer               103           R$ 7.50 \n")
print("XTudo                    104           R$ 11.00 \n")
print("Refrigerante             105           R$ 5.00 \n")

print("\n Faça seu Pedido \n")
while (pedido != -1):
    pedido=int(input("Digite o Código do pedido ou (-1) para finalizar o pedido: "))
    if (pedido==100):
        print("\n Você escolheu Cachorro Quente \n")
        quantidade=int(input("Digite a quantidade: "))
        q_cq=q_cq+quantidade
        valortotalcq = valortotalcq + (cachorro_quente * quantidade)
        print("Total do Pedido: ", valortotalcq)

    elif(pedido==101):
        print("\n Você escolheu Bauru Simples \n")
        quantidade = int(input("Digite a quantidade: "))
        q_bs = q_bs + quantidade
        valortotalbs = valortotalbs + (bauru_simples * quantidade)
        print("Total do Pedido: ", valortotalbs)

    elif (pedido == 102):
        print("\n Você escolheu Bauru com ovo \n")
        quantidade = int(input("Digite a quantidade: "))
        q_bo = q_bo + quantidade
        valortotalbo = valortotalbo + (bauru_com_ovo * quantidade)
        print("Total do Pedido: ", valortotalbo)

    elif (pedido == 103):
        print("\n Você escolheu Hamburguer \n")
        quantidade = int(input("Digite a quantidade: "))
        q_h = q_h + quantidade
        valortotalh = valortotalh + (hamburguer * quantidade)
        print("Total do Pedido: ", valortotalh)

    elif (pedido == 104):
        print("\n Você escolheu XTudo \n")
        quantidade = int(input("Digite a quantidade: "))
        q_x = q_x + quantidade
        valortotalx = valortotalx + (xtudo * quantidade)
        print("Total do Pedido: ", valortotalx)

    elif (pedido == 105):
        print("\n Você escolheu Refrigerante \n")
        quantidade = int(input("Digite a quantidade: "))
        q_r = q_r + quantidade
        valortotalr = valortotalr + (refrigerante * quantidade)
        print("Total do Pedido: ", valortotalr)

print("\n Operação Encerrada \n")
valortotal=valortotalcq + valortotalbs + valortotalbo + valortotalh + valortotalx + valortotalr

print("\nEspecificação         Código     Qte     Preço        Totalp/ Item\n")
print("Cachorro Quente          100       {}    R$ 3,00       R$ {:.2f}\n".format(q_cq,valortotalcq))
print("Bauru Simples            101       {}    R$ 2.50       R$ {:.2f}\n".format(q_bs,valortotalbs))
print("Bauru com ovo            102       {}    R$ 4.50       R$ {:.2f}\n".format(q_bo,valortotalbo))
print("Hambúrguer               103       {}    R$ 7.50       R$ {:.2f}\n".format(q_h,valortotalh))
print("XTudo                    104       {}    R$ 11.00      R$ {:.2f}\n".format(q_x,valortotalx))
print("Refrigerante             105       {}    R$ 5.00       R$ {:.2f} \n".format(q_r,valortotalr))
print("   Valor Total do Pedido : R$. {:.2f}".format(valortotal))





