'''
/Users/judsonbelmont/Documents/Shared_Folders/Mastering-GUI-Programming-with-Python/Chapter03/form_window.py
page 64-66 of Mastering_Gui_Programming with Python by Allan D Moore
THe second program is more basic and introduces the use of 'custom signals' here named 'submitted' 
submitted = qtc.pyqtSignal() is the signal. and in the second window is used to latch onto, bind, the 'edit' (here it is a QLineEdit) and signal.
In the second program the mainWindow Pushbutton calls this from the formWIndow and the created 'submitted' SIGNAL  moves the lineEdit in the FormWindow to the label is the MainWIndow:     self.formwindow.submitted.connect(self.label.setText)     ## It then binds our custom signal,which is ' FormWindow.submitted' in the FormWindow, to the setText slot of the label
 In the first program we have an example of overloading ,  the one value in the  mainWindow function self.change = qtw.QPushButton("Change", clicked=self.onChange)
 uses  @qtc.pyqtSlot() to designate that the function is a slot. and then in the function def
 onSubmit(self) ,once the formWindow has been instantiated. pulls in the fact that in the Form Window , the submitted  slot is syntaxed as an 'overload' (page 64-5).as shown here:  submitted = qtc.pyqtSignal([str], [int, str])
 so when it is pulled back to the mainWIndow. this is taken into account.
'''


import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class FormWindow(qtw.QWidget):

    submitted = qtc.pyqtSignal([str], [int, str])

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.edit = qtw.QLineEdit()
        self.submit = qtw.QPushButton('Submit', clicked=self.onSubmit)

        self.layout().addWidget(self.edit)
        self.layout().addWidget(self.submit)

    def onSubmit(self):
        if self.edit.text().isdigit():
            text = self.edit.text()
            self.submitted[int, str].emit(int(text), text)
        else:
            self.submitted[str].emit(self.edit.text())
        self.close()

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel('Click "change" to change this text.')
        self.change = qtw.QPushButton("Change", clicked=self.onChange)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.change)
        self.show()

    @qtc.pyqtSlot()
    def onChange(self):
        self.formwindow = FormWindow()
        #self.formwindow.submitted.connect(self.label.setText)
        self.formwindow.submitted[str].connect(self.onSubmittedStr)
        self.formwindow.submitted[int, str].connect(self.onSubmittedIntStr)
        self.formwindow.show()

    @qtc.pyqtSlot(str)
    def onSubmittedStr(self, string):
        self.label.setText(string)

    @qtc.pyqtSlot(int, str)
    def onSubmittedIntStr(self, integer, string):
        print(type(integer))
        text = f'The string {string} becomes the number {integer}'
        self.label.setText(text)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
    
'''

pages 64
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc


# class FormWindow(qtw.QWidget): 
#     submitted = qtc.pyqtSignal(str) # page 62 custom signal called submitted. To define a custom signal, we need to call the QtCore.pyqtSignal() function.
#                 # We can use Python type objects here, or strings naming a C++ data type ('QString', for example).
    

#     def __init__(self):
#         """MainWindow constructor.

#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         super().__init__()
#         self.setLayout(qtw.QVBoxLayout())
#         self.edit=qtw.QLineEdit(self)
#         self.edit.setGeometry(10,10,30,150)
#         self.submit = qtw.QPushButton('Submit',clicked = self.onSubmit)
#         self.setWindowTitle('my Chapter 2 Window')
#         self.layout().addWidget(self.edit)
#         self.layout().addWidget(self.submit)
        
#         self.show()
#     def onSubmit(self):
#         print('submit')
#         self.submitted.emit(self.edit.text())
#         self.close()
# # In this method, we call the submitted signal's emit() method, passing in the contents of QLineEdit. This means that any connected slots will be called with the string retrieved from self.edit.text(). After emitting the signal, we close the FormWindow. Down in our MainWindow constructor, let's build an application that uses it:
# class MainWindow(qtw.QWidget):
#     def __init__(self,):
#         super().__init__()
#         self.setWindowTitle('my MainWindow')
#         self.setLayout(qtw.QVBoxLayout())
#         self.label = qtw.QLabel('Click "change" to change this text.') 
#         self.change = qtw.QPushButton("Change", clicked=self.onChange)
#         self.layout().addWidget(self.label)
#         self.layout().addWidget(self.change)
        
#         self.show()
#     ##  my Understanding:  the 'submitted 'signal is in FormWindow and was linked to the onSubmit function to the self.edit  in FormWindow
#     #Here is MainWindow the FormWindow submitted 'signal' is connected to self.label here in the MainWindow
#     ## the key is that 'formwindow' is linked or bound to the 'submitted' signal which is 'connect' to MainWindow's 'label' !!  submitted is a signal in the same way .clicked is for QPushbutton
#     def onChange(self):
#         print('On Change')
#         self.formwindow = FormWindow()  #This method creates an instance of our FormWindow.
#         self.formwindow.submitted.connect(self.label.setText)     ## It then binds our custom signal,which is ' FormWindow.submitted' in the FormWindow, to the setText slot of the label

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
'''
The onChange() method looks like this: def onChange(self): self.formwindow = FormWindow() 
self.formwindow.submitted.connect(self.label.setText) self.formwindow.show() This method creates an instance of our FormWindow. 
It then binds our custom signal, FormWindow.submitted, to the setText slot of the label; 
setText takes a single string for an argument, and our signal sends a single string. If you run this application, you'll see that when you submit the pop-up form window, the text in the label does indeed change
'''

''' Subject of 'OVERLOADING'   page 65-66 Overloading signals and slots Just as C++ signals and slots can be overloaded to accept different argument signatures, we can overload our custom PyQt signals and slots. For instance, suppose that, if a valid integer string is entered into our pop-up window, we'd like to emit it as both a string and an integer. To do this, we first have to redefine our signal: submitted = qtc.pyqtSignal([str], [int, str])'''