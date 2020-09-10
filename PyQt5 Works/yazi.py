import sys

from PyQt5 import QtWidgets,QtGui

def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 2")
    etiket = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("logo.png"))
    etiket2.move(40,70)


    etiket.setText("Burasi bir yazidir")
    etiket.move(160,30)


    pencere.setGeometry(500,200,400,400)
    pencere.show()
    sys.exit(app.exec_())

pencere()