with open("sinav_sonuc.txt", "r", encoding ="UTf-8") as file:
    for i in file:
        isim = i
        i = i[-3:-1]
        if (i == "FD") or (i == "FF"):
            with open("kalanlar.txt", "a", encoding="UTf-8") as file1:
                file1.write(isim)
        else:
            with open("gecenler.txt", "a", encoding="UTf-8") as file2:
                file2.write(isim)


