def extra(func):
    def wrapper(sayilar):
        tek_sayi = 0
        tek_sayilar = 0
        cift_sayi = 0
        cift_sayilar = 0
        for sayi in sayilar:
            if sayi%2==0:
                cift_sayi += 1
                cift_sayilar +=sayi
            else:
                tek_sayi += 1
                tek_sayilar += sayi
        print("Tek sayilar ortalamasi : ",tek_sayilar/tek_sayi)
        print("Cift sayilar ortalamasi : ",cift_sayilar/cift_sayi)
        func(sayilar)
    return wrapper




def ortalama_hesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    print("Sayilarin ortalamasi : ",toplam/len(sayilar))

ortalama_hesapla([1,2,3,4,5,6,7,8,9,10])