import sys

from PyQt5 import QtWidgets

def pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 2")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Burasi bir yazidir")
    etiket.move(160,30)


    pencere.setGeometry(500,200,400,400)
    pencere.show()
    sys.exit(app.exec_())

pencere()