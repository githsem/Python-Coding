def asal():
    for sayi in range(2,1000):
        sayac = 0
        for i in range(2,sayi):
            if sayi%i == 0:
                sayac += 1
        if sayac==0:
            yield sayi

for sayi in asal():
    print(sayi)