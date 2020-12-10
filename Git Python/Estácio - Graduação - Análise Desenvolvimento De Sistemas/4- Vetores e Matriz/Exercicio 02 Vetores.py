i=1
Aluno=1
notas = []
aprovados = 0
while(i<=3):
    print("Aluno {}" .format(Aluno))
    nota1=float(input("Digite a Nota 1 do aluno :"))
    nota2=float(input("Digite a Nota 2 do aluno :"))
    nota3=float(input("Digite a Nota 3 do aluno :"))
    nota4=float(input("Digite a Nota 4 do aluno :"))

    valormedia=(nota1+nota2+nota3+nota4)/4
    print("Média atual: {:.2f}".format(valormedia))
    notas.append(valormedia)
    if (valormedia>=7):
        aprovados=aprovados+1

    Aluno=Aluno+1
    i=i+1

print("Media dos alunos : {}".format(notas))
print("Alunos aprovados : {}".format(aprovados))
