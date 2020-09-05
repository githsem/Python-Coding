with open("siir.txt","r",encoding="utf-8") as file:
    string = ""
    for i in file:
        string +=i[0]
    print(string)
