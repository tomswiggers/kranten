from PySide import QtCore, QtGui

class Ui_Main(QtGui.QWidget):
  button_height = 20
  button_width = 100

  def __init__(self):
    super(Ui_Main, self).__init__()
    self.resize(600, 800)
    self.setWindowTitle("Kranten")
    self.showMainWindow()
    self.show()

  def showMainWindow(self):
    self.main = QtGui.QWidget(self)
    btn = QtGui.QPushButton('Klanten', self.main)
    btn.setToolTip('Klanten aanmaken/bewerken')
    btn.setGeometry(10, 20, self.button_width, self.button_height)
    btn.clicked.connect(self.showClient)

    btn2 = QtGui.QPushButton('Diensten', self.main)
    btn2.setToolTip('????')
    btn2.setGeometry(10, 50, self.button_width, self.button_height)

    self.main.show()

  def showClient(self):
    import os, sys

    dir = os.path.dirname(os.path.abspath(__file__))
    dir += "/ui";
    sys.path.append(dir)

    from client import Ui_Client

    client = Ui_Client(self)
    self.main.hide()  
