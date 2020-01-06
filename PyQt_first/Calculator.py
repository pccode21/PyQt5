import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from functools import partial

qtCreatorFile = r".\PyQt5\PyQt_first\Calculator.ui"  # Enter *.ui file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setFixedSize(243, 235)
        self.setupUi(self)

    def setDisplayText(self, text):
        self.lineEdit.setText(text)
        self.lineEdit.setFocus()

    def displayText(self):
        return self.lineEdit.text()

    def clearDisplay(self):
        self.setDisplayText('')


class MyAppCtrl():
    def __init__(self, view):
        self._view = view
        self._connectSignals()

    def _buildExpression(self, sub_exp):
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for text, btn in self._view.items:
            if text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, text))
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    MyAppCtrl(view=window)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
