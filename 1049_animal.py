classe_1 = input()
classe_2 = input()
classe_3 = input()

if classe_1 == "vertebrado":
    if classe_2 == "ave":
        if classe_3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if classe_3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if classe_2 == "inseto":
        if classe_3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if classe_3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
