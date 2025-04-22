class Zmogus:
    def __init__(self, vardas, pavarde, amzius, lytis, lokacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.lytis = lytis
        self.lokacija = lokacija

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.amzius} m., {self.lytis}, {self.lokacija},"

def atvaizduoti_zmones(zmoniu_sar):
    rezultatas="\n Žmonių sąrašas:\n"
    for zmogus in zmoniu_sar:
        rezultatas += f"{zmogus}"
    return rezultatas


def skaiciuoti_vidurki(zmoniu_sar):
    if len(zmoniu_sar) == 0:
        return 0 
    suma = 0
    for zmogus in zmoniu_sar:
        suma += zmogus.amzius
    vidurkis = suma / len(zmoniu_sar)
    
    return vidurkis


zmoniu_sar = []

while True:
    print("-- Menu --")
    print("_1. Ivedimas")
    print("_2. Saraso Avaizdavimas") 
    print("_3. Vidurkio Apskaiciavimas")   
    
    pasirinikimas = int(input("Iveskite pasirinkima(1/2/3): "))
    if pasirinikimas == " ":
            break

    match pasirinikimas:
        case 1:
            vardas= input("Iveskite savo varda: ")
            pavarde = input("Iveskit savo pavarde: ")
            lytis = input("Iveskite savo lyti: ")
            amzius = int(input("Iveskite savo amziu: "))
            vieta = input("Iveskite vietove kurioje gyvenate(Miestas/Kaimas ...) ")
            asmuo = Zmogus(vardas, pavarde, amzius, lytis, vieta)
            zmoniu_sar.append(asmuo)
        case 2:
            atvaizdavimas = atvaizduoti_zmones(zmoniu_sar)
            print(atvaizdavimas)
        case 3:
           vidurkis= skaiciuoti_vidurki(zmoniu_sar)
           print(vidurkis)
        

    
    
    



    

    
    
