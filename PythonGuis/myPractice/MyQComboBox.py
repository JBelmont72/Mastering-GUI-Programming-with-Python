## https://www.pythonguis.com/docs/qcombobox/

# The error in your code is that you are trying to set a layout directly on the `QMainWindow` using `self.setLayout(layout)`, which is not allowed. Instead, you should set the layout on a central widget and then set that widget as the central widget of the `QMainWindow`.



# Made changes.

#Version 1
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# import sys


# class MyQComboBox(qtw.QMainWindow):
#     def __init__(self, parent=None):
#         super(MyQComboBox, self).__init__(parent)
#         self.setWindowTitle("My QComboBox Example")
#         self.setGeometry(100, 100, 300, 200)

#         # Create a QComboBox
#         self.combo = qtw.QComboBox(self)
#         self.combo.addItem("Option 1")
#         self.combo.addItem("Option 2")
#         self.combo.addItem("Option 3")
#         self.combo.move(50, 50)

#         # Connect the signal to a slot
#         self.combo.activated[str].connect(self.on_combobox_changed)


#         # You can also use the currentIndexChanged signal to get the index of the selected item
#         central_widget = qtw.QWidget()
        
#         layout= qtw.QVBoxLayout(central_widget)## option 1:This is an alternative to next three lines
        
#         # # option 2: Create a central widget and set its layout with combo box inside it.This is an alternative to layout= qtw.QVBoxLayout(central_widget)!!!!!!
#         # layout = qtw.QVBoxLayout()
#         # # Create a vertical layout and add the combobox to it
#         # layout.addWidget(self.combo)
#         # # Set the layout on the central widget
#         # central_widget.setLayout(layout)
#         # # Set the central widget for the main window     
#         # # Add the QComboBox to the layout
#         lineEdit = qtw.QLineEdit()
#         # Add the QLineEdit to the layout
#         subLayout = qtw.QHBoxLayout()
#         pushButton = qtw.QPushButton("Push Me")
#         # Add the QLineEdit to the subLayout
#         subLayout.addWidget(pushButton)
#         subLayout.addWidget(lineEdit)
#         # Add the subLayout to the main layout
#         layout.addLayout(subLayout)
        
#         layout.addWidget(self.combo)
#         # Set the layout on the central widget
#         self.setCentralWidget(central_widget)
#         # Set the central widget for the main window
  
   
        
#         self.show()
#         # Set the main window's layout
#     def on_combobox_changed(self, text):
#         """Slot to handle the QComboBox selection change."""
#         print(f"Selected option: {text}")
#         # You can add more logic here based on the selected option
#         # For example, you could update other UI elements or perform actions
#         # based on the selected option.
# if __name__=='__main__':
#     app=qtw.QApplication(sys.argv)
#     window = MyQComboBox()
#     sys.exit(app.exec_())
    
##version 2   
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# import sys

# class MyQComboBox(qtw.QMainWindow):
#     def __init__(self, parent=None):
#         super(MyQComboBox, self).__init__(parent)
#         self.setWindowTitle("My QComboBox Example")
#         self.setGeometry(100, 100, 300, 200)

#     #     # Create a QComboBox and add options to it
#     #     self.combo = qtw.QComboBox()
#     #     self.combo.addItem("Option 1")
#     #     self.combo.addItem("Option 2")
#     #     self.combo.addItem("Option 3")

#     #     # Connect the signal to a slot
#     #     self.combo.activated[str].connect(self.on_combobox_changed)

#     #    # Create a central widget and set its layout with combo box inside it.
#     #     central_widget = qtw.QWidget()  # step 1: create an instance of QWidget named central_widget
#     #     layout = qtw.QVBoxLayout(central_widget)  # step2 : Create a vertical layout and add the combobox to it, then assign this layout to the central widget.
#     #     layout.addWidget(self.combo)
#     #     self.setCentralWidget(central_widget)   #step3: Set the main window's central widget
#     #    # Show the main window
#         self.show()
#     def on_combobox_changed(self, text):
#         """Slot to handle the QComboBox selection change."""
#         print(f"Selected option: {text}")
#         # You can add more logic here based on the selected option...
# if __name__=='__main__':
#     app=qtw.QApplication(sys.argv)
#     window = MyQComboBox()
#     sys.exit(app.exec_())
###19 May2025
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()
# # class MyQComboBox(qtw.QMainWindow):
# #     def __init__(self, parent=None):
# #         super(MyQComboBox, self).__init__(parent)
#         self.setWindowTitle("My QComboBox Example")
#         self.setGeometry(100, 100, 300, 200)
#         ## create a combo box
#         myCombo=qtw.QComboBox()
        
  
#         ## create a central_widget
#         # central_widget=qtw.QDockWidget() ## interesting Widget
#         central_widget =qtw.QWidget()
#         layout=qtw.QVBoxLayout(central_widget)
        
#         layout.addWidget(myCombo)
#         self.setCentralWidget(central_widget)
#         lineEdit =qtw.QLineEdit()
#         layout.addWidget(lineEdit)

        
        
#         self.show()
        
# if __name__ == '__main__':
#     app= qtw.QApplication(sys.argv)
#     window= MainWindow()
#     sys.exit(app.exec_())       
## multiple ways to create comboBoxs   
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QMainWindow):

#     def __init__(self):
#         """MainWindow constructor.

#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         super().__init__()
#         # Main UI code goes here

#         # End main UI code
#         self.show()

#         combobox1 = qtw.QComboBox()
#         combobox1.addItem('One')
#         combobox1.addItem('Two')
#         combobox1.addItem('Three')
#         combobox1.addItem('Four')

#         combobox2 = qtw.QComboBox()
#         combobox2.addItems(['One', 'Two', 'Three', 'Four'])

#         combobox3 = qtw.QComboBox()
#         combobox3.addItems(['One', 'Two', 'Three', 'Four'])
#         combobox3.insertItem(2, 'Hello!')

#         combobox4 = qtw.QComboBox()
#         combobox4.addItems(['One', 'Two', 'Three', 'Four'])
#         combobox4.insertItems(2, ['Hello!', 'again'])

#         combobox5 = qtw.QComboBox()
#         icon_penguin = qtg.QIcon('PythonGuis/demos/paint/icons/pencil.png')
#         icon_monkey = qtg.QIcon('PythonGuis/demos/paint/icons/piecasso.ico')
#         icon_bauble = qtg.QIcon('PythonGuis/demos/paint/icons/selection.png')
#         combobox5.addItem(icon_penguin, 'Linux')
#         combobox5.addItem(icon_monkey, 'Monkeyix')
#         combobox5.insertItem(1, icon_bauble, 'Baublix')

#         layout = qtw.QVBoxLayout()
#         layout.addWidget(combobox1)
#         layout.addWidget(combobox2)
#         layout.addWidget(combobox3)
#         layout.addWidget(combobox4)
#         layout.addWidget(combobox5)

#         central_widget = qtw.QWidget()
#         central_widget.setLayout(layout)

#         self.setCentralWidget(central_widget)

#     def current_text_changed(self, s):
#         print("Current text: ", s)






# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
# QComboBox signals
# The QComboBox emits a number of signals on state changes. When the currently selected item changes, the widget emits .currentIndexChanged() and .currentTextChanged() signals. The first receives the index of the selected entry while the second receives the text of that item. There is a further signal .activated() which is emitted for user-selections whether the index is changed or not: selecting the same entry again will still emit the signal. Highlighting an entry in the QComboBox popup list will emit the .highlighted() signal.

# The following example demonstrates these signals in action.
# from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication
# import sys


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.combobox = QComboBox()
#         self.combobox.addItems(['One', 'Two', 'Three', 'Four','Clear'])

#         # Connect signals to the methods.
#         self.combobox.activated.connect(self.activated)
#         self.combobox.currentTextChanged.connect(self.text_changed)
#         self.combobox.currentIndexChanged.connect(self.index_changed)
        
        
#         self.setCentralWidget(self.combobox)

#     def activated(Self, index):
#         print("Activated index:", index)

#     def text_changed(self, s):
#         if s =='Clear':
#             self.combobox.clear()
#             self.setWindowTitle('I just cleared it')
#         print("Text changed:", s)

#     def index_changed(self, index):
#         print("Index changed", index)
        

# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec_()
####
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('my combo box')
#         ## create combo Box
#         self.combo=qtw.QComboBox()

#         self.combo.addItem("Option 1")
#         self.combo.addItem("Option 2")
#         self.combo.addItem("Option 3")


        
#         ## create central_widget
#         central_widget =qtw.QWidget()
#         layout=qtw.QHBoxLayout(central_widget)
#         layout.addWidget(self.combo)
        
#         ## add a horizontal layout to layout
#         h_layout = qtw.QHBoxLayout()
#         layout.addLayout(h_layout)
#         # created a pushButton and added it to h_layout
#         self.push=qtw.QPushButton('push me')
#         h_layout.addWidget(self.push)
        
        
#         layout.addWidget(central_widget)
#         self.setCentralWidget(central_widget)
        
        
# if __name__ == '__main__':
#     app =qtw.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

### 22 may 2025
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle('My Combo')
        # self.setGeometry(600,800)
        


        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())