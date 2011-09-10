from PySide import QtCore, QtGui

class Ui_Client_View(QtGui.QWidget):
  def __init__(self, mainWindow, parentWindow):
    super(Ui_Client_View, self).__init__(mainWindow)
    
    self.mainWindow = mainWindow
    self.parentWindow = parentWindow
    
    self.showView()
    self.show()

  def createSearchForm(self):
    self.clientNumber = QtGui.QLineEdit()
    self.searchButton = QtGui.QPushButton("zoek")

    self.searchButton.clicked.connect(self.search)

    layoutSearch = QtGui.QHBoxLayout()
    layoutSearch.addWidget(QtGui.QLabel("Klantnummer"))
    layoutSearch.addWidget(self.clientNumber)
    layoutSearch.addWidget(self.searchButton)
 
    return layoutSearch

  def showView(self):
    layout = QtGui.QVBoxLayout()
    layout.addLayout(self.createSearchForm())

    self.setLayout(layout)

  def showMainWindow(self):
    self.hide()
    self.mainWindow.main.show()

  def search(self):
    print "search"
