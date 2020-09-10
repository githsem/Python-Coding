import sys

from PyQt5 import QtWidgets,QtGui

def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 2")

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Buton")

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dunya")
    etiket.move(160,30)
    buton.move(160,50)


    pencere.setGeometry(500,200,400,400)
    pencere.show()
    sys.exit(app.exec_())

pencere()