import random
import time

print("""
****************************************

           Sayi Tahmin Oyunu
           -----------------
    
1 ile 40 arasinda bir sayi tahmin ediniz    


****************************************
""")


sayi = random.randint(1,40)
hak=7

while True:
    tahmin = int(input("Tahmininiz : "))

    if hak==0:
        print("Hakkiniz Bitti...")
        break
    if tahmin < sayi:
        print("Bilgiler Sorgulaniyor...")
        time.sleep(1)
        print("Daha buyuk bir sayi giriniz......")
        hak-=1
    elif tahmin > sayi:
        print("Bilgiler Sorgulaniyor...")
        time.sleep(1)
        print("Daha kucuk bir sayi giriniz...")
        hak-=1
    else :
        print("Bilgiler Sorgulaniyor",end=" . ")
        time.sleep(1)
        print(".",end=" ")
        time.sleep(1)
        print(".", end="\n")
        time.sleep(1)
        print("Tebrikler Dogru Tahmin Ettiniz")
        break

