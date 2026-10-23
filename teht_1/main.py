class Auto:
    def __init__(self,rekisteritunnus , huippunopeus ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus=0
        self.matka=0

auto = Auto("ABC-123", 142,)
print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Nopeus:", auto.nopeus, "km/h")
print("Kuljettu matka:", auto.matka, "km")