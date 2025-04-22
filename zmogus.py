class Zmogus:
    def __init__(self, vardas, pavarde, amzius, lytis, lokacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.amzius = amzius
        self.lytis = lytis
        self.lokacija = lokacija


    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.amzius} m., {self.lytis}, {self.lokacija}"
    


    def atvaizduoti_zmones(zmoniu_sar):
        print("\n Žmonių sąrašas:")
        for zmogus in zmoniu_sar:
            print(zmogus)


    def skaiciuoti_vidurki(zmoniu_sar):
        if len(zmoniu_sar) == 0:
            return 0
        suma = 0
        for zmogus in zmoniu_sar:
            suma += zmogus.amzius
        vidurkis = suma / len(zmoniu_sar)
        return vidurkis
    
    dexdwgdvgewdyucfdegyu
    
    
    
