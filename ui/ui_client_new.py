from PySide import QtCore, QtGui
from client import Client

from ui import Ui

from form_client import Form_Client

class Ui_Client_New(Ui):
  def __init__(self, window):
    self.form = Form_Client()
    super(Ui_Client_New, self).__init__(window)

  def init(self):
    layoutForm = self.form.formFields()
    layoutButtons = self.form.formButtons()

    self.form.saveButton.clicked.connect(self.save)
    self.form.cancelButton.clicked.connect(self.showClient)
    self.form.backButton.clicked.connect(self.showMain)

    layout = QtGui.QVBoxLayout()
    layout.addLayout(layoutForm)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

  def save(self):
    client = self.form.getValues()
    client.save()

    self.window.placeholder.close()

    self.showClient()

    self.window.placeholder.setMessage("Nieuwe klant met nummer " + str(client.id) + " aangemaakt!")
