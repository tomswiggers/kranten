from PySide import QtCore, QtGui

from ui import Ui
from form.client import Form_Client
from newspaper.models import Client

class Ui_Client_View(Ui):
  def __init__(self, window):
    super(Ui_Client_View, self).__init__(window)

  def createSearchForm(self):
    self.clientNumber = QtGui.QLineEdit()
    self.clientName = QtGui.QLineEdit()
    self.clientFirstname = QtGui.QLineEdit()
    self.searchButton = QtGui.QPushButton("zoek")

    self.searchButton.clicked.connect(self.search)

    layoutSearch = QtGui.QVBoxLayout()

    number = QtGui.QHBoxLayout()
    number.addWidget(QtGui.QLabel("Klantnummer"))
    number.addWidget(self.clientNumber)
    layoutSearch.addLayout(number)

    name = QtGui.QHBoxLayout()
    name.addWidget(QtGui.QLabel("Naam"))
    name.addWidget(self.clientName)
    layoutSearch.addLayout(name)
    
    firstname = QtGui.QHBoxLayout()
    firstname.addWidget(QtGui.QLabel("Voornaam"))
    firstname.addWidget(self.clientFirstname)
    layoutSearch.addLayout(firstname)
    
    layoutSearch.addWidget(self.searchButton)
 
    return layoutSearch

  def createBackButtons(self):
    layout = QtGui.QHBoxLayout()

    self.backButton = QtGui.QPushButton("Terug")
    self.backButton.clicked.connect(self.showClient)
    
    self.backMainButton = QtGui.QPushButton("Terug naar hoofdmenu")
    self.backMainButton.clicked.connect(self.showMain)
    
    layout.addWidget(self.backButton)
    layout.addWidget(self.backMainButton)

    return layout

  def init(self):
    self.layout = QtGui.QVBoxLayout()
    self.layout.addLayout(self.createSearchForm())

    self.formSearch = Form_Client()
    layoutForm = self.formSearch.formFields()
    self.formSearch.disableFormFields()

    self.layout.addLayout(layoutForm)
    self.layout.addLayout(self.createBackButtons())
  
    self.setLayout(self.layout)

  def search(self):

    if len(self.clientNumber.text()):
      client = Client.objects.get(id = int(self.clientNumber.text()))
    elif len(self.clientName.text()):
      client = Client.objects.get(name = self.clientName.text())
    elif len(self.clientFirstname.text()):
      client = Client.objects.get(firstname = self.clientFirstname.text())
    
    self.formSearch.populateFormFields(client)
