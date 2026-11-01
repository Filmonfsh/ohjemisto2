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
auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print("Nopeus:", auto.nopeus, "km/h")

auto.kiihdytä(-200)
print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")

###########
auto.kuljettu_matka = 2000
auto.kiihdytä(60)
auto.kulje(1.5)
print("Kuljettu matka:", auto.kuljettu_matka, "km")