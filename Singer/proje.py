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
    islem = input("Yapacağınız İşlem:")

    if (islem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (islem == "1"):
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
    elif (islem == "2"):
        isim = input("Hangi sarkiyi silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Sarki Siliniyor...")
            time.sleep(2)
            sarkilar.sarki_sil(isim)
            print("Sarki silindi....")
    elif(islem == "3"):
        sarkilar.sure_hesapla()



