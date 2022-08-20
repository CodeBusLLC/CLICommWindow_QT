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

  def doFind(self,aString, aNext):
    if False == aNext:
      cursor_ = self.textCursor()
      cursor_.movePosition( QtGui.QTextCursor.Start )
      self.setTextCursor(cursor_)
    self.find(aString)
    cursor_ = self.textCursor()
    print( cursor_.selectedText() )
    fmt_ = cursor_.charFormat()
    fmt_.setBackground(QtCore.Qt.yellow)
    fmt_.setBackground(QtCore.Qt.yellow) 
    cursor_.setCharFormat(fmt_)
    