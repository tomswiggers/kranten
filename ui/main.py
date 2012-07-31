from PySide import QtCore, QtGui
from config import Config
from ui import Ui

class Ui_Main(Ui):

  def __init__(self, window):
    super(Ui_Main, self).__init__(window)
    self.init()

  def init(self):
    layoutFrame = QtGui.QVBoxLayout()
   
    layoutFrame.addWidget(self.createMessage())

    buttonClient = QtGui.QPushButton('Klanten')
    buttonClient.setToolTip('Klanten aanmaken/bewerken')
    buttonClient.clicked.connect(self.showClient)

    buttonItems = QtGui.QPushButton('Artikels')
    buttonItems.setToolTip('Artikels aanmaken/bewerken')
    buttonItems.clicked.connect(self.showItems)

    buttonMaintenance = QtGui.QPushButton('Onderhoud')
    buttonMaintenance.setToolTip('Backup en herstellen')
    buttonMaintenance.clicked.connect(self.showMaintenance)
    
    buttonClose = QtGui.QPushButton('Afsluiten')
    buttonClose.setToolTip('Sluit het programma af.')
    buttonClose.clicked.connect(self.window.close)

    layoutFrame.addWidget(buttonClient)
    layoutFrame.addWidget(buttonItems)
    layoutFrame.addWidget(buttonMaintenance)
    layoutFrame.addWidget(buttonClose)

    self.setLayout(layoutFrame)
    self.show()

