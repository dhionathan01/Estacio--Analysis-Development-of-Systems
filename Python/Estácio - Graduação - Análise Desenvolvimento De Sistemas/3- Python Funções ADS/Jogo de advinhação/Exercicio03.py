def jogar (numero):


    print("*******************************")
    print("Bem Vindo ao jogo de advinhação")
    print("*******************************")
    print("numero_passado", numero)
    #Este é um comentário por linha
    '''
    Este é um comentário 
    por linhas
    '''
    import random

    numero_secreto = random.randint(1,20)
    total_de_tentativas = 3
    for rodada in range(1, total_de_tentativas + 1):

        numero_digitado = input("Digite o seu número: ")
        print("Você digitou: ", numero_digitado)
        numero_digitado = int(numero_digitado)

        acertou = numero_secreto == numero_digitado
        maior = numero_digitado > numero_secreto
        menor = numero_digitado < numero_secreto

        if (acertou):
            print("Você acertou!")
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    print("Fim do jogo")