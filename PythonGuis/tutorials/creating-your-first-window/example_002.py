# import sys

# from PyQt5.QtCore import QSize
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press Me!")

#         self.setFixedSize(QSize(400, 300))

#         self.setCentralWidget(button)


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
###############
# import sys
# # from PyQt5.QtCore import QSize
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc
# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = qtw.QPushButton("Press Me!")

#         self.setFixedSize(qtc.QSize(400, 300))

#         self.setCentralWidget(button)


# app = qtw.QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
# import sys
# # from PyQt5.QtCore import QSize
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc
# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = qtw.QPushButton("Press Me!")

#         self.setFixedSize(qtc.QSize(400, 300))

#         self.setCentralWidget(button)


# app = qtw.QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
####### convert to QWidget
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         self.layout = qtw.QVBoxLayout(self)  # Main layout for the QWidget

#         # Create widgets
#         button = qtw.QPushButton("Press Me!")
#         button.setToolTip("This is a tooltip")  # Set tooltip for the buttonbutton
#         lineEdit = qtw.QLineEdit(self)
#         lineEdit.setPlaceholderText("Enter text here")
#         # lineEdit.setStyleSheet("background-color: lightyellow;")  # Commented out
#         # button.setStyleSheet("background-color: lightblue;")  # Commented out
#         button.setCursor(qtc.Qt.PointingHandCursor)
#         button2 = qtw.QPushButton("Press Me Also!")
#         # button2.setStyleSheet("background-color: lightgreen;")  # Commented out
#         button2.setCursor(qtc.Qt.PointingHandCursor)
#         button2.setToolTip("This is another tooltip")  # Set tooltip for the button2
#         self.layout.addWidget(button)
#         self.layout.addWidget(button2)
#         self.layout.addWidget(lineEdit)
#         self.layout.addStretch()

#         # Set the layout for the QWidget
#         self.setLayout(self.layout)
#         self.adjustSize()  # Adjust the size of the window to fit its contents

# app = qtw.QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
#####
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: lightblue;")
        self.setCursor(qtc.Qt.PointingHandCursor)
        button =qtw.QPushButton("Press Me!")
        button.setToolTip("This is a tooltip")
        # self.setFixedSize(qtc.QSize(400, 300))
        self.setMinimumSize(qtc.QSize(400, 300))  # Set minimum size
        self.setMaximumSize(qtc.QSize(800, 600))
        self.setCentralWidget(button)
        self.show()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())