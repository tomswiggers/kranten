from PySide import QtCore, QtGui

if __name__ == "__main__":
  import os, sys
  
  base = os.path.dirname(os.path.abspath(__file__))
  
  dir = base + "/ui"
  sys.path.append(dir)

  dir = base + "/form"
  sys.path.append(dir)

  from ui import Ui
  from ui_window import Ui_Window
  from ui_main import Ui_Main

  app = QtGui.QApplication(sys.argv)
  window = Ui_Window()
  main = Ui_Main(window)
  sys.exit(app.exec_())
