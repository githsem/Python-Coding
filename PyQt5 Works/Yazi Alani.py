import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
