import sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyeler (kullanici_adi TEXT,parola TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giris")
        self.yazi_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanici Girisi")
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("SELECT * FROM uyeler WHERE kullanici_adi = ? and parola = ?", (adi, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Boyle bir kullanici yok\nLutfen tekrar deneyiniz...")
        else:
            self.yazi_alani.setText("Hos Geldiniz  " + adi)


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
