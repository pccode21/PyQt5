我的第一个使用Python和PyQt5的GUI应用程序
======================================
一.介绍
-------
许多人都在努力学习如何构建GUI应用程序。最常见的原因是，他们甚至不知道从哪里开始。大多数教程都是纯粹基于文本的，并且由于GUI主要是可视介质，因此很难学习使用文本进行GUI开发。<br>
我们将通过构建一个简单的GUI应用程序来解决这个问题，并向您展示入门的容易程度。一旦了解了基础知识，就可以轻松添加高级内容。<br>
这是我们将要构建的：<br>
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt19.gif) <br>
一个简单的GUI应用程序，可以获取价格，税率并计算最终价格。<br>
大多数关于GUI应用程序的教程都尝试使用代码来布局GUI块，但这非常痛苦。我们将使用一流的QT Designer工具来布局我们的应用程序：<br>
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt21-1024x616.gif) <br>
因此，无需费力地手工布置设计。一切都将以图形方式完成。<br>
所有[源代码都在这里](https://github.com/pccode21/PyQt5/tree/master/PyQt_first)。<br>
二.先决条件
----------
三.入门
-------
四.编写代码
-----------
Qt的代码是面向对象的，并且易于遵循。我们添加的每个小部件都是一个对象，它具有自己的功能，例如toPlainText（）（用于读取框中的值）。这使得它非常容易使用。<br>
我确定官方文档在某处提到了这一点，但是在使用代码之前，您必须进行一些设置。我在任何地方都找不到此设置，因此我从官方示例（以及其他在线教程）中查找了初始化类所需的最小程序。我已经在[pyqt_skeleton.py](https://github.com/pccode21/PyQt5/tree/master/PyQt_first/pyqt_skeleton.py)中检查了此功能。<br>
这很有用，因为每次您启动新的PyQt项目时，都使用此框架开始并添加代码。<br>
代码是：<br>
```Python
import sys
from PyQt5 import QtCore, QtGui, uic

qtCreatorFile = "" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
```
