# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_mscDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 340, 500))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 530, 130, 16))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 530, 130, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 560, 680, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.buttonTalk = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTalk.setGeometry(QtCore.QRect(690, 560, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonTalk.setFont(font)
        self.buttonTalk.setObjectName("buttonTalk")
        self.labelResponse = QtWidgets.QLabel(self.centralwidget)
        self.labelResponse.setGeometry(QtCore.QRect(360, 310, 500, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResponse.setFont(font)
        self.labelResponse.setFrameShape(QtWidgets.QFrame.Box)
        self.labelResponse.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelResponse.setText("")
        self.labelResponse.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResponse.setObjectName("labelResponse")
        self.labelShowImg = QtWidgets.QLabel(self.centralwidget)
        self.labelShowImg.setGeometry(QtCore.QRect(360, 10, 501, 291))
        self.labelShowImg.setText("")
        self.labelShowImg.setPixmap(QtGui.QPixmap(":/re/normal.png"))
        self.labelShowImg.setScaledContents(False)
        self.labelShowImg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelShowImg.setObjectName("labelShowImg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuClose = QtWidgets.QAction(MainWindow)
        self.menuClose.setObjectName("menuClose")
        self.menu.addAction(self.menuClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.buttonTalk.clicked.connect(MainWindow.buttonTalkSlot)
        self.radioButton_1.clicked.connect(MainWindow.showResponderName)
        self.radioButton_2.clicked.connect(MainWindow.hiddenResponderName)
        self.menuClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_1.setText(_translate("MainWindow", "Responder表示"))
        self.radioButton_2.setText(_translate("MainWindow", "Responder非表示"))
        self.buttonTalk.setText(_translate("MainWindow", "送信"))
        self.menu.setTitle(_translate("MainWindow", "ファイル"))
        self.menuClose.setText(_translate("MainWindow", "閉じる"))
import qt_resource_rc
