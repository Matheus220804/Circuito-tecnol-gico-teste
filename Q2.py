palavra1 = input()
palavra2 = input()
palavra3 = input()

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("Águia")
        else:
            print("Pomba")
    else:
        if palavra3 == "onivoro":
            print("Homem")
        else:
            print("Vaca")
else:
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            print("Pulga")
        else:
            print("Lagarta")
    else:
        if palavra3 == "hematofago":
            print("Sanguessuga")
        else:
            print("Minhoca")