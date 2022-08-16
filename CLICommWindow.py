import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

import CLICommWindow_Reader
import CLICommWindow_Menu
import CLICommWindow_ElementTree
import CLICommWindow_EntryBar
import CLICommWindow_ReceivedText
    
class MainWindow(QtWidgets.QMainWindow):
  strTitle="CLI Comm Window 0.1"
  def __init__(self, aApp):
    QtWidgets.QMainWindow.__init__(self)
    self.app = aApp
    self.setTitle("")
    self.resize(800, 600)
    
    self.menu = CLICommWindow_Menu.CLICommWindow_Menu(self)
    top = QtWidgets.QWidget()
    layout_ = QtWidgets.QGridLayout(top)
    self.tree = CLICommWindow_ElementTree.ElementTree(layout_, self)
    self.entrybar = CLICommWindow_EntryBar.EntryBar(layout_, self)
    self.recvdText = CLICommWindow_ReceivedText.ReceivedText(layout_)
    self.reader = CLICommWindow_Reader.CLICommWindow_Reader(self)
    self.setCentralWidget(top)

  def setTitle(self, aString):
    self.setWindowTitle( "%s %s" % (MainWindow.strTitle, aString) )
    
  def connected(self, aConnected, aPort):
    #print( aConnected, aPort )
    str_ = ""
    if aConnected:
      str_ = "- %s" % (aPort)
    self.setTitle(str_)
    
  def closeEvent(self, aEvent):
    #print('closing')
    self.reader.stop()
  
  def doExit(self):
    self.reader.stop()
    self.close()
  
  def processText(self, aString):
    self.recvdText.append(aString)
  
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow(app)
    widget.show()

    sys.exit(app.exec())
