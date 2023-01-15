class Ertekel:

    def beker(self):
        ret = []
        input_ok = False
        ret.append(input("\tÉtel neve: "))
        ret.append(input("\tÉtel rendelőjének neve: "))
        ertekeles = int(input("\tÉrtékelés (1-5):"))
        ret.append(ertekeles)
        if ertekeles < 0:
            ret.append("Az értékelés nem lehet negatív!")
        elif ertekeles > 5:
            ret.append("5 pont feletti értékelés nem elfogadható!")
        elif ertekeles == 0:
            ret.append("Az értékelés csak 1 és 5 közötti egész szám lehet!")
        else:
            ret.append("Köszönjük az értékelést!")
        return ret
