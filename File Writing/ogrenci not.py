def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    print(liste)


with open("sinav.txt", "r", encoding ="UTf-8") as file:
   for i in file:
       not_hesapla(i)
