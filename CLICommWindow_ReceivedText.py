from PySide6 import QtCore, QtWidgets, QtGui

class ReceivedText(QtWidgets.QTextEdit):
  inst = None
  def __init__(self, aLayout):
    super().__init__()
    ReceivedText.inst = self
    l_ = QtWidgets.QHBoxLayout()
    l_.addWidget(self)
    aLayout.addLayout(l_, 2, 0)

  def append(self, aString):
    curs_ = QtGui.QTextCursor(self.document())
    curs_.movePosition(QtGui.QTextCursor.End)
    curs_.insertText(aString)

  def doFind(self,aString):
    self.find(aString)
    print( self.textCursor().selectedText() )