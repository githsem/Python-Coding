def extra(func):
    def wrapper(sayi):
        mukemmel = 0;
        for i in range(1,sayi):
            if sayi%i == 0:
                mukemmel += i
        if sayi == mukemmel:
            print("Mukemmel : ",sayi)
        func(sayi)
    return wrapper

@extra
def asal(sayi):
    bolen = 0
    for i in range(2,sayi):
        if sayi%i == 0:
            bolen +=1
    if bolen == 0:
        print("Asal : ",sayi)

for i in range(2,1000):
    asal(i)