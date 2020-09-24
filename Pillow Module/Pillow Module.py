from PIL import Image,ImageFilter

image = Image.open("kus.jpg")
image.save("kus2.jpg")
image.rotate(90).save("kus3.jpg")
degistir = (500,400)
image.thumbnail(degistir)
image.save("kus4.jpg")
image.filter(ImageFilter.GaussianBlur(10)).save("kuş5.jpg")
kirp = (50,30,440,350)
image.crop(kirp).save("kus6.jpg")