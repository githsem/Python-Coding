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
        for i in self.sade_kelimeler(
            kelimeler_kumesi.add(i)
        for i in     


dosya = Dosya()