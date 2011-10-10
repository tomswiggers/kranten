from PySide import QtCore, QtGui
from newspaper.models import Client

class Form_Client():
  elements = dict()
  
  def __init__(self):
    print "init"

  def setButtonSave(self, func):
    self.saveButton.clicked.connect(func)

  def formFields(self):
    layout = QtGui.QFormLayout()

    for field in Client._meta.fields:

      if field.name == 'order':
        self.createOrderList()
        layout.addRow(field.verbose_name, self.listWidget)
      elif field.name == 'round':
        layout.addRow(field.verbose_name, self.createRadioButtons())
        self.group.buttonClicked.connect(self.fillOrderList)
      elif field.get_internal_type() == 'CharField': 
        self.elements[field.name] = QtGui.QLineEdit()
        layout.addRow(field.verbose_name, self.elements[field.name])
      
    return layout

  def createOrderList(self):
    self.listWidget = QtGui.QListWidget()
    self.listWidget.clear()

  def fillOrderList(self):
    round = self.group.checkedId()

    self.listWidget.clear()
  
    QtGui.QListWidgetItem('begin', self.listWidget, 0)

    for client in Client.objects.filter(round = round).order_by('order'):
      QtGui.QListWidgetItem(str(client.order) + ':' + client.name + ', ' + client.street + ', ' + client.number, self.listWidget, int(client.order))

    QtGui.QListWidgetItem('einde', self.listWidget, -1)

  def createRadioButtons(self):
    hbox = QtGui.QHBoxLayout()
    round1 = QtGui.QRadioButton('1')
    round2 = QtGui.QRadioButton('2')
    round3 = QtGui.QRadioButton('3')

    hbox.addWidget(round1)
    hbox.addWidget(round2)
    hbox.addWidget(round3)

    self.group = QtGui.QButtonGroup()
    
    self.group.addButton(round1, 1)
    self.group.addButton(round2, 2)
    self.group.addButton(round3, 3)

    return hbox

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
