from PySide import QtCore, QtGui

if __name__ == "__main__":
  import os, sys
 
  os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

  from django.db import models
  from django.core.management import call_command

  from ui.window  import Ui_Window

  app = QtGui.QApplication(sys.argv)
  window = Ui_Window()
  window.showFrame("Ui_Main")

  sys.exit(app.exec_())
