# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UseSQL.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r".\PyQt5\PyQt_first\images\LOGO.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background-image: url(./PyQt5/PyQt_first/images/bg.png);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setStyleSheet("background-image: url(./PyQt5/PyQt_first/images/bg1.jpg);")
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(95, 0))
        self.groupBox.setObjectName("groupBox")
        self.view_data = QtWidgets.QPushButton(self.groupBox)
        self.view_data.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.view_data.setObjectName("view_data")
        self.up_data = QtWidgets.QPushButton(self.groupBox)
        self.up_data.setGeometry(QtCore.QRect(10, 70, 75, 23))
        self.up_data.setObjectName("up_data")
        self.add_row = QtWidgets.QPushButton(self.groupBox)
        self.add_row.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.add_row.setObjectName("add_row")
        self.delete_row = QtWidgets.QPushButton(self.groupBox)
        self.delete_row.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.delete_row.setObjectName("delete_row")
        self.close = QtWidgets.QPushButton(self.groupBox)
        self.close.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "林旭东-在PyQt5中使用数据库"))
        self.groupBox.setTitle(_translate("mainWindow", "数据库按钮"))
        self.view_data.setText(_translate("mainWindow", "浏览数据"))
        self.up_data.setText(_translate("mainWindow", "更新数据"))
        self.add_row.setText(_translate("mainWindow", "添加一行"))
        self.delete_row.setText(_translate("mainWindow", "删除一行"))
        self.close.setText(_translate("mainWindow", "退出"))
