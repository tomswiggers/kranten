from PySide import QtCore, QtGui

class Form_Client():
  elements = dict()
  
  def __init__(self):
    print "init"

  def setButtonSave(self, func):
    self.saveButton.clicked.connect(func)

  def formFields(self):
    self.elements["name"] = QtGui.QLineEdit()
    self.elements["firstname"] = QtGui.QLineEdit()
    self.elements["street"] = QtGui.QLineEdit()

    layout = QtGui.QFormLayout()
    layout.addRow("Naam:", self.elements["name"])
    layout.addRow("Voornaam:", self.elements["firstname"])
    layout.addRow("Straat:", self.elements["street"])

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
      self.elements[k].setText(client.getValue(k))

  def disableFormFields(self):

    for k, v in self.elements.items():
      print k
      self.elements[k].setReadOnly(True)

  def getValues(self):
    client = Client()

    for k, v in self.elements.items():
      client.setValue(k, v.text())

    return client
