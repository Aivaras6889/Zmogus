class Zmogus:
    def __init__(self, vardas, pavarde, amzius, lytis, lokacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.lytis = lytis
        self.lokacija = lokacija

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.amzius}, {self.lytis}, {self.lokacija}\n"
    
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
            suma += int(zmogus.amzius)
        vidurkis = suma / len(zmoniu_sar)
        return vidurkis


zmoniu_sar = []

def prideti_zmogu(zmoniu_sar):
    while True:
        print("Iveskite duomenys(vardas, pavarde, lytis, amzius, vieta) noredami uzbaigti iveskite 'q' ")

        vardas= input("Iveskite savo varda: ")

        if vardas.lower() == "q":
            break
        pavarde = input("Iveskit savo pavarde: ")
        amzius = int(input("Iveskite savo amziu: "))
        lytis = input("Iveskite savo lyti: ")
        vieta = input("Iveskite vietove kurioje gyvenate(Miestas/Kaimas ...) ")

        asmuo = Zmogus(vardas, pavarde, amzius, lytis, vieta)
        zmoniu_sar.append(asmuo)

        for zmogus in zmoniu_sar:
            print(zmogus)
    
while True:
        print("\n--- Meniu ---")
        print("1 - Pridėti žmogų")
        print("2 - Rodyti žmonių sąrašą")
        print("3 - Apskaičiuoti amžiaus vidurkį")
        print("4 - Baigti programą")

        pasirinkimas = input("Pasirinkite: ")

        if pasirinkimas == "1":
            prideti_zmogu(zmoniu_sar)
        elif pasirinkimas == "2":
            print(Zmogus.atvaizduoti_zmones(zmoniu_sar))
        elif pasirinkimas == "3":
            vidurkis = Zmogus.skaiciuoti_vidurki(zmoniu_sar)
            print(f"\nAmžiaus vidurkis: {vidurkis:.1f} m.")
        elif pasirinkimas == "4":
            print("Programa baigta.")
            break
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")


    

    
    
