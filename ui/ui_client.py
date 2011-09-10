from PySide import QtCore, QtGui

class Ui_Client(QtGui.QWidget):
  buttonWidth = 200

  def __init__(self, mainWindow):
    super(Ui_Client, self).__init__(mainWindow)
    self.mainWindow = mainWindow
    self.showClient()

  def setMinimumWidthButton(self, button):
    button.setMinimumWidth(self.buttonWidth)

  def createButtonNew(self):
    new = QtGui.QPushButton('Nieuw', self)
    new.setToolTip('Klanten aanmaken/bewerken')
    new.clicked.connect(self.showNew)

    return new

  def createButtonView(self):
    edit = QtGui.QPushButton('Raadpleeg', self)
    edit.setToolTip('Gegevens van een klant raadplegen')
    edit.clicked.connect(self.showView)

    return edit

  def createButtonEdit(self):
    edit = QtGui.QPushButton('Wijzig', self)
    edit.setToolTip('Gegevens van een klant wijzigen')
    edit.clicked.connect(self.showEdit)

    return edit

  def createButtonBack(self):
    back = QtGui.QPushButton('Terug', self)
    back.setToolTip('Ga terug naar het hoofdmenu')
    back.clicked.connect(self.showMain)

    return back

  def createMessage(self):
    self.message = QtGui.QLabel()
    self.message.setMinimumWidth(400)

    return self.message

  def showClient(self):
    layout = QtGui.QVBoxLayout()
    layoutButtons = QtGui.QVBoxLayout()
    layoutMessage = QtGui.QHBoxLayout()

    layoutMessage.addWidget(self.createMessage())

    layoutButtons.addWidget(self.createButtonNew())
    layoutButtons.addWidget(self.createButtonView())
    layoutButtons.addWidget(self.createButtonEdit())
    layoutButtons.addWidget(self.createButtonBack())

    layout.addLayout(layoutMessage)
    layout.addLayout(layoutButtons)

    self.setLayout(layout)

    self.show()

  def showMain(self):
    self.hide()
    self.mainWindow.main.show()

  def showNew(self):
    import os, sys

    dir = os.path.dirname(os.path.abspath(__file__))
    dir += "/ui"
    sys.path.append(dir)

    from client_new import Ui_Client_New

    client = Ui_Client_New(self.mainWindow, self)
    self.hide()
    self.mainWindow.main.hide()
 
  def showEdit(self):
    print "show_edit"

  def setMessage(self, message):
    self.message.setText(message)

  def showView(self):
    import os, sys

    dir = os.path.dirname(os.path.abspath(__file__))
    dir += "/ui"
    sys.path.append(dir)

    from client_view import Ui_Client_View

    client = Ui_Client_View(self.mainWindow, self)
    self.hide()
    self.mainWindow.main.hide()
 
