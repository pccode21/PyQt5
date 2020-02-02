import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from UI_PlayerWin import Ui_UI_PlayerWin


# 这里的QtWidgets.QWidget是因为在定义图形界面主窗口时，选择的窗口类型是QWidget，如果是其他类型需要更换成对应类型
class MediaPlayerWin(QtWidgets.QWidget, Ui_UI_PlayerWin):
    def __init__(self):  # 定义构造方法
        super(MediaPlayerWin, self).__init__()
        self.setupUi(self)  # 构造方法至少需要调用父类的构造方法和UI界面类的setupUi方法

    # 实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    def playMedia(self):
        QMessageBox.information(self, '播放提示', '即将播放:'+self.lineEdit.text())


if __name__ == '__main__':
    # 每一个pyqt程序必须创建一个application对象，sys.argv是命令行参数，可以通过命令启动的时候传递参数。
    app = QtWidgets.QApplication(sys.argv)
    mainwin = MediaPlayerWin()  # 初始化主程序窗口
    mainwin.show()  # 显示
    sys.exit(app.exec_())
    """
    主循环程序的任务就是等待事件，并把事件通过信号和槽的连接关系发送给指定应用处理。
    当调用app.exit()或者程序因为各种原因被破坏后，使用sys.exit()关闭程序，并释放内存资源。
    """
