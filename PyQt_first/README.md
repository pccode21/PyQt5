我的第一个使用Python和PyQt5的GUI应用程序
======================================
一.介绍
-------
许多人都在努力学习如何构建GUI应用程序。最常见的原因是，他们甚至不知道从哪里开始。大多数教程都是纯粹基于文本的，并且由于GUI主要是可视介质，因此很难学习使用文本进行GUI开发。<br>
我们将通过构建一个简单的GUI应用程序来解决这个问题，并向您展示入门的容易程度。一旦了解了基础知识，就可以轻松添加高级内容。<br>
这是我们将要构建的：<br>
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt5.gif) <br>
一个简单的GUI应用程序，可以获取价格，税率并计算最终价格。<br>
大多数关于GUI应用程序的教程都尝试使用代码来布局GUI块，但这非常痛苦。我们将使用一流的QT Designer工具来布局我们的应用程序：<br>
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt1.gif) <br>
因此，无需费力地手工布置设计。一切都将以图形方式完成。<br>
所有[源代码都在这里](https://github.com/pccode21/PyQt5/tree/master/PyQt_first)。<br>

二.先决条件
----------
首先，我们必须按照PyQt5和pyqt5_tools，而designer.exe在pyqt5_tools安装后的pyqt5_tools\Qt\bin里面，用以下命令可以安装：<br>
```Python
pip install PyQt5
pip install pyqt5_tools
```

三.入门
-------
启动QT Designer,可以随意的可视化编辑窗体。 <br>
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt2.gif) <br>
保存后是一个*.ui文件，也是一个XML文件，如果需要，可以在文本编辑器中将其打开，然后您将找到以下内容： <br>
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt3.gif) <br>

四.编写代码
-----------
Qt的代码是面向对象的，并且易于遵循。我们添加的每个小部件都是一个对象，它具有自己的功能，例如toPlainText（）（用于读取框中的值）。这使得它非常容易使用。<br>
我确定官方文档在某处提到了这一点，但是在使用代码之前，您必须进行一些设置。我在任何地方都找不到此设置，因此我从官方示例（以及其他在线教程）中查找了初始化类所需的最小程序。我已经在[pyqt_skeleton.py](https://github.com/pccode21/PyQt5/tree/master/PyQt_first/pyqt_skeleton.py)中检查了此功能。<br>
这很有用，因为每次您启动新的PyQt项目时，都使用此框架开始并添加代码。<br>
代码是：<br>
```Python
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
```
要注意的主要是第3行：<br>
```Python
qtCreatorFile = r".\PyQt5\PyQt_first\tax_calc.ui"
```
在此添加先前创建的*.ui文件。它是使用内置函数加载的：<br>
```Python
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
```
让我们快速看一下代码：<br>
```Python
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
```
主要代码创建一个新的Qt Gui应用程序。由于可以从命令行配置QT，因此需要传递sys.argv。我们不会那样做。<br>
最后，我们创建一个名为MyWindow的类，该类继承自Qt库并初始化父类：<br>
```Python
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
```
取这个文件pyqt_skeleton.py，并将其重命名为pyqt_first.py。那是因为我们不想编辑原始文件。<br>
现在，GUI中的关键小部件是按钮。按下按钮后，事情发生了。什么？我们需要告诉我们的代码，当用户按下Calculate Tax按钮时该怎么做。在__init__函数中，添加以下行：<br>
```Python
self.calc_tax_button.clicked.connect(self.calculate_tax)
```
这是做什么的？还记得我们叫按钮calc_tax_button吗？（这是对象的名称，而不是显示在其上的文本。）单击是一个内部函数，当（惊讶）有人单击按钮时会调用该内部函数。所有QT小部件都有特定的功能，您可以通过Googling找到我们的功能。该代码的最后一部分说connect（self.calculate_tax）。这表示将此按钮连接到一个名为self.calculate_tax的函数，以便每次用户按下该按钮时都会调用该函数。<br>
我们尚未编写该函数。让我们现在就开始做吧。<br>
在MyWindow类中，添加另一个函数。我们将首先查看整个功能，然后再详细介绍：<br>
```Python
def calculate_tax(self):
    price = int(self.price_box.toPlainText())
    tax = self.tax_rate.value()
    total_price = price + ((tax / 100) * price)
    total_price_string = "The total price with tax is: {:.2f}".format(total_price)
    self.results_window.setText(total_price_string)
```
好的，让我们逐行查看上面的代码。<br>
我们必须做两件事：阅读价格框，阅读税框，然后计算最终价格。现在开始吧。请记住，我们将使用给它们提供的名称来调用这些对象（这就是为什么我问您不要使用默认的通用名称，如box1，因为那样会很快使您感到困惑）。<br>
```Python
price = int(self.price_box.toPlainText())
```
我们阅读了price_box。toPlainText（）是一个内部函数，它读取存储在该框中的值。顺便说一下，您不必记住所有这些功能。我只是用Google之类的“ Qt Textbox read data”之类的东西来查找函数的名称，尽管一段时间后您将开始记住这些名称，因为它们的名称逻辑上很合理。<br>
读取的值是一个字符串，因此我们将其转换为整数并将其存储在名为price的变量中。<br>
接下来，我们阅读税框：<br>
```Python
tax = self.tax_rate.value()
```
同样，value（）是从spinbox读取的函数。谢谢，谷歌。<br>
现在我们有了这两个值，我们可以使用非常高科技的数学方法来计算最终价格：<br>
```Python
total_price = price + ((tax / 100) * price)
total_price_string = "The total price with tax is: {:.2f}".format(total_price)
```
我们用最终价格创建一个字符串。这是因为我们将直接将此字符串输出到我们的应用程序：<br>
```Python
self.results_window.setText(total_price_string)
```
在results_window中，我们调用函数setText（），该函数输出我们创建的字符串。<br>
只需使用以下命令运行文件：<br>
```Python
python pyqt_first.py
```
![](https://github.com/pccode21/PyQt5/blob/master/PyQt_first/images/qt4.gif) <br>
到处，介绍完毕！
