# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.15.0

#PROJECT ON KAPREKAR CONSTANT FOR 4/5/6 DIGIT NUMBERS
#THE NUMBER SHOULD ATLEAST 2 DIGITS
#THE NUMBER SHOULD BE POSITIVE INTEGER
#THE NUMBER CAN HAVE ATMOST 6 DIGITS

#FOR 5/6 DIGITS IT WILL CHECK FOR FIRST 100 ITERATION
#FOR 5/6 DIGITS IT WILL GIVE YOU THE REPEATING NO

#BY HARSH THAKUR
#EMAIL : THAKURHARSH4111@GMAIL.COM

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

__version__ = '0.1'
__author__ = 'HARSH TAHKUR : thakurharsh4111@gmail.com'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(605, 367)
        MainWindow.setWindowTitle("KAPREKAR CALC")
        # data = ""
        # with open("Decorate.qss", 'r') as f:
        #     data = f.read()
        # MainWindow.setStyleSheet(data)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 311))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 311))

#----------------------------RADIO BUTTONS-----------------------------------------------------------

        self.radioButton_1 = QRadioButton("4 Digits")
        self.radioButton_1.setChecked(True)
        self.radioButton_2 = QRadioButton("5 Digits")
        self.radioButton_3 = QRadioButton("6 Digits")

        self.VAl = QLineEdit()


        self.VAl.setMaximumWidth(100)
        self.VAl.setMinimumHeight(10)

        self.vbox1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vbox1.setContentsMargins(0, 0, 0, 0)

        self.grid = QtWidgets.QGridLayout()

        self.grid.addWidget(self.VAl, 1, 0)
        self.grid.addWidget(self.radioButton_1, 2, 0)
        self.grid.addWidget(self.radioButton_2, 3, 0)
        self.grid.addWidget(self.radioButton_3, 4, 0)


        self.vbox1.addLayout(self.grid)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(319, 0, 281, 311))



        self.vbox2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vbox2.setContentsMargins(0, 0, 0, 0)

        self.OUTPUT_show=QLabel("")
        self.OUTPUT_show.setWordWrap(True)
        self.OUTPUT_show.setObjectName("OUTPUTBOX")

        self.OUTPUT_get=QPushButton("SUBMIT")
        self.OUTPUT_get.setCheckable(True)
        self.OUTPUT_get.clicked.connect(self.start)
        # self.OUTPUT_get.isCheckable()

        self.OUTPUT_get.setMaximumWidth(100)
        self.OUTPUT_get.setMinimumHeight(10)

        self.REFRESH = QPushButton("REFRESH")
        self.REFRESH.clicked.connect(self.reload)
        self.REFRESH.setMaximumWidth(100)
        self.REFRESH.setMinimumHeight(10)

        self.grid2 = QtWidgets.QGridLayout()


        self.grid2.addWidget(self.OUTPUT_show, 4, 0)
        self.grid2.addWidget(self.OUTPUT_get, 5, 0)
        self.grid2.addWidget(self.REFRESH, 6, 0)


        self.vbox2.addLayout(self.grid2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 24))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


# ----------------------------------------WORKING PART-------------------------------------------------

    def start(self):                                        #STARTING FUNCTION
        A=self.OUTPUT_get.isChecked()
        if A==True:
            # self.YUP=None
            self.deal_with_working()

    def deal_with_working(self):                         #RADIO BUTTONS OUTPUT
        if self.radioButton_1.isChecked():
            self.D=4
        if self.radioButton_2.isChecked():
            self.D=5
        if self.radioButton_3.isChecked():
            self.D=6
        self.get_digits_IN()

    def get_digits_IN(self):                              #VALIDATE INPUT
        try:
            No = None
            No = self.VAl.text()
            No = str(No)
            if len(No) > self.D or len(No) >= 7 or len(No) < 2:
                raise self.reload()
            No=int(No)
        except:
            self.showdialog()
        else:
            from CALC import work
            w=work()


            K=w.get_digits(No,self.D)                       #CALLING


            if K==None:
                self.OUTPUT_show.setText("NOT POSSIBLE IN 100 ITERATIONS")
                self.OUTPUT_show.setFont(QtGui.QFont('SansSerif', 20))
            else:
                self.OUTPUT_show.setText(K)
                self.OUTPUT_show.setFont(QtGui.QFont('SansSerif', 30))
                self.OUTPUT_get.setChecked(False)
                self.start()

    def showdialog(self):                                  #ERROR MESSAGEBOX
        self.VAl.setText("")
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)

        self.msg.setText("!!!ERROR!!!")
        self.msg.setMaximumWidth(200)

        self.msg.setInformativeText(" INPUT IS NOT ACCEPTABLE ")
        self.msg.setWindowTitle("OOPS!!!")

        self.msg.setDetailedText("1. Only Enter +ve Integer\n2. NO SHOULD BE OF 4 or 5 or 6 DIGITS\n3. Input Digits should not be more than Selected No. of Digits")

        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setDefaultButton(QMessageBox.Ok)
        # self.msg.buttonClicked.connect(self.reload)
        error=self.msg.exec_()
        self.reload()

    def reload(self):                                   #REFRESH BUTTON WORKING
        self.OUTPUT_get.setChecked(False)
        self.VAl.clear()
        self.OUTPUT_show.setText("")
        self.start()

if __name__ == "__main__":                                    #START OF PROGRAM
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
