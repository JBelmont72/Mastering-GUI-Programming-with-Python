#/Users/judsonbelmont/Documents/Shared_Folders/Mastering-GUI-Programming-with-Python/Create_Gui_App/basic/windows_1.py

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, is_checked):
        w = AnotherWindow()
        w.show()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

## for refernce using for loops to create widgets. /Users/judsonbelmont/Documents/Shared_Folders/PyQt5/LearnerFolder/Py_Tut_1.py

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import sys

class SecondWindow(qtw.QWidget ):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs )
        layout=qtw.QVBoxLayout()
        self.label=qtw.QLabel('this is my label')
        layout.addWidget(self.label)
        self.setLayout(layout)



class MainWindow(qtw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle('my Window')
        self.setGeometry(10,10,400,500)
        layout=qtw.QVBoxLayout()
        PushButton=[]
        for i in range (1,4,1):
            PushButton.append('pushButton'+str(i))
        yellow='red'   
        print(PushButton)
        buttons = [qtw.QPushButton(title) for title in PushButton]
        for idx, button in enumerate(buttons):
            layout.addWidget(button)
            button.setStyleSheet('background-color: ' + yellow + ';')
            # Assign each button as an attribute for later access
            setattr(self, f'button{idx+1}', button)
            if idx == 0:
                button.clicked.connect(self.button1_clicked)
                button.setObjectName('myButton1')
                print(button.objectName())
            elif idx == 1:
                button.clicked.connect(self.button2_clicked)
                button.setObjectName('myButton2')
                print(button.objectName())
            elif idx == 2:
                button.clicked.connect(self.button3_clicked)
        # Example: Access button by object name and do something
        # btn = central_window.findChild(qtw.QPushButton, 'myButton1')
        # if btn:
        #     btn.setText('Found by Name!')
                    
        layout.addStretch()
        central_window = qtw.QWidget()
        central_window.setLayout(layout)
        self.setCentralWidget(central_window)
        btn = central_window.findChild(qtw.QPushButton, 'myButton1')
        if btn:
            btn.setText('Found by Name!')
 
        btn2 = central_window.findChild(qtw.QPushButton, 'myButton2')
        if btn2:
            btn2.clicked.connect(self.open_second_window)

    def open_second_window(self):
        self.second = SecondWindow()
        self.second.show()
    # Example button click handlers
    def button1_clicked(self):
        print("Button 1 clicked")

    def button2_clicked(self):
        print("Button 2 clicked")

    def button3_clicked(self):
        print("Button 3 clicked")
    # def button4_clicked(self): # My mistake was not to make 'self'
    #     print("Button 4 clicked")        
    #     second=SecondWindow()
    #     second.show()
        

if __name__ == '__main__':
    app =qtw.QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())
    
