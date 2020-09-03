with open("bilgi.txt","r",encoding ="UTf-8") as file:
    for i in file:
        print(i)

with open("bilgi.txt","r",encoding ="UTf-8") as file:
    print(file.tell())
    file.seek(12)
    print(file.tell())

with open("bilgi.txt","r",encoding ="UTf-8") as file:
    file.seek(2)
    print(file.read(5))

with open("bilgi.txt","r+",encoding ="UTf-8") as file:
    file.seek(5)
    file.write("degistirildi")

with open("bilgi.txt","r",encoding ="UTf-8") as file:
    print(file.read())
