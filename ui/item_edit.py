from PySide import QtCore, QtGui
from ui import Ui
from newspaper.models import Item
from django.db.models import F

class Ui_Item_Edit(Ui):
  def __init__(self, window):
    super(Ui_Item_Edit, self).__init__(window)

  def createButtonBack(self):
    back = QtGui.QPushButton('Terug', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMain)

    return back

  def init(self):
    layout = QtGui.QVBoxLayout()

    layoutButtons = QtGui.QVBoxLayout()

    layoutButtons.addWidget(self.createButtonBack())
    layoutButtons.addWidget(self.createButtonMainMenu())

    layout.addLayout(layoutButtons)

    self.setLayout(layout)
