string = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

harfler = list(string)
harf_sozluk = dict()

for i in harfler:
    if i in harf_sozluk:
        harf_sozluk[i] += 1
    else:
        harf_sozluk[i] = 1
for i,j in harf_sozluk.items():
    print("{} herfi {} defa gecmektedir".format(i,j))
