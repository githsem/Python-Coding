from Supermarkt import *

print("""
Supermarkt Programi

1. Urun Ekle

2. Urunleri Goster

3. Urun Adeti Ekle

4. Cikis
""")
supermarkt = Supermarkt()

while True:
    islem = input("Islem Seciniz :")

    if islem == "1":
        ad = input("Urun Adi : ")
        adet = input("Urun Adeti : ")
        yeni_urun = Urunler(ad,adet)
        supermarkt.urun_ekle(yeni_urun)
        print("Urun Eklendi")
    if islem == "2":
        supermarkt.goster()

    if islem =="3":
        ad = input("Urun Adi : ")
        adet = int(input("Eklemek Istediginiz Miktar : "))
        supermarkt.adet_ekle(ad,adet)
        print("Miktar Eklendi")

    if islem == "4":
        break