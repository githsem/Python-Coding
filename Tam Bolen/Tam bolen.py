def tam_bolen(sayi):
    for i  in range(2,sayi+1):
        if sayi % i == 0:
            print(i,end=" ")

sayi = int(input("Sayi : "))
tam_bolen(sayi)