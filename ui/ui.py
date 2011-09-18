from PySide import QtCore, QtGui
from config import Config

class Ui(QtGui.QWidget):

  def __init__(self, window):
    super(Ui, self).__init__(window)
    self.window = window
    self.window.placeholder = self
    self.init()
    self.setMinimumSize(Config.width, 0)
    self.show()

  def createTitle(self, string):
    title = QtGui.QLabel(string)
    title.setAlignment(QtCore.Qt.AlignCenter)

    return title
  
  def createMessage(self):
    self.message = QtGui.QLabel()
    self.message.setMinimumWidth(400)

    return self.message
  
  def showMain(self):
    print "Ui.showMain"
    self.window.showFrame("Ui_Main")

  def showClient(self):
    print "Ui.showClient"
    self.window.showFrame("Ui_Client")

  def showClientNew(self):
    print "Ui.showClientNew"
    self.window.showFrame("Ui_Client_New")

  def showClientEdit(self):
    print "Ui.showEdit"
  
  def showClientView(self):
    print "Ui.showClientEdit"
    self.window.showFrame("Ui_Client_View")

  def showMaintenance(self):
    print "Ui.showMaintenance"
    self.window.showFrame("Ui_Maintenance")

  def showMaintenanceBackup(self):
    print "showMaintenanceBackup"

  def showMaintenanceRestore(self):
    print "showMaintenanceRestore"
