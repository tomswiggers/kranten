from PySide import QtCore, QtGui
from newspaper.models import Item

class Form_Item():
  elements = dict()
  
  def __init__(self):
    print "init"

  def setButtonSave(self, func):
    self.saveButton.clicked.connect(func)

  def formFields(self):
    layout = QtGui.QFormLayout()

    for field in Item._meta.fields:

      if field.get_internal_type() == 'CharField': 
        self.elements[field.name] = QtGui.QLineEdit()
        layout.addRow(field.verbose_name, self.elements[field.name])
      
    return layout

  def formButtons(self):
    self.saveButton = QtGui.QPushButton("Opslaan")
    self.cancelButton = QtGui.QPushButton("Annuleer")
    self.backButton = QtGui.QPushButton("Terug naar hoofdmenu")

    layoutButtons = QtGui.QHBoxLayout()
    layoutButtons.addWidget(self.saveButton)
    layoutButtons.addWidget(self.cancelButton)
    layoutButtons.addWidget(self.backButton)

    return layoutButtons

  def populateFormFields(self, client):

    for k, v in self.elements.items():
      print k
      print getattr(client, k)
      print client.name
      self.elements[k].setText(getattr(client, k))

  def disableFormFields(self):

    for k, v in self.elements.items():
      print k
      self.elements[k].setReadOnly(True)

  def getValues(self):
    client = Client()

    for k, v in self.elements.items():
      client.setValue(k, v.text())

    return client
