
zmogus_sars = []
while True:
    print("Iveskite duomenys(vardas, pavarde, lytis, amzius, vieta) noredami uzbaigti iveskite 'q' ")

    vardas= input("Iveskite savo varda: ")
    if vardas == "q":
        break
    pavarde = input("Iveskit savo pavarde: ")
    lytis = input("Iveskite savo lyti: ")
    amzius = int(input("Iveskite savo amziu: "))
    vieta = input("Iveskite vietove kurioje gyvenate(Miestas/Kaimas ...) ")

    asmuo = Zmogus(vardas, pavarde, lytis, amzius, vieta)
    zmogus_sar.append(asmuo)




    
    
