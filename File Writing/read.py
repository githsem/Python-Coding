file = open("bilgi.txt","r",encoding="UTF-8")

for i in file:
    print(i,end="")
file.close()
print("**********************************")
file = open("bilgi.txt","r",encoding="UTF-8")
icerik = file.read()
print(icerik)
file.close()

file = open("bilgi.txt","r",encoding="UTF-8")
liste = file.readlines()
print(liste)
file.close()
