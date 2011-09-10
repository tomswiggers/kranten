from PySide import QtCore, QtGui

if __name__ == "__main__":
  import os, sys
  
  base = os.path.dirname(os.path.abspath(__file__))
  
  dir = base + "/ui"
  sys.path.append(dir)

  dir = base + "/form"
  sys.path.append(dir)

  from main import Ui_Main
  from ui_client import Ui_Client

  app = QtGui.QApplication(sys.argv)
  main = Ui_Main()
  sys.exit(app.exec_())
