from PySide6 import QtCore, QtWidgets, QtGui
import serial
from serial.tools.list_ports import comports

class CLICommWindow_DlgConnect(QtWidgets.QDialog):
  def __init__(self, aParent):
    QtWidgets.QDialog.__init__(self)
    self.parent = aParent
    self.setModal(True)
    self.setMinimumWidth(250)
    self.strPortSelected = None
    l_ = QtWidgets.QVBoxLayout()
    self.cbPorts = QtWidgets.QComboBox()
    l_.addWidget(self.cbPorts)
    btn_ = QtWidgets.QPushButton('Connect')
    btn_.clicked.connect(self.portSelected)
    l_.addWidget(btn_)
    self.setLayout(l_)
    
    portlist = comports()
    for i_ in range(0, len(portlist)):
      str_ = "%s (%s)" % (portlist[i_].name, portlist[i_].description)
      #print( str_ )
      self.cbPorts.addItem( str_ )
      
  def portSelected(self):
    self.strPortSelected = self.cbPorts.currentText().split()[0]
    #print( self.strPortSelected )
    self.done(0)
