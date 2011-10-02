from PySide import QtCore, QtGui
from ui import Ui
from config import Config

class Ui_Maintenance(Ui):

  def __init__(self, window):
    super(Ui_Maintenance, self).__init__(window)

  def createButtonBackup(self):
    btn = QtGui.QPushButton('Backup maken', self)
    btn.setToolTip('Een backup aanmaken.')
    btn.clicked.connect(self.showMaintenanceBackup)

    return btn

  def createButtonRestore(self):
    btn = QtGui.QPushButton('Backup herstellen', self)
    btn.setToolTip('Een eerder gemaakte backup terugzetten.')
    btn.clicked.connect(self.showMaintenanceRestore)

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

    layoutButtons.addWidget(self.createButtonBackup())
    layoutButtons.addWidget(self.createButtonRestore())
    layoutButtons.addWidget(self.createButtonBack())

    layout.addLayout(layoutMessage)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

