
'''
https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python/tree/master
basic steps:  p 34 
1.Create a QApplication object. 
2.Create our main application window. 
3.Display our main application window
4. Call QApplication.exec() to start the event loop
first is basic elements, second refined to class structure

uv pip install -r requirements.txt || uv pip install --upgrade --all
'''

# from PyQt5 import QtWidgets

# app = QtWidgets.QApplication([])
# window = QtWidgets.QWidget(windowTitle='Hello Qt')
# window.show()
# app.exec()

from PyQt5.QtWidgets import QWidget,QApplication
import sys
from PyQt5 import QtCore as qtc
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('my Widget')
        self.show()


if __name__ == '__main__':
    app= QApplication(sys.argv)
    window = MainWindow()
    # window = QWidget(cursor=qtc.Qt.CursorShape(3))## uses enum values to pick pointer.cool 
    window = QWidget(cursor=qtc.Qt.ArrowCursor)## uses enum values to pick pointer.cool 
    # window.setWindowFlags(qtc.Qt.Sheet|qtc.Qt.Popup)
    window.show()
    sys.exit(app.exec_())


