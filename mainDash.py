from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from mainUi import Ui_MainWindow
import sys
import backend as Main

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.mainBackend()

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton.clicked.connect(self.startFunc)

    def startFunc(self):
        self.jarvis_ui.movies = QtGui.QMovie("Dash.gif")
        self.jarvis_ui.Gif.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()
        startFunctions.start()


