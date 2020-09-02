def tek_cift(sayi):
    if sayi%2==0:
        return sayi
    else:
        raise ValueError("Tek Sayi Hatasi")

liste =[1,2,3,4,5,6,7,8,9,10]

for i in liste:
    try:
        print(tek_cift(i))
    except:
        print("Tek Sayi")