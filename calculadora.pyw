__author__ = "Rodrigo Zambianco Cataroço"
__version__ = "0.1α"

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic
import math

# >>>>>>>> Para mostrar os dias da semana em pt-br
import locale 
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
# <<<<<<<<<

class Calculadora(QtWidgets.QMainWindow):
    """Calcula o peso teórico de um cilindro, dado seu diametro, altura e densidade do material"""
    def about(self):
        """Texto de informação"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Sobre")
        msg.setText('Calculadora para peso teórico de cilidros<br>versão 0.1α<br> <a href="https://github.com/Zambianco/pesoteorico">github</a>')
        msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        msg.exec_() 


    def calcular_peso_cilindro(self):
        diametro = int(self.lineEdit_diametro.text()) / 100
        altura = int(self.lineEdit_altura.text()) / 100
        densidade = float(self.lineEdit_densidade.text().replace(",", "."))
        peso = (math.pi * math.pow(diametro/2,2) * altura) * densidade
        peso_str = '{:.2f} Kg'.format(peso).replace(".", ",")
        self.label_peso.setText(peso_str)
    

    def __init__(self):
        super().__init__()
        uic.loadUi("cilindro.ui", self)
        self.pushButton_calcular.clicked.connect(self.calcular_peso_cilindro)
        self.actionSobre.triggered.connect(self.about)


app = QtWidgets.QApplication(sys.argv)
inicio = Calculadora()
inicio.show() #FullScreen()  ##inicia o aplicativo no modo 'fullscreen'
app.exec_()
