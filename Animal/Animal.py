class Hayvan():
    def __init__(self,ad,ayak_sayisi):
        self.ad = ad
        self.ayak_sayisi = ayak_sayisi

class Kopek(Hayvan):
    def __init__(self,ad,ayak_sayisi,renk):
        super().__init__(ad,ayak_sayisi)
        self.renk = renk
    def havla(self,sayi):
        self.sayi = sayi
        print("{} {}  kere havladi".format(self.ad,self.sayi))

class Kus(Hayvan):
    def __init__(self,ad,ayak_sayisi,kanat):
        super().__init__(ad, ayak_sayisi)
        self.kanat = kanat
    def uc(self):
        print("{} ucuyor...".format(self.ad))

class At(Hayvan):
    def __init__(self,ad,ayak_sayisi,cins):
        super().__init__(ad, ayak_sayisi)
        self.cins = cins
    def kisne(self):
        print("{} kisniyor...".format(self.ad))

kopek = Kopek("Karabas",4,"Beyaz")
kopek.havla(3)

