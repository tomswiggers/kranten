from PySide import QtCore, QtGui
from config import Config

from main import Ui_Main
from client import Ui_Client
from client_new import Ui_Client_New
from client_view import Ui_Client_View
from maintenance import Ui_Maintenance
from maintenance_backup import Ui_Maintenance_Backup

class Ui_Window(QtGui.QWidget):
  frames = dict()
  current = ""

  def __init__(self):
    super(Ui_Window, self).__init__()
    self.resize(Config.width, Config.height)
    self.setWindowTitle("Kranten")
    self.show()

  def showFrame(self, key):

    if len(self.current):
      self.frames[self.current].hide()

    self.current = key

    if not self.frames.has_key(key):
      print "create instance: " + key
      self.frames[key] = eval(key)(self)

    self.frames[key].show()

  def setMessage(self, message):
    self.frames[self.current].message.setText(message)

  def destroyFrame(self, key):
    del self.frames[key]
