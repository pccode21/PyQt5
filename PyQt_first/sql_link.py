from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
import pymysql


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Database Connection"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.button = QPushButton('DB Connection', self)
        self.button.setGeometry(100, 100, 200, 50)
        self.button.clicked.connect(self.DBConnection)
        self.setWindowIcon(QtGui.QIcon(r".\PyQt5\PyQt_first\images\LOGO.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def DBConnection(self):
        db = pymysql.connect("localhost", "root", "Lxd05230708", "football", charset='utf8mb4')
        try:
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
            with db.cursor() as cursor:
                sql = "select * from player"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print("Id\tSimpName\tTradNamet\tEngName\tprice\tbirthday\tweight\theight\tIdioFoot\tnationality\tcontract")
                    print("---------------------------------------------------------------------------")
                    for row in result:
                        print(str(row[0]) + "\t" + row[1] + "\t" + row[2] +  "\t" + row[3] + "\t" + row[4] + "\t"+ row[5] + "\t"+ str(row[6]) + "\t"+ str(row[7]) + "\t"+ row[8] + "\t" + row[9] + "\t" + row[10])
                except:
                    print("Oops! Something wrong")
            db.commit()
        finally:
            db.close()
            sys.exit(1)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
