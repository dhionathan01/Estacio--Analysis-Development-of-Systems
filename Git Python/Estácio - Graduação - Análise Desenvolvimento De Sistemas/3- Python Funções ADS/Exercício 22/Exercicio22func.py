def factor(valor):
    fatorial = 1
    contador = 1
    while (contador <= valor):
        fatorial = fatorial * contador
        contador = contador + 1

        print(fatorial)

    print("Valor da fatoração : ", fatorial)