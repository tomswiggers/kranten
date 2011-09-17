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
    from ui_main import Ui_Main
    
    self.window.placeholder.close()
    Ui_Main(self.window)

  def showClient(self):
    from ui_client import Ui_Client
    self.window.placeholder.close()
    Ui_Client(self.window)

  def showClientNew(self):
    from ui_client_new import Ui_Client_New
    self.window.placeholder.close()
    Ui_Client_New(self.window)

  def showClientEdit(self):
    print "showEdit"
  
  def showClientView(self):
    from ui_client_view import Ui_Client_View

    self.window.placeholder.close()
    Ui_Client_View(self.window)

  def showMaintenance(self):
    from ui_maintenance import Ui_Maintenance

    self.window.placeholder.close()
    Ui_Maintenance(self.window)

  def showMaintenanceBackup(self):
    print "showMaintenanceBackup"

  def showMaintenanceRestore(self):
    print "showMaintenanceRestore"
