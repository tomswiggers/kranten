from PySide import QtCore, QtGui
from ui import Ui
from newspaper.models import Item
from form.item import Form_Item
from django.db.models import F

class Ui_Item_New(Ui):
  def __init__(self, window):
    self.form = Form_Item()
    super(Ui_Item_New, self).__init__(window)

  def init(self):

    for field in Item._meta.fields:
      print field.name
      print field.verbose_name
      print field.get_internal_type()


    layoutForm = self.form.formFields()
    layoutButtons = self.form.formButtons()

    self.form.saveButton.clicked.connect(self.save)
    self.form.cancelButton.clicked.connect(self.showItems)
    self.form.backButton.clicked.connect(self.showMain)

    layout = QtGui.QVBoxLayout()
    layout.addLayout(layoutForm)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

  def save(self):
    item = Item()
    
    for k, v in self.form.elements.items():
      setattr(item, k, v.text())

    item.save()
    self.showItems()
    self.window.destroyFrame('Ui_Item_New')
    self.window.setMessage("Nieuwe artikel " + str(item.id) + " aangemaakt!")
