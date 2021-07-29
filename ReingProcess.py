# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\Lib\TP323\Gui\ReingProcess.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog,QMessageBox
from TP323.Python import Acceuil
import pyautogui,subprocess,sys,os

class Ui_Form(QWidget):
    def Go_Acceuil(self):
        subprocess.Popen("python ./Acceuil.py",shell=True, stdout=sys.stdout)
        exit()
    def Shut_Down(self):
        QApplication.exit()
    def Take_ScrenShot(self):
        myScreenshot = pyautogui.screenshot()
        #patch = str(QFileDialog.getExistingDirectory(self,"Select Directory"))
        #Chemin = patch+"\\Capture.png"
        import  random
        var =random.randint(1,100)
        QMessageBox.information(self, "INFORMATION", "Votre Capture D'ecran à été Enregistré!!\n \n Veuillez la consultée ici : C:\Python\Lib\TP323\Capture ")
        name="..\\Capture\\"+"capt"+str(var)+".png"
        myScreenshot.save(name)
    def ReingProcess(self):
        self.pushButton_2.setStyleSheet("background-color: rgb(118, 118, 59);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.listWidget.clear()
        p = subprocess.Popen(["powershell.exe", 
              "Get-Process > ..\Txt\ProcessusEnCours.txt"], 
              stdout=sys.stdout)
        p.communicate()
        # Ouvrir le fichier en lecture seule
        file = open('..\Txt\ProcessusEnCours.txt', "r")
        lines = file.readlines()
        # fermez le fichier après avoir lu les lignes
        file.close()
        # Itérer sur les lignes
        for line in lines:
            #print(line.strip())
            self.listWidget.addItem(line.strip())          
# 
# 
# 
# 
# 
# 
# 
    def Mis_A_Jour(self):
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.pushButton.setStyleSheet("background-color: rgb(118, 118, 59);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.listWidget.clear()
        p = subprocess.Popen(["powershell.exe", 
              "Get-Hotfix >  ..\Txt\ListeMisAJour.txt"], 
              stdout=sys.stdout)
        p.communicate()
        # Ouvrir le fichier en lecture seule
        file = open("..\Txt\ListeMisAJour.txt", "r")
        lines = file.readlines()
        # fermez le fichier après avoir lu les lignes
        file.close()
        # Itérer sur les lignes
        for line in lines:
            #print(line.strip())
            self.listWidget.addItem(line.strip()) 
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1366, 768)
        Form.setMinimumSize(QtCore.QSize(1366, 768))
        Form.setMaximumSize(QtCore.QSize(1366, 768))
        Form.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(360, 300, 801, 391))
        self.listWidget.setMinimumSize(QtCore.QSize(500, 300))
        self.listWidget.setMaximumSize(QtCore.QSize(1366, 500))
        self.listWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(34, 34, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.Arreter = QtWidgets.QPushButton(Form)
        self.Arreter.setGeometry(QtCore.QRect(1160, 640, 201, 51))
        self.Arreter.setStyleSheet("background-color: rgb(104, 0, 0);\n"
"font: 12pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.Arreter.setObjectName("Arreter")
        self.Arreter.clicked.connect(self.Shut_Down)
        #
        #
        #
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(1160, 0, 211, 41))
        self.dateTimeEdit.setStyleSheet("font: 16pt \"Algerian\";\n"
"background-color: rgb(255, 255, 255);")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.Acceuil = QtWidgets.QPushButton(Form)
        self.Acceuil.setGeometry(QtCore.QRect(1160, 50, 201, 61))
        self.Acceuil.setStyleSheet("background-color: rgb(149, 67, 56);\n"
"font: 16pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.Acceuil.setObjectName("Acceuil")
        self.Acceuil.clicked.connect(self.Go_Acceuil)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1160, 240, 201, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(118, 118, 59);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.Take_ScrenShot)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 341, 51))
        self.pushButton.setStyleSheet("background-color: rgb(118, 118, 59);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ReingProcess)
        #
        #
        #
        #
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 390, 341, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(118, 118, 59);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Algerian\";\n"
"border:3px solid black;\n"
"border-radius:10px\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Mis_A_Jour)
        #
        #
        #
        #
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 1141, 291))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../image/modelisation-processus.jpg"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(920, 0, 241, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/modelisation-processus.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 1151, 61))
        self.label_2.setStyleSheet("background-color: rgb(157, 255, 180);\n"
"font: 58pt \"Algerian\";")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Arreter.setText(_translate("Form", "ARRETER"))
        self.Acceuil.setText(_translate("Form", "ACCEUIL"))
        self.pushButton_3.setText(_translate("Form", "CAPTURE D\'ECRAN"))
        self.pushButton.setText(_translate("Form", "PROCESSUS EN COURS D\'EXECUTION"))
        self.pushButton_2.setText(_translate("Form", "LES MIS A JOURS"))
        self.label_2.setText(_translate("Form", "REINGENIERIE  DES PROCESSUS"))



def main():
    app = QApplication(sys.argv)
    fen = QWidget()
    elt =Ui_Form()
    elt.setupUi(fen)
    fen.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()