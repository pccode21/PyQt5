from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow

from datetime import datetime
import json
import os
import sys
import requests
from urllib.parse import urlencode

# OPENWEATHERMAP_API_KEY = os.environ.get('b020112734ca76c7df0ccad361a58fa3')

"""
从https://openweathermap.org/获取API密钥以与此结合使用
应用.

"""


def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")


class WorkerSignals(QObject):
    '''
    定义正在运行的工作线程可用的信号.
    '''
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)

class WeatherWorker(QRunnable):
    '''
    工作线程天气更新.
    '''
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @pyqtSlot()
    def run(self):
        try:
            params = dict(
                q=self.location,
                appid='b020112734ca76c7df0ccad361a58fa3'
            )

            url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            weather = json.loads(r.text)

            # 检查我们是否失败（预测将以同样的方式失败）.
            if weather['cod'] != 200:
                raise Exception(weather['message'])

            url = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            forecast = json.loads(r.text)

            self.signals.result.emit(weather, forecast)

        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.pressed.connect(self.update_weather)

        self.threadpool = QThreadPool() # 创建线程池类，以处理运行工作程序

        self.show()


    def alert(self, message):
        alert = QMessageBox.warning(self, "Warning", message)

    def update_weather(self):
        worker = WeatherWorker(self.lineEdit.text())
        worker.signals.result.connect(self.weather_result)
        worker.signals.error.connect(self.alert)
        self.threadpool.start(worker)

    def weather_result(self, weather, forecasts):
        self.latitudeLabel.setText("%.2f °" % weather['coord']['lat'])
        self.longitudeLabel.setText("%.2f °" % weather['coord']['lon'])

        self.windLabel.setText("%.2f m/s" % weather['wind']['speed'])

        self.temperatureLabel.setText("%.1f °C" % weather['main']['temp'])
        self.pressureLabel.setText("%d" % weather['main']['pressure'])
        self.humidityLabel.setText("%d" % weather['main']['humidity'])

        self.sunriseLabel.setText(from_ts_to_time_of_day(weather['sys']['sunrise']))
# 使用自定义from_ts_to_time_of_day函数处理时间戳，以am / pm格式返回用户友好的一天中的时间，且不带前导零。
        self.weatherLabel.setText("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        )
                                  )

        self.set_weather_icon(self.weatherIcon, weather['weather'])

        for n, forecast in enumerate(forecasts['list'][:5], 1):
            getattr(self, 'forecastTime%d' % n).setText(from_ts_to_time_of_day(forecast['dt']))
            self.set_weather_icon(getattr(self, 'forecastIcon%d' % n), forecast['weather'])
            getattr(self, 'forecastTemp%d' % n).setText("%.1f °C" % forecast['main']['temp'])
# 从weatherdict 设置当前的天气图标，然后遍历所提供的前5个天气预报。预报图标，时间和温度标签在Qt Designer中使用forecastIcon<n>，forecastTime<n>和定义 forecastTemp<n>，可以轻松地依次迭代它们并使用getattr当前迭代索引检索它们。

    def set_weather_icon(self, label, weather):
        label.setPixmap(
            QPixmap(os.path.join('./PyQt5/weather/images', "%s.png" %
                                 weather[0]['icon']
                                 )
                    )

        )


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()
