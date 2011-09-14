from PySide import QtCore, QtGui
from config import Config
from ui import Ui

class Ui_Main(Ui):

  def __init__(self, window):
    super(Ui_Main, self).__init__(window)
    self.window = window
    self.window.placeholder = self
    self.init()

  def init(self):
    layoutFrame = QtGui.QVBoxLayout()
    
    buttonClient = QtGui.QPushButton('Klanten')
    buttonClient.setToolTip('Klanten aanmaken/bewerken')
    buttonClient.clicked.connect(self.showClient)

    buttonService = QtGui.QPushButton('Diensten')
    buttonService.setToolTip('Diensten')

    layoutFrame.addWidget(buttonClient)
    layoutFrame.addWidget(buttonService)

    self.setLayout(layoutFrame)
    self.show()

