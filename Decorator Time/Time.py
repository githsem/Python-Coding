import time
def zaman_hesapla(func):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = func()
        bitis = time.time()
        print(func.__name__+ " " + str(bitis-baslama) + "saniye surdu")



def kare_hesapla(sayilar):
    sonuc =[]
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc
def kup_hesapla(sayilar):
    sonuc =[]
    for i in sayilar:
        sonuc.append(i**3)
    return sonuc

kare_hesapla(range(100))
