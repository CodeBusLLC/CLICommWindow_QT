from PySide6 import QtCore, QtWidgets, QtGui

class EntryBar():
  def __init__(self, aLayout, aOwner):
    self.owner = aOwner
    l_ = QtWidgets.QHBoxLayout()
    btn = QtWidgets.QPushButton('Send')
    btn.clicked.connect(self.doSend)
    self.entry = QtWidgets.QLineEdit('test')
    l_.addWidget(btn)
    l_.addWidget(self.entry)
    aLayout.addLayout(l_, 1, 0)

  def doSend(self):
    #print( self.entry.text() )
    self.owner.reader.send( self.entry.text() )
    
  def setValue(self, aString):
    self.entry.setText(aString)
    