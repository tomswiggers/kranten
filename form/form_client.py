from PySide import QtCore, QtGui
from client import Client

class Form_Client(QtGui.QWidget):
  def __init__(self):
    super(Form_Client, self).__init__()

  def formFields(self):
    self.name = QtGui.QLineEdit()
    self.firstname = QtGui.QLineEdit()
    self.street = QtGui.QLineEdit()

    layout = QtGui.QFormLayout()
    layout.addRow(self.tr("Naam:"), self.name)
    layout.addRow(self.tr("Voornaam:"), self.firstname)
    layout.addRow(self.tr("Straat:"), self.street)

    return layout

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


