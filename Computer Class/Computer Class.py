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
    