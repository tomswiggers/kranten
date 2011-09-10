from PySide import QtCore, QtGui

class Ui_Client_New(QtGui.QWidget):
  def __init__(self, mainWindow, parentWindow):
    super(Ui_Client_New, self).__init__(mainWindow)
    
    self.mainWindow = mainWindow
    self.parentWindow = parentWindow
    
    self.showNew()
    self.show()

  def showNew(self):
    self.name = QtGui.QLineEdit()
    self.firstname = QtGui.QLineEdit()

    self.saveButton = QtGui.QPushButton("Opslaan")
    self.saveButton.clicked.connect(self.save)

    self.cancelButton = QtGui.QPushButton("Annuleer")
    self.cancelButton.clicked.connect(self.showClient)
  
    self.backButton = QtGui.QPushButton("Terug naar hoofdmenu")
    self.backButton.clicked.connect(self.showMainWindow)

    layoutInput = QtGui.QVBoxLayout()
    layoutInput.addWidget(self.name)
    layoutInput.addWidget(self.firstname)

    layoutLabels = QtGui.QVBoxLayout()
    layoutLabels.addWidget(QtGui.QLabel("Naam"))
    layoutLabels.addWidget(QtGui.QLabel("Voornaam"))

    layoutForm = QtGui.QHBoxLayout()
    layoutForm.addLayout(layoutLabels)
    layoutForm.addLayout(layoutInput)

    layoutButtons = QtGui.QHBoxLayout()
    layoutButtons.addWidget(self.saveButton)
    layoutButtons.addWidget(self.cancelButton)
    layoutButtons.addWidget(self.backButton)

    layout = QtGui.QVBoxLayout()
    layout.addLayout(layoutForm)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

  def showClient(self):
    self.hide()
    self.parentWindow.show()
  
  def showMainWindow(self):
    self.hide()
    self.mainWindow.main.show()

  def save(self):
    client = Client()
    client.name = self.name.text()
    client.firstname = self.firstname.text()

    client.save()
    self.hide()
    self.parentWindow.show()
    self.parentWindow.setMessage("Nieuwe klant met nummer " + str(client.id) + " aangemaakt!")


class Client:
  import shelve
  filename = "clients.shelve"
  client = dict()

  def __setattr__(self, key, value):
    self.client[key] = value

  def __getattr__(self, key):
    return self.client[key]

  def getNewClientId(self):
    d = self.shelve.open(self.filename)

    if (d.has_key("seq")):
      id = d["seq"] + 1
    else:
      id = 1

    d.close()

    return id

  def save(self):
    id = self.getNewClientId()
    self.client["id"] = id

    d = self.shelve.open(self.filename)
    d["seq"] = id
    d[str(id)] = self.client

    d.close()
