class Hayvan():
    def __init__(self,ad,ayak_sayisi):
        self.ad = ad
        self.ayak_sayisi = ayak_sayisi
    def bilgiler(self):
        print("Ad : {}\nAyak : {}".format(self.ad,self.ayak_sayisi))

class Kopek(Hayvan):
    def __init__(self,ad,ayak_sayisi,renk):
        super().__init__(ad,ayak_sayisi)
        self.renk = renk
    def havla(self,sayi):
        self.sayi = sayi
        print("{} {}  kere havladi".format(self.ad,self.sayi))
    def bilgiler(self):
        print("Ad : {}\nAyak : {}\nRenk : {}".format(self.ad,self.ayak_sayisi,self.renk))

class Kus(Hayvan):
    def __init__(self,ad,ayak_sayisi,kanat):
        super().__init__(ad, ayak_sayisi)
        self.kanat = kanat
    def uc(self):
        print("{} ucuyor...".format(self.ad))
    def bilgiler(self):
        print("Ad : {}\nAyak : {}\nKanat : {}".format(self.ad,self.ayak_sayisi,self.kanat))

class At(Hayvan):
    def __init__(self,ad,ayak_sayisi,cins):
        super().__init__(ad, ayak_sayisi)
        self.cins = cins
    def kisne(self):
        print("{} kisniyor...".format(self.ad))
    def bilgiler(self):
        print("Ad : {}\nAyak : {}\nCins : {}".format(self.ad,self.ayak_sayisi,self.cins))

class Tay(At):
    def __init__(self, ad, ayak_sayisi, cins):
        super().__init__(ad, ayak_sayisi,cins)


kopek = Kopek("Karabas",4,"Beyaz")
kopek.havla(3)

kus = Kus("Serce",2,2)
kus.uc()

at = At("Tom",4,"Ingiliz")
at.kisne()

kopek.bilgiler()
kus.bilgiler()
at.bilgiler()
tay =Tay("Jo",4,"Arap")
tay.bilgiler()

