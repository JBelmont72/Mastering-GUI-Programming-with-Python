import sys
from random import randint

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
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    # tag::show_new_window[] ## both ways work, one is use the boolean value of 'is_checked',second is setting window to None etc.
    def show_new_window(self, is_checked):
        print(is_checked)
        # if self.w is None:
        #     self.w = AnotherWindow()
        #     self.w.show()

        # else:
        #     self.w = None  # Discard reference, close window.
        if is_checked ==True:
            self.w = AnotherWindow()
            self.w.show()

        else:
            self.w = None  # Discard reference, close window.

    # end::show_new_window[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
