from PySide import QtCore, QtGui

if __name__ == "__main__":
  import os, sys
  
  dir = os.path.dirname(os.path.abspath(__file__))
  dir += "/ui";
  sys.path.append(dir)

  from main import Ui_Main
  from client import Ui_Client

  app = QtGui.QApplication(sys.argv)
  main = Ui_Main()
  sys.exit(app.exec_())
