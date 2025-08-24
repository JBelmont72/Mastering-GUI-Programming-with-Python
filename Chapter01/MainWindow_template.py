'''this is a main window template i which a create a layout, then a central_widget=QWidget(), then central-widget.setLayout(layout), and finally self.setCentralWidget(central_widget)'''

import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QVBoxLayout,QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.button = QPushButton('press me')
        self.button.setCheckable(True)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()
if __name__=='__main__':
    app =QApplication(sys.argv)
    w=MainWindow()
    w.show()
    sys.exit(app.exec_())