from PySide import QtCore, QtGui
from ui import Ui
from newspaper.models import Item
from django.db.models import F

class Ui_Item_List(Ui):
  def __init__(self, window):
    super(Ui_Item_List, self).__init__(window)

  def createButtonBack(self):
    back = QtGui.QPushButton('Terug', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMain)

    return back

  def createButtonEdit(self):
    btn = QtGui.QPushButton('Bekijk', self)
    btn.setToolTip('Bekijk artikel')
    btn.clicked.connect(self.showItemEdit)

    return btn

  def init(self):
    listWidget = QtGui.QListWidget()

    for item in Item.objects.filter():
      print item.name
      QtGui.QListWidgetItem(item.name, listWidget, int(item.id))

    layout = QtGui.QVBoxLayout()
    layout.addWidget(listWidget)

    layoutButtons = QtGui.QVBoxLayout()

    layoutButtons.addWidget(self.createButtonEdit())
    layoutButtons.addWidget(self.createButtonBack())

    layout.addLayout(layoutButtons)


    self.setLayout(layout)
