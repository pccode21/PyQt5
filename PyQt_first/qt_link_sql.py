import pymysql
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from UseSQL import Ui_mainWindow
from functools import partial
from PyQt5.QtWidgets import QTableWidget, QFrame, QTableWidgetItem
from PyQt5 import QtGui, QtSql, QtCore, QtWidgets


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        Ui_mainWindow.__init__(self)
        self.setFixedSize(600, 400)
        self.setupUi(self)
        db = pymysql.connect("localhost", "root", "Lxd05230708", "football", charset='utf8mb4')
        cur = db.cursor()
        cur.execute("SELECT * FROM player")
        data = cur.fetchall()
        for row in data:
            a = row[0]
            print(a)
        self.view_data.clicked.connect(self.view_data)

    def view_data(self):
        self.model = QtSql.QSqlTableModel()
        self.table_widget.setModel(self.model)
        self.model.setTable('player')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'SimpName')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'TradName')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'EngName')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'price')
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, 'birthday')
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, 'weight')
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, 'height')
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, 'IdioFoot')
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, 'nationality')
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, 'contract')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
