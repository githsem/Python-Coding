print("""
******************
Asal Sayi Programi
******************
""")

def asal(sayi):
    bolen = 0
    for i in range(2,sayi):
        if sayi%i == 0:
            bolen +=1
    if bolen == 0:
        print("{} sayisi asal bir sayidir".format(sayi))
    else :
        print("{} sayisi asal bir sayi degildir".format(sayi))

while True:
    print("Cikmak icin q'ya basiniz ")
    sayi = input("Sayi Giriniz : ")

    if int(sayi)<=0:
        print("Pozitif bir sayi giriniz...")
    elif sayi == "q":
        break
    else:
        sayi = int(sayi)
        asal(sayi)
    print("-------------------------")