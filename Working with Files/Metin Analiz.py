class Dosya():
    def __init__(self):
        self.kelime_sozluk = dict()
        with open("metin.txt","r",encoding = "utf-8") as file:
            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)

    def tum_kelimeler(self):
        kelimeler_kumesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        for i in kelimeler_kumesi:
            print(i)

    def kelime_frekansi(self):

        for i in self.sade_kelimeler:
            if i in self.kelime_sozluk:
                self.kelime_sozluk[i] +=1
            else:
                self.kelime_sozluk[i] = 1
       # for kelime,sayi in self.kelime_sozluk.items():
        #    print("{} ifadesi {} defa geciyor".format(kelime,sayi))

    def kelime_ara(self,kelime):
        self.kelime = kelime
        sayac = 0
        for i,j in self.kelime_sozluk.items():
            if i == self.kelime:
                print("{} kelimesi {} defa geciyor".format(i,j))
                sayac = -1
                break
            else:
                sayac +=1
        if sayac > 0:
            print("Boyle bir kelime bulunmamaktadir")


dosya = Dosya()
dosya.kelime_frekansi()
dosya.kelime_ara("olan")