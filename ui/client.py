from PySide import QtCore, QtGui
from ui import Ui
from config import Config

class Ui_Client(Ui):

  def __init__(self, window):
    super(Ui_Client, self).__init__(window)

  def createButtonNew(self):
    new = QtGui.QPushButton('Nieuw', self)
    new.setToolTip('Klanten aanmaken/bewerken')
    new.clicked.connect(self.showClientNew)

    return new

  def createButtonView(self):
    edit = QtGui.QPushButton('Raadpleeg', self)
    edit.setToolTip('Gegevens van een klant raadplegen')
    edit.clicked.connect(self.showClientView)

    return edit

  def createButtonEdit(self):
    edit = QtGui.QPushButton('Wijzig', self)
    edit.setToolTip('Gegevens van een klant wijzigen')
    edit.clicked.connect(self.showClientEdit)

    return edit

  def createButtonBack(self):
    back = QtGui.QPushButton('Terug', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMain)

    return back

  def init(self):
    layout = QtGui.QVBoxLayout()
    layoutButtons = QtGui.QVBoxLayout()
    layoutMessage = QtGui.QHBoxLayout()

    #layoutMessage.addWidget(self.createTitle("Klanten"))
    layoutMessage.addWidget(self.createMessage())

    layoutButtons.addWidget(self.createButtonNew())
    layoutButtons.addWidget(self.createButtonView())
    layoutButtons.addWidget(self.createButtonEdit())
    layoutButtons.addWidget(self.createButtonBack())

    layout.addLayout(layoutMessage)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)


