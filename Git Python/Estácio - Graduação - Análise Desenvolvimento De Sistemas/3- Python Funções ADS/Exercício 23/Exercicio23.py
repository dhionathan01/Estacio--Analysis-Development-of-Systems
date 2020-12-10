def pa (primeiro_termo, numero_termos, razao):
    ultimo_termo = primeiro_termo + (numero_termos - 1)*razao
    soma = 0
    for i in range (primeiro_termo, ultimo_termo + razao, razao ):
        print(i)
        soma = soma + i

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
numero_termos = int(input("Digite o número de termos da PA: "))
razao = int(input("Digite a razão da PA: "))
pa(primeiro_termo, numero_termos, razao)