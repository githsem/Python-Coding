with open("mail.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i.strip("\n")
        if i.endswith(".com") and ("@" in i):
            print(i)
