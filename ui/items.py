from PySide import QtCore, QtGui
from ui import Ui
from config import Config

class Ui_Items(Ui):

  def __init__(self, window):
    super(Ui_Items, self).__init__(window)

  def createButtonNew(self):
    btn = QtGui.QPushButton('Artikel aanmaken', self)
    btn.setToolTip('Een artikel aanmaken.')
    btn.clicked.connect(self.showItemsNew)

    return btn

  def createButtonList(self):
    btn = QtGui.QPushButton('Lijst', self)
    btn.setToolTip('De lijst met alle artikels bekijken.')
    btn.clicked.connect(self.showItemsList)

    return btn

  def createButtonBack(self):
    back = QtGui.QPushButton('Terug', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMain)

    return back

  def init(self):
    layout = QtGui.QVBoxLayout()
    layoutButtons = QtGui.QVBoxLayout()
    layoutMessage = QtGui.QHBoxLayout()

    layoutMessage.addWidget(self.createMessage())

    layoutButtons.addWidget(self.createButtonNew())
    layoutButtons.addWidget(self.createButtonList())
    layoutButtons.addWidget(self.createButtonBack())

    layout.addLayout(layoutMessage)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

