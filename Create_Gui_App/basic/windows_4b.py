# import sys
# from random import randint

# from PyQt5.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )


# class AnotherWindow(QWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window.
#     """

#     def __init__(self):
#         super().__init__()
#         layout = QVBoxLayout()
#         self.label = QLabel("Another Window % d" % randint(0, 100))
#         layout.addWidget(self.label)
#         self.setLayout(layout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.w = None  # No external window yet.
#         self.button = QPushButton("Push for Window")
#         self.button.clicked.connect(self.show_new_window)
#         self.setCentralWidget(self.button)

#     # tag::show_new_window[]
#     def show_new_window(self, is_checked):
#         if self.w is None:
#             self.w = AnotherWindow()
#             self.w.show()

#         else:
#             self.w.close()
#             self.w = None  # Discard reference, close window.

#     # end::show_new_window[]


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec_()


from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys
class SecondWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        layout =qtw.QVBoxLayout() 
        label=qtw.QLabel('my label')
        
        layout.addWidget(label)
        self.setLayout(layout)
        
class MainWindow(qtw.QMainWindow):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.w=SecondWindow()
        self.setGeometry(10,10,400,500)
        self.setWindowTitle('My Window')
        self.setStyleSheet('background-color:magenta;')
        layout=qtw.QHBoxLayout()
        color='red'
        PushButton=[]
        for i in range(1,4,1):      ## make the names for buttons
            PushButton.append('pushButton'+str(i))
        print(PushButton)
        buttons =[qtw.QPushButton(idx,self)for idx in PushButton]    ## create the button objects
        for idx,btn in enumerate(buttons):  ## instantiate the btns and set up as an attribute
            print(idx,btn)
            layout.addWidget(btn)
            btn.setStyleSheet(f'background-color:{color};')
            btn.setCheckable(True)
            ## assign each button as an attribute for later access
            #specified value setattr(x,'y',v is equivalent to ''x.y =v''))
            setattr(self,f'myButton{str(idx+1)}',btn)
            if idx == 0:
                btn.clicked.connect(self.click_1)
            if idx ==1:
                btn.clicked.connect(self.openSecondWindow)
                    
        central_window=qtw.QWidget()
        central_window.setLayout(layout)
        self.setCentralWidget(central_window)
        

        
                     
    def click_1(self,is_clicked):
        print('clicked',is_clicked)     
    def openSecondWindow(self,checked):
        print(checked)
        if self.w. isVisible():
            self.w.hide()
        else:
            self.w.show()
if __name__ == '__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    
'''In this example, setattr() is used to set the placeholderText attribute of two QLineEdit widgets dynamically, demonstrating its utility in a PyQt5 application.'''   
# from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
# import sys

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("setattr() in PyQt5")
#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)

#         self.line_edit1 = QLineEdit()
#         self.layout.addWidget(self.line_edit1)

#         self.line_edit2 = QLineEdit()
#         self.layout.addWidget(self.line_edit2)

#         # Dynamically set a placeholder text using setattr()
#         attribute_name = "placeholderText"
#         value_for_edit1 = "Enter text here (dynamic)"
#         value_for_edit2 = "Another dynamic placeholder"

#         setattr(self.line_edit1, attribute_name, value_for_edit1)
#         setattr(self.line_edit2, attribute_name, value_for_edit2)
#         self.line_edit1.setPlaceholderText(value_for_edit1)
#         self.line_edit2.setPlaceholderText(value_for_edit2)
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())
'''The setattr() function in Python is a built-in utility that allows for dynamic attribute assignment to objects. While it's a general Python function, its application in PyQt5 contexts is identical to its use with any other Python object. 
Purpose in PyQt5:
You would use setattr() in PyQt5 when you need to dynamically set attributes of PyQt5 widgets or other Qt objects, especially when the attribute name is not known until runtime. This can be useful in scenarios such as:
Programmatically configuring UI elements:
.
If you have a list of attribute names (e.g., from a configuration file or user input) and their corresponding values that you want to apply to a widget, setattr() allows you to do this without hardcoding each attribute assignment.
Creating dynamic UI components:
.
When building a UI where the properties of widgets might change based on user interaction or data, setattr() can be used to update these properties on the fly.
Implementing generic attribute manipulation:
.
In frameworks or tools that interact with PyQt5 widgets, setattr() can provide a flexible way to manage and modify object attributes generically.
'''