import sys

# from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
app = qtw.QApplication(sys.argv) # QApplication([]) is also valid
app.setApplicationName('Hello Qt')
## any widget can be a window but not all widgets are windows, not very useful to have only one widget
# window = qtw.QWidget()
# window=qtw.QPushButton('Hello World')
window=qtw.QTextEdit('Hello World')
window.show()
app.exec()
