from PySide import QtCore, QtGui
from ui import Ui
from form.client import Form_Client
from django.db.models import F

from newspaper.models import *

class Ui_Client_New(Ui):
  def __init__(self, window):
    self.form = Form_Client()
    super(Ui_Client_New, self).__init__(window)

  def init(self):
    client = Client()
    #print client._get_FIELD_display()	
    print dir(client)

    for field in Client._meta.fields:
      print field.name
      print field.verbose_name
      print field.get_internal_type()


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
    client = Client()
    
    for k, v in self.form.elements.items():
      setattr(client, k, v.text())

    round_nbr = self.form.group.checkedId()
    setattr(client, 'round_nbr', round_nbr)

    for listWidget in self.form.listWidget.selectedItems():
      order = listWidget.type()

    if order == -1:
      order = Client.objects.filter(round_nbr = round_nbr).count()
      order = order
    else:
      Client.objects.filter(round_nbr = round_nbr, order__gte = order).update(order = F('order') + 1)
    
    setattr(client, 'order', order)

    print "order:" + str(order)

    client.save()
    self.showClient()
    self.window.destroyFrame('Ui_Client_New')
    self.window.setMessage("Nieuwe klant met nummer " + str(client.id) + " aangemaakt!")
