def recebe (idade):
    valora =int( idade / 365)
    valorm=int(idade%365)/12
    valord =int(idade%365)%12
    print("Dias de Vida: ",int(valord))
    print("Meses de Vida: ",int(valorm))
    print("Anos de Vida: ",int(valora))