# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '24_Masaustu_Uygulamasi_PyQt5/_radioButtonForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblUlke = QtWidgets.QLabel(self.centralwidget)
        self.lblUlke.setGeometry(QtCore.QRect(80, 190, 121, 51))
        self.lblUlke.setText("")
        self.lblUlke.setObjectName("lblUlke")
        self.lblEgitim = QtWidgets.QLabel(self.centralwidget)
        self.lblEgitim.setGeometry(QtCore.QRect(320, 190, 121, 51))
        self.lblEgitim.setText("")
        self.lblEgitim.setObjectName("lblEgitim")
        self.btnUlke = QtWidgets.QPushButton(self.centralwidget)
        self.btnUlke.setGeometry(QtCore.QRect(80, 280, 141, 41))
        self.btnUlke.setObjectName("btnUlke")
        self.btnEgitim = QtWidgets.QPushButton(self.centralwidget)
        self.btnEgitim.setGeometry(QtCore.QRect(310, 280, 141, 41))
        self.btnEgitim.setObjectName("btnEgitim")
        self.groupBoxUlke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUlke.setGeometry(QtCore.QRect(50, 10, 191, 181))
        self.groupBoxUlke.setObjectName("groupBoxUlke")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxUlke)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 141, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridUlke = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridUlke.setContentsMargins(0, 0, 0, 0)
        self.gridUlke.setObjectName("gridUlke")
        self.radioTurkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioTurkiye.setObjectName("radioTurkiye")
        self.gridUlke.addWidget(self.radioTurkiye, 0, 0, 1, 1)
        self.radioAzerbeycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAzerbeycan.setObjectName("radioAzerbeycan")
        self.gridUlke.addWidget(self.radioAzerbeycan, 1, 0, 1, 1)
        self.radioAlmanya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAlmanya.setObjectName("radioAlmanya")
        self.gridUlke.addWidget(self.radioAlmanya, 2, 0, 1, 1)
        self.radioYunanistan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioYunanistan.setObjectName("radioYunanistan")
        self.gridUlke.addWidget(self.radioYunanistan, 3, 0, 1, 1)
        self.groupBoxEgitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEgitim.setGeometry(QtCore.QRect(290, 10, 171, 181))
        self.groupBoxEgitim.setObjectName("groupBoxEgitim")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxEgitim)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 141, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridEgitim = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridEgitim.setContentsMargins(0, 0, 0, 0)
        self.gridEgitim.setObjectName("gridEgitim")
        self.radioLise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioLise.setObjectName("radioLise")
        self.gridEgitim.addWidget(self.radioLise, 1, 0, 1, 1)
        self.radioIlkokul = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioIlkokul.setObjectName("radioIlkokul")
        self.gridEgitim.addWidget(self.radioIlkokul, 0, 0, 1, 1)
        self.radioUniversite = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioUniversite.setObjectName("radioUniversite")
        self.gridEgitim.addWidget(self.radioUniversite, 2, 0, 1, 1)
        self.radioYuksekLisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioYuksekLisans.setObjectName("radioYuksekLisans")
        self.gridEgitim.addWidget(self.radioYuksekLisans, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnUlke.setText(_translate("MainWindow", "Ülke Seçimi"))
        self.btnEgitim.setText(_translate("MainWindow", "Eğitim Seçimi"))
        self.groupBoxUlke.setTitle(_translate("MainWindow", "Ülke"))
        self.radioTurkiye.setText(_translate("MainWindow", "Türkiye"))
        self.radioAzerbeycan.setText(_translate("MainWindow", "Azerbeycan"))
        self.radioAlmanya.setText(_translate("MainWindow", "Almanya"))
        self.radioYunanistan.setText(_translate("MainWindow", "Yunanistan"))
        self.groupBoxEgitim.setTitle(_translate("MainWindow", "Eğitim"))
        self.radioLise.setText(_translate("MainWindow", "Lise"))
        self.radioIlkokul.setText(_translate("MainWindow", "İlkokul"))
        self.radioUniversite.setText(_translate("MainWindow", "Üniversite"))
        self.radioYuksekLisans.setText(_translate("MainWindow", "Yüksek Lisans"))