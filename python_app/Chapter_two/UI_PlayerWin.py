# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_PlayerWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_PlayerWin(object):
    def setupUi(self, UI_PlayerWin):
        UI_PlayerWin.setObjectName("UI_PlayerWin")
        UI_PlayerWin.setWindowModality(QtCore.Qt.ApplicationModal)
        UI_PlayerWin.resize(400, 138)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r".\PyQt5\python_app\Chapter_two\播放器.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UI_PlayerWin.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(UI_PlayerWin)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(UI_PlayerWin)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.BtPlay = QtWidgets.QPushButton(UI_PlayerWin)
        self.BtPlay.setGeometry(QtCore.QRect(160, 90, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r".\PyQt5\python_app\Chapter_two\播放.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtPlay.setIcon(icon1)
        self.BtPlay.setObjectName("BtPlay")

        self.retranslateUi(UI_PlayerWin)
        self.BtPlay.clicked.connect(UI_PlayerWin.playMedia)
        QtCore.QMetaObject.connectSlotsByName(UI_PlayerWin)

    def retranslateUi(self, UI_PlayerWin):
        _translate = QtCore.QCoreApplication.translate
        UI_PlayerWin.setWindowTitle(_translate("UI_PlayerWin", "媒体播放器"))
        self.label.setText(_translate("UI_PlayerWin", "请输入要播放的媒体文件名："))
        self.BtPlay.setText(_translate("UI_PlayerWin", "播放"))
