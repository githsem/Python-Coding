liste = ["123","wer","23we","344","ss"]

for i in range(0,5):
    try:
        if liste[i] != int(liste[i]):
            print(liste[i])
    except:
        pass

