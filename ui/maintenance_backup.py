from datetime import datetime 

from PySide import QtCore, QtGui
from ui import Ui
from config import Config

class Ui_Maintenance_Backup(Ui):
  dirname = ""

  def __init__(self, window):
    super(Ui_Maintenance_Backup, self).__init__(window)

  def getDirname(self):
    dirname = QtGui.QFileDialog.getExistingDirectory()
    self.dirname.setText(dirname)

  def createButtonDirname(self):
    btn = QtGui.QPushButton('Selecteer folder', self)
    btn.setToolTip('Selecteer een folder waar de backup opgeslagen moet worden.')
    btn.clicked.connect(self.getDirname)

    return btn

  def createFieldDirname(self):
    self.dirname = QtGui.QLineEdit()
    return self.dirname

  def createButtonBackup(self):
    btn = QtGui.QPushButton('Backup maken', self)
    btn.setToolTip('Een backup aanmaken.')
    btn.clicked.connect(self.createBackup)

    return btn

  def createButtonBack(self):
    back = QtGui.QPushButton('Terug', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMaintenance)

    return back

  def createButtonMain(self):
    back = QtGui.QPushButton('Terug naar hoofdmenu', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMain)

    return back

  def init(self):
    layout = QtGui.QVBoxLayout()
    layoutButtons = QtGui.QVBoxLayout()
    layoutMessage = QtGui.QHBoxLayout()

    layoutMessage.addWidget(self.createMessage())

  
    layoutDirname = QtGui.QHBoxLayout()
    layoutDirname.addWidget(self.createFieldDirname())
    layoutDirname.addWidget(self.createButtonDirname())
    
    layoutButtons.addLayout(layoutDirname)
    layoutButtons.addWidget(self.createButtonBackup())
    layoutButtons.addWidget(self.createButtonBack())
    layoutButtons.addWidget(self.createButtonMain())

    layout.addLayout(layoutMessage)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

  def getCurrentTimeFormat(self):
    d = datetime.now()
    return d.strftime('%m%d%H%M%S')

  def createBackup(self):
    import shutil

    shutil.copy(Config.dbFilename, self.dirname.text() + "/backup-" + Config.dbName)
    shutil.copy(Config.dbFilename, Config.dirBackup + "/" + self.getCurrentTimeFormat() + "-" + Config.dbName)
