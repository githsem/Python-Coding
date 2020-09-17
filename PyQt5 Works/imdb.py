import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 370)
        Form.setWindowOpacity(4.0)
        Form.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 110, 101, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 110, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 170, 411, 171))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.veri_cek)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "IMDB"))
        self.label.setText(_translate("Form", "IMDB PROGRAMINA HOSGELDINIZ"))
        self.label_2.setText(_translate("Form", "Rating Giriniz : "))
        self.pushButton.setText(_translate("Form", "Goster"))

    def veri_cek(self):
        url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")

        basliklar = soup.find_all("td", {"class": "titleColumn"})
        ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})
        sayi = float(self.lineEdit.text())
        
        for baslik, rating in zip(basliklar, ratingler):
            baslik = baslik.text
            rating = rating.text

            baslik = baslik.strip()
            baslik = baslik.replace("\n", "")
            baslik = baslik.strip("0123456789. ")

            rating = rating.strip()
            rating = rating.replace("\n", "")
            if float(rating) > sayi:
                ekle = baslik + "   "+rating
                self.textEdit.append(ekle)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
