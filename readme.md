# Ágazati vizsga gyakorló  Python - 2023

A feladatokat külön modulokban oldja meg, a modulok nevei a feladatokban találhatók!  
A főprogramból (main.py) hívja meg az egyes modulok metódusait a feladatban meghatározott neveikkel (1p)!  
A projektet agazati_2023_a néven mentse, majd a munkáját sajat_nev.zip (Pl.: Nagy_Virag.zip) nevű állományban adja le! (1p)  

## 1. feladat

Összesen 7p szerezhető, a modul neve: **ertekel.py**

**minta:**

```
I/A, B
    Étel neve: Ananászos pizza 
    Étel rendelőjének neve: Kiss Előd
    Értékelés (1-5): 4

I/C
    Köszönjük az értékelést! 
```

A. Kérje be az alábbi adatokat a fenti mintának megfelelően:  
    étel neve, étel rendelőjének neve és értékelés!  (2p)  
B. A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ([1,5], zárt intervallum értendő):  
Amennyiben negatív számot adott meg:  
“Az értékelés nem lehet negatív!”,  
Amennyiben 5 feletti egész számot adott meg:  
“5 pont feletti értékelés nem elfogadható!”  
Helyes pont-adat esetén:  
“Köszönjük az értékelést!”  
Feltételezzük, hogy csak egész számokat adnak meg. (4p)  
C. A **mintának megfelelően** írassa ki az eredményt! (1p)  
 
## 2. feladat

Összesen 14p szerezhető, a modul neve: **sorozat.py**

**minta:** 
```
II/A, B, C:
    20$28$124$166$15$188$174$243$221$22$945$841
II/D, E:
    A páratlanok száma: 5.
```

kimutatas.txt tartalma:
```
II/F:
    A páratlanok száma: 5. 
```

A. Írasson ki a konzolra **dollár jellel** (\$) elválasztva **12** számból álló **véletlen** számsorozatot [-10,1000] **zárt** intervallumon a mintának megfelelően! (4p)  
B. A generált értékeket tárolja **lista** adatszerkezetben! (1p)  
C. A \$ jel **csak az értékek között** szerepeljen (a végén, elején ne)! (2p)  
D. Írjon függvényt **paratlanok_szama** néven, amiben számolja meg, hogy hány olyan elem van, ami **páratlanok**. A **visszatérési érték** legyen egy egész szám! (3p)  
E. A paratlanok_szama függvény **eredményét** írassa ki a mintának megfelelően a konzolra, amit **konzol_kiir** nevű metódusban fogalmazzon meg! (2p)  
F. A paratlanok_szama függvény **eredményét** írassa ki a mintának megfelelően a **eredmeny.txt** nevű fájlba, amit **fajlba_kiir** nevű metódusban fogalmazzon meg! (2p)  
 
## 3. feladat

Összesen 17p szerezhető, a modul neve: **poggyasz1.py**

A csomag.txt forrásállomány, csomagok méret adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A csomag.txt állomány szerkezete:

* a (szélesség cm): pl: 51
* b (magasság cm): pl.: 33
* c (mélység cm): pl.: 24
* m (súly kg-ban megadva): pl.: 10

Az állomány első sora a mezőneveket tartalmazza kettőskereszttel elválasztva.

A megoldás mintája:
```
III/A, B:
            	A poggyászok száma: 101
III/C:
            	Az 51 cm-es poggyászok átlag súlyértéke: 7375 g
III/D:
            	A legmagasabb poggyász méretei: 47x46x16, súlya: 4 kg.
```
A.	Olvassa be **osztály** segítségével (utóbbit hozza létre **külön modulban**) a csomag.txt fájlból a poggyászok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)  
B.	Írassa ki a **poggyászok számát** a mintának megfelelően a konzolra! (2p)  
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy mennyi az 51 cm széles poggyászok **átlag súlya** gramban. (1kg = 1000g) (4p)  
D.	Írassa ki konzolra a mintának megfelelően a **legmagasabb poggyász méreteit és súlyát** (ha több is van, akkor az első legmagasabb adatait).(4p)  

 
Pontozó táblázat:

|Feladat|Maximum pontszám|Diák pontja
|---------|-------:|---------:|
|Megfelelő projekt és modul elnevezések. **ertekel.py, sorozat.py, poggyasz1.py**|1|
|**Első feladat**|
|Kérje be az alábbi adatokat a fenti mintának megfelelően:<br>étel neve, étel rendelőjének neve és értékelés!|2|
|A program az adatbekérés után írja ki, ha a pontozás nem a megfelelő határokon belül lett megadva (**zárt intervallum** értendő):|1|
|Amennyiben negatív számot adott meg:<br>“A értékelés nem lehet negatív!”,|1|
|Amennyiben 5 feletti egész számot adott meg:<br>“5 pont feletti értékelés nem elfogadható!”|1|
|Helyes pont-adat esetén:<br>“Köszönjük az értékelést!”|1|
|A **mintának megfelelően** írassa ki az eredményt!|1|
|**Második feladat**|
|Írasson ki a konzolra **dollárjelel(\$)** elválasztva|1|
|**12** számból álló|1|
|véletlen számsorozatot [-10,1000] **zárt** intervallumon a mintának megfelelően!|2|
|A generált értékeket tárolja **lista** adatszerkezetben!|1|
|A \$ jel **csak az értékek között** szerepeljen (a végén, elején ne)!|2|
|Írjon függvényt **paratlanok_szama** néven,|1|
|amiben számolja meg, hogy hány olyan elem van, ami **páratlan**.|1|
|A **visszatérési érték** legyen egy egész szám!|1|
|A paratlanok_szama függvény **eredményét** írassa ki a mintának megfelelően a konzolra, amit **konzol_kiir** nevű metódusban fogalmazzon meg!|2|
|A paratlanok_szama függvény **eredményét** írassa ki a mintának megfelelően|1|
|a eredmeny**.txt** nevű fájlba, amit **fajlba_kiir** nevű metódusban fogalmazzon meg!|1|
|**Harmadik feladat**|
|Osztályt hozott létre a minta fájl alapján megfelelő adattagokkal.|2|
|**Tárolja el** összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását!  
|(soronként beolvasás(1p), sorvégi adattisztítása(1p), objektumok létrehozása(1p), objektumok listában tárolása(1p), meg van az összes adatsor(1p))|4|
|Ügyeljen arra, hogy az állomány első sora az adatok **fejléc**ét tartalmazza!|1|
|Írassa ki a poggyászok számát|1|
|a mintának megfelelően a konzolra!|1|
|Határozza meg és írassa ki a konzolra a minta szerint,|1|
|hogy mennyi az 51 cm széles poggyászok|1|
|**átlag súlya**|1|
|**grammban.**|1|
|Írassa ki konzolra a mintának megfelelően a|1|
|**legmagasabb poggyász méreteit és magasságát** (ha több is van, akkor az első legmagasabb adatait).|2|
|A méreteket a megfelelő sorrendben x -el elválasztva írta ki (4p)|1|
|**Összesen:**|40|

