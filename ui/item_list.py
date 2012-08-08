from PySide import QtCore, QtGui
from ui import Ui
from newspaper.models import Item
from django.db.models import F

class Ui_Item_List(Ui):
  def __init__(self, window):
    super(Ui_Item_List, self).__init__(window)

  def init(self):
    listWidget = QtGui.QListWidget()

    for item in Item.objects.filter():
      print item.name
      QtGui.QListWidgetItem(item.name, listWidget, int(item.id))

    layout = QtGui.QVBoxLayout()
    layout.addWidget(listWidget)

    self.setLayout(layout)
