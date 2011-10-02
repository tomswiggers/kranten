from PySide import QtCore, QtGui
from ui import Ui
from form_client import Form_Client

class Ui_Client_View(Ui):
  def __init__(self, window):
    super(Ui_Client_View, self).__init__(window)

  def createSearchForm(self):
    self.clientNumber = QtGui.QLineEdit()
    self.searchButton = QtGui.QPushButton("zoek")

    self.searchButton.clicked.connect(self.search)

    layoutSearch = QtGui.QHBoxLayout()
    layoutSearch.addWidget(QtGui.QLabel("Klantnummer"))
    layoutSearch.addWidget(self.clientNumber)
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
    client = Client()
    client.getClientById(self.clientNumber.text())

    self.formSearch.populateFormFields(client)
