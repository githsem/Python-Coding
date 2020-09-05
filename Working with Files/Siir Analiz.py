with open("siir.txt","r",encoding="utf-8") as file:
    satir = file.readlines()
    string = ""
    for i in satir:
        string +=i[0]
    print(string)
