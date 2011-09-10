from PySide import QtCore, QtGui
from client import Client
from form_client import Form_Client

class Ui_Client_New(QtGui.QWidget):
  def __init__(self, mainWindow, parentWindow):
    super(Ui_Client_New, self).__init__(mainWindow)
    
    self.mainWindow = mainWindow
    self.parentWindow = parentWindow
    self.form = Form_Client()

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
    '''
    layoutInput = QtGui.QVBoxLayout()
    layoutInput.addWidget(self.name)
    layoutInput.addWidget(self.firstname)
    '''
    
    layoutForm = self.form.formFields()

    '''
    layoutLabels = QtGui.QVBoxLayout()
    layoutLabels.addWidget(QtGui.QLabel("Naam"))
    layoutLabels.addWidget(QtGui.QLabel("Voornaam"))

    layoutForm = QtGui.QHBoxLayout()
    layoutForm.addLayout(layoutLabels)
    layoutForm.addLayout(layoutInput)
    '''
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
