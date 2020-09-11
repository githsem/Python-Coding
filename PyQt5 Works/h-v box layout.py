import sys

from PyQt5 import QtWidgets, QtGui


def pencere():
    app = QtWidgets.QApplication(sys.argv)

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("Iptal")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)
   
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Ders 2")
    pencere.setLayout(v_box)



    pencere.setGeometry(500, 200, 400, 400)
    pencere.show()
    sys.exit(app.exec_())


pencere()
