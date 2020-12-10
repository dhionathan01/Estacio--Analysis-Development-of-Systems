pedido = 0
total = 0.0
qtditens = 0
valor = 0.0
while pedido != -1:
    valor=0
    pedido = int(input('Faça seu pedido: \n'
                       '100 - Cachorro-Quente\n'
                       '101 - Bauru Simples\n'
                       '102 - Bauru com Ovo\n'
                       '103 - Hamburgues\n'
                       '104 - X-Tudo\n'
                       '105 - Refrigerante\n'
                       '-1 - Finalizar Pedido\n'))
    qtditens = int(input('Digite a quantidade: '))
    if pedido == 100:
        valor = 3 * qtditens
        print('O valor a ser pago é: R${}'.format(valor))
    elif pedido == 101:
        valor = 2.50 * qtditens
        print('O valor a ser pago é: R${}'.format(valor))
    elif pedido == 102:
        valor = 4.50 * qtditens
        print('O valor a ser pago é: R${}'.format(valor))
    elif pedido == 103:
        valor = 7 * qtditens
        print('O valor a ser pago é: R${}'.format(valor))
    elif pedido == 104:
        valor = 11 * qtditens
        print('O valor a ser pago é: R${}'.format(valor))
    elif pedido == 105:
        valor = 5 * qtditens
        print('O valor a ser pago é: R${}'.format(valor))

    total = total + valor

print('O valor total do pedido é R${}'.format(total))