import ertekel
import sorozat
import poggyasz1

print("I/A, B")

ert = ertekel.Ertekel().beker()

print("I/C")

print("\t" + ert[3])

print("II/A, B, C:")

s = sorozat.Sorozat()
veletlenek = s.veletlenek()
print(f"\t{veletlenek}")

print("II/D, E:")

psz = s.paratlanok_szama()
print(f"\tA páratlanok száma: {psz}.")
s.paratlanok_szama_ment("kimutatas.txt")

print("III/A, B:")

p = poggyasz1.Poggyasz1("csomag.txt")
db = p.darab()
print(f"\tA poggyászok száma: {db}")

print("III/C:")

szelesseg = 51
atlagsuly = p.atlagsuly(szelesseg)
print(f"\tAz {szelesseg} cm-es poggyászok átlag súlyértéke: {atlagsuly} g")

print("III/D:")

legm = p.legmagasabb()
print(f"\tA legmagasabb poggyász méretei: {legm.szelesseg}x{legm.magassag}x{legm.melyseg}, súlya {legm.suly} kg.")
