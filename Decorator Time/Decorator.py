
def ortalama_hesapla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    print("Sayilarin ortalamasi : ",toplam/len(sayilar))

ortalama_hesapla([1,2,3,4,5,6,7,8,9,10])