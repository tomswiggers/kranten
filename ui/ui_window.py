from PySide import QtCore, QtGui
from config import Config

class Ui_Window(QtGui.QWidget):

  def __init__(self):
    super(Ui_Window, self).__init__()
    self.resize(Config.width, Config.height)
    self.setWindowTitle("Kranten")
    self.show()
