import sqlite3

import time

class Sarki():

    def __init__(self,isim,sanatci,album,sirket,sure):

        self.isim = isim
        self.sanatci = sanatci
        self.album = album
        self.sirket = sirket
        self.sure = sure

    def __str__(self):

        return "Sarki İsmi: {}\nSanatci: {}\nAlbum: {}\nProduksiyon Sirketi: {}\nsure: {}\n".format(self.isim,self.sanatci,self.album,self.sirket,self.sure)


class Sarkilar():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarkilar.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists sarkilar (isim TEXT,sanatci TEXT,album TEXT,sirket TEXT,sure INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarki_ekle(self, sarki):
        sorgu = "Insert into sarkilar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu, (sarki.isim, sarki.sanatci, sarki.album, sarki.sirket, sarki.sure))

        self.baglanti.commit()

    def sarki_sil(self, isim):
        sorgu = "Delete From sarkilar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        self.baglanti.commit()

    def sure_hesapla(self):

        sorgu = "Select * From sarkilar"

        self.cursor.execute(sorgu)

        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Böyle bir sarki bulunmuyor...")
        else:
            sure=0
            for i in sarkilar:
                sure += sarkilar[0][4]
        print("Toplam Sure : ",sure)
