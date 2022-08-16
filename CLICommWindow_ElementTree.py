from PySide6 import QtCore, QtWidgets, QtGui
import CLICommWindow_Yaml

class ElementTree(QtWidgets.QTreeWidget):
  def __init__(self, aLayout, aOwner):
    super().__init__()
    self.owner = aOwner
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

  def addTop(self, aValue, aColumns):
    item_ = QtWidgets.QTreeWidgetItem(aColumns)
    item_.setData(0, QtCore.Qt.UserRole, aValue)
    self.itemDoubleClicked.connect(self.doDblClick)
    self.addTopLevelItem(item_)
    return item_
    
  def addChild( self, aParent, aValue, aColumns):
    item_ = QtWidgets.QTreeWidgetItem( aParent, aColumns )
    item_.setData(0, QtCore.Qt.UserRole, aValue)
    return item_

  def doDblClick(self, aItem):
    value_ = aItem.data(0, QtCore.Qt.UserRole )
    self.owner.entrybar.setValue( value_ )
    
    