import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog(self)
        result = dlg.exec()
        if result == QDialog.Accepted:
            print(f"Dialog accepted (OK or Apply pressed) {result}")
        elif result == QDialog.Rejected:
            print(f"Dialog rejected (Cancel pressed): {result}")
        else:
            print("Dialog closed with result:", result)
        # def button_clicked(self, s):
        #     print("click", s)

        #     dlg = CustomDialog(self)
        #     if dlg.exec_():
        #         print('Success')
        #     else:
        #         print('Cancel')

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")
        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        
        self.setLayout(layout)
        # Define which buttons to show in the dialog
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.Open | QDialogButtonBox.Apply

        # Create the button box with the specified buttons
        self.buttonBox = QDialogButtonBox(QBtn)
        layout.addWidget(self.buttonBox)
        # Connect the accepted signal to self.accept (triggered by OK and Apply by default)
        self.buttonBox.accepted.connect(self.accept)  # OK, Apply

        # Connect the rejected signal to self.reject (triggered by Cancel by default)
        self.buttonBox.rejected.connect(self.reject)  # Cancel

        # Connect the Open button's clicked signal to a custom slot
        open_button = self.buttonBox.button(QDialogButtonBox.Open)
        if open_button:
            open_button.clicked.connect(self.open_clicked)

        # Connect the Apply button's clicked signal to a custom slot
        apply_button = self.buttonBox.button(QDialogButtonBox.Apply)
        if apply_button:
            apply_button.clicked.connect(self.apply_clicked)
        self.show()
    def open_clicked(self):
        print("Open button clicked")
    # Add custom logic for Open button here

    def apply_clicked(self):
        print("Apply button clicked")
    # Add custom logic for Apply button here
       
        # layout = QVBoxLayout()
        # message = QLabel("Something happened, is that OK?")
        # layout.addWidget(message)
        # layout.addWidget(self.buttonBox)
        # self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


'''
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Dialog")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        label = QLabel("Do you want to proceed?")
        layout.addWidget(label)

        # Create button box with OK and Cancel buttons
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

# Usage
dialog = MyDialog()
if dialog.exec_() == QDialog.Accepted:
    print("Accepted")
else:
    print("Rejected")
'''