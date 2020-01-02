# ************************************************************************/
# *@Copyright (c) 2020,https://github.com/pccode21/
# *@All rights reserved.
# *@File Name         : PyQt_first.py
# *@Author            : LinXuDong
# *@Language          : Python
# *@Created Date      : 2020/1/2 15:55
# *@App inter         : PyQt5
# ************************************************************************/

import sys

from PyQt5 import QtWidgets, uic


qtCreatorFile = r".\PyQt5\PyQt_first\tax_calc.ui"  # Enter *.ui file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.calculate_tax)

    def calculate_tax(self):
        price = int(self.price_box.toPlainText())
        tax = self.tax_rate.value()
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: {:.2f}".format(total_price)
        self.results_window.setText(total_price_string)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
