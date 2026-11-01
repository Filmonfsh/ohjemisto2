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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


# Pääohjelma
sähköauto = Sähköauto("ABC-15", 180, 52.5)
bensa_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(120)
bensa_auto.kiihdytä(100)

sähköauto.kulje(3)
bensa_auto.kulje(3)

print(f"{sähköauto.rekisteritunnus} (akku {sähköauto.akkukapasiteetti} kWh): "
      f"matkamittari {sähköauto.kuljettu_matka} km")
print(f"{bensa_auto.rekisteritunnus} (tankki {bensa_auto.tankin_koko} l): "
      f"matkamittari {bensa_auto.kuljettu_matka} km")