'''
has https://www.geeksforgeeks.org/python/pyqt5-qlistwidget-python/
example of QListWidget

'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc

# class MainWindow(qtw.QWidget):

#     def __init__(self):
#         """MainWindow constructor."""
#         super().__init__()

#         # Configure the window
#         self.setWindowTitle("My Calendar App")
#         self.resize(800, 600)

#         # Create our widgets
#         self.calendar = qtw.QCalendarWidget()
#         self.event_list = qtw.QListWidget()
#         self.event_title = qtw.QLineEdit()
#         self.event_category = qtw.QComboBox()
#         self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
#         self.allday_check = qtw.QCheckBox('All Day')
#         self.event_detail = qtw.QTextEdit()
#         self.add_button = qtw.QPushButton('Add/Update')
#         self.del_button = qtw.QPushButton('Delete')

#         # Configure some widgets

#         # Add event categories
#         self.event_category.addItems(
#             ['Select category…', 'New…', 'Work',
#              'Meeting', 'Doctor', 'Family']
#             )
#         # disable the first category item
#         self.event_category.model().item(0).setEnabled(False)

#         # Arrange the widgets
#         main_layout = qtw.QHBoxLayout()
#         self.setLayout(main_layout)
#         main_layout.addWidget(self.calendar)
#         # Calendar expands to fill the window
#         self.calendar.setSizePolicy(
#             qtw.QSizePolicy.Expanding,
#             qtw.QSizePolicy.Expanding
#         )
#         right_layout = qtw.QVBoxLayout()
#         main_layout.addLayout(right_layout)
#         right_layout.addWidget(qtw.QLabel('Events on Date'))
#         right_layout.addWidget(self.event_list)
#         # Event list expands to fill the right area
#         self.event_list.setSizePolicy(
#             qtw.QSizePolicy.Expanding,
#             qtw.QSizePolicy.Expanding
#         )
#         ## this is the bottom right of the calendar
#         # Create a sub-layout for the event view/add form
#         event_form = qtw.QGroupBox('Event')
#         right_layout.addWidget(event_form)
#         event_form_layout = qtw.QGridLayout()
#         event_form.setLayout(event_form_layout)

#         event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
#         event_form_layout.addWidget(self.event_category, 2, 1)
#         event_form_layout.addWidget(self.event_time, 2, 2,)
#         event_form_layout.addWidget(self.allday_check, 2, 3)
#         event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
#         event_form_layout.addWidget(self.add_button, 4, 2)
#         event_form_layout.addWidget(self.del_button, 4, 3)

#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem


class Ui_MainWindow(QWidget):
    def __init__(self, parent = None):
        super(Ui_MainWindow, self).__init__(parent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    listWidget = QListWidget()
    window.setWindowTitle("Demo for QListWidget")

    QListWidgetItem("Geeks", listWidget)
    QListWidgetItem("For", listWidget)
    QListWidgetItem("Geeks", listWidget)

    listWidgetItem = QListWidgetItem("GeeksForGeeks")
    listWidget.addItem(listWidgetItem)
    
    window_layout = QVBoxLayout(window)
    window_layout.addWidget(listWidget)
    window.setLayout(window_layout)

    window.show()

    sys.exit(app.exec_())
    
    '''
    https://www.geeksforgeeks.org/python/pyqt5-qlistwidget-python/
     QListWidget is a convenience class that provides a list view with a classic item-based interface for adding and removing items. QListWidget uses an internal model to manage each QListWidgetItem in the list. Syntax:

listWidget = QListWidget()
There are two ways to add items to the list. 

They can be constructed with the list widget as their parent widget.
QListWidgetItem("Geeks", listWidget)
QListWidgetItem("For", listWidget)
QListWidgetItem("Geeks", listWidget)
They can be constructed with no parent widget and added to the list later.
listWidgetItem = QListWidgetItem("GeeksForGeeks")
listWidget.addItem(listWidgetItem)
Some of the most frequently used methods in QListWidget:

addItem() : To add QListWidgetItem object in list
addItems() : To add multiple QListWidgetItem objects
insertItem() : It adds item at specified position
clear() : To delete all the items present in the list
count() : To count number of items present in the list'''