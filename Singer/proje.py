from Singer import *

print("""
***************************************************

        Sarkici Programına Hoşgeldiniz

İşlemler;

1. Sarki Ekle

2. Sarki Sil 

3. Sure Hesapla

Çıkmak için 'q' ya basın.
***************************************************""")
sarkilar = Sarkilar()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem == "1"):
        isim = input("İsim:")
        sanatci = input("Sanatci:")
        album = input("Album:")
        sirket = input("Sirket:")
        sure = int(input("Sure:"))

        yeni_sarki = Sarki(isim, sanatci, album, sirket, sure)

        print("Sarki ekleniyor....")
        time.sleep(2)

        sarkilar.sarki_ekle(yeni_sarki)
        print("Sarki Eklendi....")

