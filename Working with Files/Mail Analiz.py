with open("mail.txt","r",encoding="utf-8") as file:
    for i in file:
        i = i.strip("\n")

    for i in liste:
        if i.endswith(".com") and ("@" in i):
            if "@" in i:
                print("gecerli")
            else :
                print("gecersiz")
        else:
            print("gecersiz")
