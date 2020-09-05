class Dosya():
    def __init__(self):
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
        self.kelime_sozluk = dict()

        for i in self.sade_kelimeler:
            if i in self.kelime_sozluk:
                self.kelime_sozluk[i] +=1
            else:
                self.kelime_sozluk[i] = 1
        for kelime,sayi in kelime_sozluk.items():
            print("{} ifadesi {} defa geciyor".format(kelime,sayi))

    def kelime_ara(self,kelime):
        self.kelime = kelime
        for i in self.kelime_sozluk.items():
            if i = self.kelime:
                print("{} kelimesi {} defa geciyor")
            else:
                print("Boyle bir kelime bulunmamaktadir")

dosya = Dosya()
dosya.kelime_ara()