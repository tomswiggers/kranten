from PySide import QtCore, QtGui

if __name__ == "__main__":
  import os, sys
 
  os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

  from django.db import models
  from django.core.management import call_command

  base = os.path.dirname(os.path.abspath(__file__))
  
  dir = base + "/ui"
  sys.path.append(dir)

  dir = base + "/form"
  sys.path.append(dir)

  from ui_window import Ui_Window

  app = QtGui.QApplication(sys.argv)
  window = Ui_Window()
  window.showFrame("Ui_Main")

  sys.exit(app.exec_())
