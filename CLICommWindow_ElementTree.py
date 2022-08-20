from PySide6 import QtCore, QtWidgets, QtGui
import CLICommWindow_Yaml

class ElementTree(QtWidgets.QTreeWidget):
  inst = None
  def __init__(self, aLayout, aOwner):
    super().__init__()
    ElementTree.inst = self
    self.owner = aOwner
    self.found = None
    columns_ = ("Category", "Group", "Element", "Help")
    colWidth_=( 100, 120, 160, 350 )
    l_ = QtWidgets.QHBoxLayout()
    l_.addWidget(self)
    self.setColumnCount(len(columns_))
    for i_ in range(0, len(columns_)):
      self.setColumnWidth(i_, colWidth_[i_])
    self.setHeaderItem(QtWidgets.QTreeWidgetItem(columns_))
    aLayout.addLayout(l_, 0, 0)
    CLICommWindow_Yaml.LoadData_Yaml(self,'elements.yaml')
    
    self.popupItem = None
    self.popup = QtWidgets.QMenu()
    self.popup.addAction("Send", self.doSend)
    # Connect the contextmenu
    self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.customContextMenuRequested.connect(self.menuContextTree)


  def menuContextTree(self, point):
    # Infos about the node selected.
    item_ = self.itemAt(point)
    if item_:
      self.popupItem = item_
      self.popup.exec(self.mapToGlobal(point))


  def addTop(self, aValue, aColumns):
    item_ = QtWidgets.QTreeWidgetItem(aColumns)
    item_.setData(0, QtCore.Qt.UserRole, aValue)
    #self.itemDoubleClicked.connect(self.doDblClick)
    self.addTopLevelItem(item_)
    return item_
    
  def addGroup( self, aParent, aColumns):
    item_ = QtWidgets.QTreeWidgetItem( aParent, aColumns )
    return item_

  def addChild( self, aParent, aValue, aColumns):
    item_ = QtWidgets.QTreeWidgetItem( aParent, aColumns )
    self.itemDoubleClicked.connect(self.doDblClick)
    item_.setData(0, QtCore.Qt.UserRole, aValue)

  def _getData(self, aItem):
    ret_ = None
    value_ = aItem.data(0, QtCore.Qt.UserRole )
    if value_:
      parent_ = aItem.parent()
      parentValue_ = parent_.data(0, QtCore.Qt.UserRole )
      if parentValue_ == None:
        parent_ = parent_.parent()
        if parent_:
          parentValue_ = parent_.data(0, QtCore.Qt.UserRole )
          
      if parentValue_ != None:
        ret_ = "%s %s" % (parentValue_, value_ )
    return ret_

  def doDblClick(self, aItem):
    ret_ = self._getData(aItem)
    if ret_:
      self.owner.entrybar.setValue( ret_ )
    
  def doSend(self):
    ret_ = self._getData(self.popupItem)
    if ret_:
      self.owner.entrybar.setValue( ret_ )
  
  def _searchChildren(self, aItem, aString):
    if aItem.childCount() > 0:
      for idx_ in range(0, aItem.childCount()):
        child_ = aItem.child(idx_)
        if child_.text(2).__contains__( aString ):
          self.found = child_
          print( child_.text(2) )
          break
        self._searchChildren( child_, aString )
  
  def doSearch(self,aString, aNext):
    if False == aNext:
      for idx_ in range(0, self.topLevelItemCount()):
        print( self.topLevelItem(idx_).text(0) )
        self._searchChildren( self.topLevelItem(idx_), aString )
        if self.found:
          break
        

