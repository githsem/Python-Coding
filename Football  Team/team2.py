gs =[]
fb = []
bjk =[]
with open("liste.txt","r") as file:
    for i in file:
        i = i[:-1]
        kelime = i.split(",")
        if kelime[1]=="Galatasaray":
            gs.append(i+"\n")
        elif kelime[1]=="Fenerbahce":
            fb.append(i+"\n")
        elif kelime[1]=="Besiktas":
            bjk.append(i+"\n")

with open("gs1.txt","w") as file:
    file.writelines(gs)
with open("fb1.txt","w") as file:
    file.writelines(fb)
with open("bjk1.txt","w") as file:
    file.writelines(bjk)
