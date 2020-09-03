with open("bilgi.txt","r",encoding ="UTf-8") as file:
    for i in file:
        print(i)

with open("bilgi.txt","r",encoding ="UTf-8") as file:
    print(file.tell())
    file.seek(12)
    print(file.tell())