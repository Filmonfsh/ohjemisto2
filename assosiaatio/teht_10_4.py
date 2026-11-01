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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<10} {'Huippunopeus':>13} {'Nopeus':>9} {'Matka':>9}")
        print("-" * 44)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:>8} km/h "
                  f"{auto.nopeus:>4} km/h {auto.kuljettu_matka:>6} km")
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False


# Pääohjelma
autot = []
for i in range(1, 11):
    rekisteri = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while True:
    kilpailu.tunti_kuluu()
    tunnit = tunnit + 1
    if kilpailu.kilpailu_ohi():
        break
    if tunnit % 10 == 0:
        print(f"{kilpailu.nimi}: tilanne {tunnit} tunnin jälkeen")
        kilpailu.tulosta_tilanne()

print(f"{kilpailu.nimi} päättyi {tunnit} tunnin jälkeen!")
kilpailu.tulosta_tilanne()
