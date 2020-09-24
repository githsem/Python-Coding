class Kareler():
    def __init__(self,max):
        self.max = max
        self.sayi = 1
    def __iter__(self):
        return(self)
    def __next__(self):
        if self.sayi < self.max:
            sonuc = self.sayi**2
            self.sayi +=1
            return sonuc
        else:
            self.sayi = 1
            raise StopIteration
kareal = Kareler(5)
iterator = iter(kareal)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
