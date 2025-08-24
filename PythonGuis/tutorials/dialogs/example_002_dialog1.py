# import sys

# from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)

#     def button_clicked(self, s):
#         print("click", s)

#         dlg = QDialog(self)
#         dlg.setWindowTitle("HELLO!")
#         dlg.exec()


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QDialog,QVBoxLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('my MainWindow')
        self.setGeometry(10,10,400,300)
        layout=QVBoxLayout()
        self.button= QPushButton('Press me for Dialog Widget')
        layout.addWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect( lambda : self.button_clicked(1))
        
        
        
        
        central_widget=QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def button_clicked(self,s):
        print(s)
        dlg =QDialog(self)
        dlg.setWindowTitle(f'my Dialog Guis {s}')
        dlg.setGeometry(10,10,300,400)
        dlg.exec()


if __name__=='__main__':
    app = QApplication(sys.argv)
    w=MainWindow()
    w.show()
    sys.exit(app.exec_())