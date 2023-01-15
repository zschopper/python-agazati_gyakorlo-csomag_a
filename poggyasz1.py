class Poggyasz:
    def __init__(self, lista) -> None:
        self.szelesseg = int(lista[0])
        self.magassag = int(lista[1])
        self.melyseg = int(lista[2])
        self.suly = int(lista[3])

class Poggyasz1:
    def __init__(self, fajlnev) -> None:
        self.lista = []
        fh = open(fajlnev, "r", encoding="utf-8")
        sor = fh.readline()

        while sor:
            sor = fh.readline()
            if sor:
                self.lista.append(Poggyasz(sor.strip().split("#")))

    def darab(self):
        return len(self.lista)

    def atlagsuly(self, szelesseg):
        i = 0
        ossz = 0
        db = 0
        while i < len(self.lista):
            if self.lista[i].szelesseg == szelesseg:
                ossz += self.lista[i].suly
                db += 1
            i += 1

        if db:
            return ossz * 1000 // db
        return 0

    def legmagasabb(self):
        i = 0
        idx = 0
        while i < len(self.lista):
            if self.lista[i].magassag > self.lista[idx].magassag:
                idx = i
            i += 1
        return self.lista[idx]
