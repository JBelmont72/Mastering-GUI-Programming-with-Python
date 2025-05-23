'''
https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QWidget):

#     def __init__(self):
#         """MainWindow constructor.

#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         super().__init__()
#         # Main UI code goes here

#         # End main UI code
#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
# ###~~~~
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QWidget):

#     def __init__(self):
#         """MainWindow constructor.

#         This widget will be our main window.
#         We'll define all the UI components in here.
#         """
#         super().__init__()
#         # Main UI code goes here

#         # End main UI code
#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
### example where the button is checkable but not checked. so for a signal to be observed, need .setChecked(True)
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# # class MainWindow(qtw.QWidget):


# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.button_is_checked = True

#         self.setWindowTitle("My App")

#         self.button = qtw.QPushButton("Press Me!")
#         self.button.setCheckable(True)
#         self.button.released.connect(self.the_button_was_released)
#         self.button.setChecked(self.button_is_checked)

#         self.setCentralWidget(self.button)
#         self.show()
#     def the_button_was_released(self):
#         self.button_is_checked = self.button.isChecked()

#         print(self.button_is_checked) ## output: True,False,True....
 

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
###
# Changing the interface
# So far we've seen how to accept signals and print output to the console. But how about making something happen in the interface when we click the button? Let's update our slot method to modify the button, changing the text and disabling the button so it is no longer clickable. We'll also turn off the checkable state for now.
# Again, because we need to be able to access the button in our the_button_was_clicked method, we keep a reference to it on self. The text of the button is changed by passing a str to .setText(). To disable a button call .setEnabled() with False   as the argument. This will grey out the button and prevent it from being clicked again. To make the button checkable again, we can call .setCheckable(True) on it.

# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui as qtg
# from PyQt5 import QtCore as qtc

# # class MainWindow(qtw.QWidget):


# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()
        

#         self.setWindowTitle("My App")

#         self.button = qtw.QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)

#         self.setCentralWidget(self.button)
#         self.show()
#     def the_button_was_clicked(self):
#         self.button.setText("You already clicked me.")
#         self.button.setEnabled(False)
#         # Also change the window title.
#         self.setWindowTitle("My Oneshot App")
        

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())

####
# First we set up a list of window titles -- we'll select one at random from this list using Python's built-in random.choice(). We hook our custom slot method the_window_title_changed to the window's .windowTitleChanged signal.

# When we click the button the window title will change at random. If the new window title equals "Something went wrong" the button will be disabled.
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QWidget):
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = qtw.QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
        self.show()
    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
        count = self.n_times_clicked
        self.n_times_clicked += 1
        self.button.setText("Clicked %d times" % count) # if i stop here, the button will be disabled if window title is "Something went wrong"
        # self.button.setText("You already clicked me.")
        # self.button.setEnabled(True)
        # self.button.setCheckable(True)
        # self.button.setChecked(True)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())



