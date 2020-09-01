class Computer():
    def __init__(self,marka,islemci,hafiza):
        self.marka = marka
        self.islemci = islemci
        self.hafiza = hafiza

    def hafiza_arttir(self,miktar):
        self.hafiza += miktar
        print("Hafiza Arttirildi...")

    def __str__(self):
        return "Marka : {}\nIslemci : {},Hafiza : {}".format(self.marka,self.islemci,self.hafiza)

computer = Computer("Asus","i7",1000)

print("""
        Computer

1. Ozellikleri

2. Hafiza Artir

3. Cikis        
""")
while True:

    islem = input("Isleminizi Seciniz : ")

    if (islem == "1"):
        print(computer)

    elif (islem == "2")
        miktar = int(input("Arttirmak istediginiz miktari giriniz : "))
        computer.hafiza_arttir(miktar)

    elif (islem == "3")
        print("Cikiliyor...")
        break

    else
