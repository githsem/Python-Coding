liste = []
with open("liste.txt","r") as file:
    for i in file:
        kelime = i.split(",")
        liste.append(kelime)
    for x in range(0,len(liste)):
        if liste[x][1]=="Galatasaray\n":
            a=liste[x][0]+" " + liste[x][1]
            with open("gs.txt", "a") as file1:
                file1.write(a)
        elif liste[x][1]=="Fenerbahce\n":
            a=liste[x][0]+" " + liste[x][1]
            with open("fb.txt", "a") as file2:
                file2.write(a)
        if liste[x][1]=="Besiktas\n":
            a=liste[x][0]+" " + liste[x][1]
            with open("bjk.txt", "a") as file2:
                file2.write(a)