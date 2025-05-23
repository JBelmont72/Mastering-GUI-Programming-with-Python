# You can connect as many slots to a signal as you like and can respond to different versions of signals at the same time on your slots.


import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("My App")

        self.button = QPushButton("Press me")
        self.button.setCheckable(True)
        # button.clicked.connect(self.button_clicked)
        self.button.released.connect( lambda:self.the_button_was_released())
        # self.button.released.connect( self.the_button_was_released)
        
        # button.clicked.connect(self.button_pressed)
        self.setCentralWidget(self.button)
        self.show
    def the_button_was_released(self):
        print("click")
        self.button_is_checked = self.button.isChecked()
        print("Button is checked:", self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
# import sys

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         button.clicked.connect(lambda: self.button_clicked("Hello!"))
#         button.clicked.connect(self.button_pressed)
#         self.setCentralWidget(button)

#     def button_clicked(self, s):
#         pass
#         # print("click", s)
#     def button_pressed(self, s):
#         print("press", s)
#         if s == False:
#             print("False",s)
#             s = True
#         else:   
#             print("True",s)
#             s = False
#         print("Button press", s)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()
###
