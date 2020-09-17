from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup


class Ui_Doviz(object):
    def setupUi(self, Doviz):
        Doviz.setObjectName("Doviz")
        Doviz.resize(512, 374)

        self.label = QtWidgets.QLabel(Doviz)
        self.label.setGeometry(QtCore.QRect(80, 20, 331, 31))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Doviz)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 291, 16))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Doviz)
        self.lineEdit.setGeometry(QtCore.QRect(310, 110, 121, 21))
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.label_3 = QtWidgets.QLabel(Doviz)
        self.label_3.setGeometry(QtCore.QRect(140, 220, 51, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Doviz)
        self.label_4.setGeometry(QtCore.QRect(270, 220, 61, 21))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Doviz)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 250, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Doviz)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 250, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Doviz)
        self.pushButton.setGeometry(QtCore.QRect(340, 140, 71, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Doviz)
        QtCore.QMetaObject.connectSlotsByName(Doviz)

        self.veri_cek()

    def retranslateUi(self, Doviz):
        _translate = QtCore.QCoreApplication.translate
        Doviz.setWindowTitle(_translate("Doviz", "Doviz"))
        self.label.setText(_translate("Doviz", "Doviz Programina Hosgeldiniz"))
        self.label_2.setText(_translate("Doviz", "Donusturmek Istediginiz TL Miktarini Giriniz :"))
        self.label_3.setText(_translate("Doviz", "EURO"))
        self.label_4.setText(_translate("Doviz", "DOLAR"))
        self.pushButton.setText(_translate("Doviz", "OK"))

        self.pushButton.clicked.connect(self.click)

    def click(self):
        miktar = int(self.lineEdit.text())
        euro = miktar*self.sonuceu
        dolar = miktar*self.sonucdo
        self.lineEdit_2.setText(str(euro))
        self.lineEdit_3.setText(str(dolar))

    def veri_cek(self):
        url = "https://www.doviz.com/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        isim = soup.find_all("span", {"class": "name"})
        kur = soup.find_all("span", {"class": "value"})
        for i, j in zip(isim, kur):
            i = i.text
            j = j.text
            if i == "DOLAR":
                sonucd = j
            if i == "EURO":
                sonuce = j

        self.sonucdo = float(sonucd.replace(",", "."))
        self.sonuceu = float(sonuce.replace(",", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Doviz = QtWidgets.QWidget()
    ui = Ui_Doviz()
    ui.setupUi(Doviz)

    Doviz.show()
    sys.exit(app.exec_())

