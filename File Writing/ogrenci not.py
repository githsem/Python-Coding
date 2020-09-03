def not_hesapla(satir):
    satir = satir[:-1]


with open("sinav.txt", "r", encoding ="UTf-8") as file:
   for i in file:
       not_hesapla(i)
