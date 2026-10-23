import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunnit


# Pääohjelma

# 1. Tehdään 10 autoa listaan
autot = []
for i in range(1, 11):
    rekisteri = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))

# 2. Kilpailu
kilpailu_käynnissä = True
tunnit = 0

while kilpailu_käynnissä:
    tunnit = tunnit + 1
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_käynnissä = False

# 3. Tulostetaan taulukko
print(f"Kilpailu kesti {tunnit} tuntia.\n")
print(f"{'Rekisteri':<10} {'Huippunopeus':>13} {'Nopeus':>8} {'Matka':>8}")
print("-" * 42)
for auto in autot:
    print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:>9} km/h "
          f"{auto.nopeus:>4} km/h {auto.kuljettu_matka:>5} km")