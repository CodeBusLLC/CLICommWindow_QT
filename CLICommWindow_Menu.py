from PySide6 import QtCore, QtWidgets, QtGui
import CLICommWindow_DlgConnect
import CLICommWindow_DlgSearch
import CLICommWindow_ReceivedText
import CLICommWindow_ElementTree

class CLICommWindow_Menu():
  def __init__(self, aOwner):
    self.menu = aOwner.menuBar()
    self.owner = aOwner
    
    filemenu = self.menu.addMenu( "File" )
    
    actConnect = QtGui.QAction( "Connect", aOwner )
    actConnect.triggered.connect( self.doConnect )
    filemenu.addAction( actConnect )
    
    actConnect = QtGui.QAction( "Disconnect", aOwner )
    actConnect.triggered.connect( self.doConnect )
    filemenu.addAction( actConnect )
    
    actConnect = QtGui.QAction( "Reconnect", aOwner )
    actConnect.triggered.connect( self.doConnect )
    filemenu.addAction( actConnect )
    
    filemenu.addSeparator()

    actConnect = QtGui.QAction( "Exit", aOwner )
    actConnect.triggered.connect( self.owner.doExit )
    filemenu.addAction( actConnect )

    searchmenu = self.menu.addMenu( "Search" )
    
    act_ = QtGui.QAction( "Element Tree", aOwner )
    act_.triggered.connect( self.doSearchTree )
    searchmenu.addAction( act_ )
    
    act_ = QtGui.QAction( "Received Text", aOwner )
    act_.triggered.connect( self.doSearchRecvd )
    searchmenu.addAction( act_ )
    
  def doConnect(self):
    dlg_ = CLICommWindow_DlgConnect.CLICommWindow_DlgConnect(self)
    if 0 == dlg_.exec() and dlg_.strPortSelected:
      self.owner.reader.openConnection(dlg_.strPortSelected)
    
  def doDisconnect(self):
    pass

  def doReconnect(self):
    pass

  def doSearchTree(self):
    dlg_ = CLICommWindow_DlgSearch.CLICommWindow_DlgSearch(self.owner, CLICommWindow_ElementTree.ElementTree.inst )

  def doSearchRecvd(self):
    dlg_ = CLICommWindow_DlgSearch.CLICommWindow_DlgSearch(self.owner, CLICommWindow_ReceivedText.ReceivedText.inst )
    