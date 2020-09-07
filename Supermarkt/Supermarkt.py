import sqlite3

class Urunler():
    def __init__(self,ad,adet):
        self.ad = ad
        self.adet= adet

class Supermarkt():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("supermarkt.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS supermarkt(ad TEXT,adet INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def goster(self):
        sorgu = "SELECT * FROM supermarkt"
        self.cursor.execute(sorgu)
        veriler = self.cursor.fetchall()

        for i in veriler:
            urunler = Urunler(i[0],i[1])
            print("Urun Adi : {}\nUrun Adeti : {}".format(urunler.ad,urunler.adet))

    def urun_ekle(self,yeni_urun):
        sorgu = "INSERT INTO supermarkt VALUES(?,?)"
        self.cursor.execute(sorgu,(yeni_urun.ad,yeni_urun.adet))
        self.baglanti.commit()

    def adet_ekle(self,ad,adet):
        sorgu = "SELECT * FROM supermarkt WHERE ad = ?"
        self.cursor.execute(sorgu,(ad,))
        urun = self.cursor.fetchall()
        miktar = urun[0][1]
        adet += miktar
        sorgu = "UPDATE supermarkt SET adet = ? WHERE ad = ? "
        self.cursor.execute(sorgu,(adet,ad))
        self.baglanti.commit()
