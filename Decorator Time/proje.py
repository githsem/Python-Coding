



def asal(sayi):
    bolen = 0
    for i in range(2,sayi):
        if sayi%i == 0:
            bolen +=1
    if bolen == 0:
        print(sayi)

for i in range(2,1000):
    asal(i)