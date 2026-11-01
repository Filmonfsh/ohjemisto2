class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde):
        if kohde < self.alin or kohde > self.ylin:
            print(f"Kerrosta {kohde} ei ole.")
            return
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissin_numero, kohde):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Hissiä {hissin_numero} ei ole.")
            return
        print(f"Hissi {hissin_numero} liikkuu kerrokseen {kohde}:")
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohde)


# Pääohjelma
talo = Talo(1, 6, 3)

talo.aja_hissiä(1, 4)
talo.aja_hissiä(2, 6)
talo.aja_hissiä(1, 2)
talo.aja_hissiä(3, 3)
talo.aja_hissiä(5, 2)