class Zmogus:
    def __init__(self, vardas, pavarde, amzius, lytis, lokacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.lytis = lytis
        self.lokacija = lokacija


    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.amzius} m., {self.lytis}, {self.lokacija}"
    
    


    #vardas, pavarde, amzius ,vieta ,lytis

zmoniu_sar = []


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
    zmoniu_sar.append(asmuo)






