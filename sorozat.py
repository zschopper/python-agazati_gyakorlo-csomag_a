import random

class Sorozat:

    def __init__(self):
        self.lista = []

    def veletlenek(self):
        self.lista = []
        while len(self.lista) < 12:
            self.lista.append(int(random.random() * 1011) - 10)
        # print("$".join(map(str, lista)))
        i = 1
        szoveg = str(self.lista[0])
        while i < len(self.lista):
            szoveg += "$" + str(self.lista[i])
            i += 1
        return szoveg

    def paratlanok_szama(self):
        i = 0
        db = 0
        while i < len(self.lista):
            if i % 2:
                db += 1
            i += 1
        return db

    def paratlanok_szama_ment(self, fajlnev):
        psz = self.paratlanok_szama()
        fh = open(fajlnev, "w", encoding="utf-8")
        fh.write(f"II/F:\r\n\tA páratlanok száma: {psz}.")
        fh.close()
