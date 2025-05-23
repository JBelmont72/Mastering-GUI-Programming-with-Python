'''
create a calendar for a given month and year
using the calendar module
page 50 Mastering GUI Programming with Python
I had to use QVBoxLayout instead of QHBoxLayout to get it to work
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
#         # Main UI code goes here.First configure the main window
#         self.setWindowTitle("My Calendar")
#         self.setGeometry(100, 100, 800, 600)
#         self.setStyleSheet("background-color: lightblue;")
#         # create the widgets
#         self.calendar = qtw.QCalendarWidget()
#         self.event_list = qtw.QListWidget()##for displaying, editing, deleting events
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
#              'Meeting', 'Doctor', 'Family'])##configures the combo box with the given items
#         # disable the first category item
#         self.event_category.model().item(0).setEnabled(False)
        
        
        
        
#         # Configure the calendar widget
#         self.calendar.setSizePolicy(
#             qtw.QSizePolicy.Expanding,
#             qtw.QSizePolicy.Expanding
#         )          
#         self.calendar.setGridVisible(True)
#         self.calendar.setStyleSheet("background-color: white;")
#         self.calendar.setMinimumDate(qtc.QDate(1900, 1, 1))
#         self.calendar.setMaximumDate(qtc.QDate(2100, 12, 31))
#         self.calendar.setFirstDayOfWeek(qtc.Qt.Monday)
#         self.calendar.setLocale(qtc.QLocale(qtc.QLocale.English, qtc.QLocale.UnitedStates))
#         self.calendar.setVerticalHeaderFormat(qtw.QCalendarWidget.NoVerticalHeader)
#         self.calendar.setHorizontalHeaderFormat(qtw.QCalendarWidget.ShortDayNames)## could have singleLetterNames also
#         self.calendar.setNavigationBarVisible(True)
#         self.calendar.setDateTextFormat(qtc.QDate.currentDate(), qtg.QTextCharFormat())
#         self.calendar.setSelectedDate(qtc.QDate.currentDate())
        
        
#         ## build the layout
#         main_layout = qtw.QHBoxLayout()
#         self.setLayout(main_layout)
#         main_layout.addWidget(self.calendar)
        
#         ##the below code was commented out in the original and displayed the event list
#        ## add the event list below the calendar
#         # main_layout.addWidget(self.event_list)
#         # # Event list expands to fill the right area
#         # self.event_list.setSizePolicy(
#         #     qtw.QSizePolicy.Expanding,
#         #     qtw.QSizePolicy.Expanding
#         # ) ## at this point the event list is empty
        
        
#         # Create a sub-layout for the event view/add form
#         event_form = qtw.QGroupBox('Event')
#         main_layout.addWidget(event_form)
#         event_form_layout = qtw.QGridLayout()
#         event_form.setLayout(event_form_layout)
#         event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
#         event_form_layout.addWidget(self.event_category, 2, 1)
#         event_form_layout.addWidget(self.event_time, 2, 2,)
#         event_form_layout.addWidget(self.allday_check, 2, 3)
#         event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
#         event_form_layout.addWidget(self.add_button, 4, 2)
#         event_form_layout.addWidget(self.del_button, 4, 3)
#         # Set the size policy for the event form could repeat the code for the event list but I did not see the need to do so
#         # event_form.setSizePolicy(
#         #     qtw.QSizePolicy.Expanding,
#         #     qtw.QSizePolicy.Expanding)
       
      
#         # End main UI code
#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
#### below is the code for the calendar form and I will add the event list and event form to a verticl layout
## here i created a v_layout to the right of the calendar and just listed the widgets vertically
## next version I will use a grid layout for the event form
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
#         # Main UI code goes here.First configure the main window
#         self.setWindowTitle("My Calendar")
#         self.setGeometry(100, 100, 800, 600)
#         self.setStyleSheet("background-color: lightblue;")
#         # create the widgets
#         self.calendar = qtw.QCalendarWidget()
#         self.event_list = qtw.QListWidget()##for displaying, editing, deleting events
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
#              'Meeting', 'Doctor', 'Family'])##configures the combo box with the given items
#         # disable the first category item
#         self.event_category.model().item(0).setEnabled(False)
        
        
        
        
#         # Configure the calendar widget
#         self.calendar.setSizePolicy(
#             qtw.QSizePolicy.Expanding,
#             qtw.QSizePolicy.Expanding
#         )          
#         self.calendar.setGridVisible(True)
#         self.calendar.setStyleSheet("background-color: white;")
#         self.calendar.setMinimumDate(qtc.QDate(1900, 1, 1))
#         self.calendar.setMaximumDate(qtc.QDate(2100, 12, 31))
#         self.calendar.setFirstDayOfWeek(qtc.Qt.Monday)
#         self.calendar.setLocale(qtc.QLocale(qtc.QLocale.English, qtc.QLocale.UnitedStates))
#         self.calendar.setVerticalHeaderFormat(qtw.QCalendarWidget.NoVerticalHeader)
#         self.calendar.setHorizontalHeaderFormat(qtw.QCalendarWidget.ShortDayNames)## could have singleLetterNames also
#         self.calendar.setNavigationBarVisible(True)
#         self.calendar.setDateTextFormat(qtc.QDate.currentDate(), qtg.QTextCharFormat())
#         self.calendar.setSelectedDate(qtc.QDate.currentDate())
        
        
#         ## build the layout
#         main_layout = qtw.QHBoxLayout()
#         self.setLayout(main_layout)
#         main_layout.addWidget(self.calendar)
        
#         ## build the right layout
#         v_layout=qtw.QVBoxLayout()
#         main_layout.addLayout(v_layout)
#         v_layout.addWidget(self.event_list)
#         v_layout.addWidget(self.event_title)
#         v_layout.addWidget(self.event_category)
#         v_layout.addWidget(self.event_time)
#         v_layout.addWidget(self.allday_check)
        
        
        
        
#         ##the below code was commented out in the original and displayed the event list
#        ## add the event list below the calendar
#         # main_layout.addWidget(self.event_list)
#         # # Event list expands to fill the right area
#         # self.event_list.setSizePolicy(
#         #     qtw.QSizePolicy.Expanding,
#         #     qtw.QSizePolicy.Expanding
#         # ) ## at this point the event list is empty
        
        
#         # # Create a sub-layout for the event view/add form
#         # event_form = qtw.QGroupBox('Event')
#         # main_layout.addWidget(event_form)
#         # event_form_layout = qtw.QGridLayout()
#         # event_form.setLayout(event_form_layout)
#         # event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
#         # event_form_layout.addWidget(self.event_category, 2, 1)
#         # event_form_layout.addWidget(self.event_time, 2, 2,)
#         # event_form_layout.addWidget(self.allday_check, 2, 3)
#         # event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
#         # event_form_layout.addWidget(self.add_button, 4, 2)
#         # event_form_layout.addWidget(self.del_button, 4, 3)
#         # # Set the size policy for the event form could repeat the code for the event list but I did not see the need to do so
#         # # event_form.setSizePolicy(
#         # #     qtw.QSizePolicy.Expanding,
#         # #     qtw.QSizePolicy.Expanding)
       
      
#         # End main UI code
#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     # it's required to save a reference to MainWindow.
#     # if it goes out of scope, it will be destroyed.
#     mw = MainWindow()
#     sys.exit(app.exec())
### below is the complete code(same as calendar_1.py
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor."""
        super().__init__()

        # Configure the window
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        # Create our widgets
        self.calendar = qtw.QCalendarWidget()
        self.event_list = qtw.QListWidget()
        self.event_title = qtw.QLineEdit()
        self.event_category = qtw.QComboBox()
        self.event_time = qtw.QTimeEdit(qtc.QTime(8, 0))
        self.allday_check = qtw.QCheckBox('All Day')
        self.event_detail = qtw.QTextEdit()
        self.add_button = qtw.QPushButton('Add/Update')
        self.del_button = qtw.QPushButton('Delete')

        # Configure some widgets

        # Add event categories
        self.event_category.addItems(
            ['Select category…', 'New…', 'Work',
             'Meeting', 'Doctor', 'Family']
            )
        # disable the first category item
        self.event_category.model().item(0).setEnabled(False)

        # Arrange the widgets
        #Create the main laoyout and add the calendar
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)
        # Calendar expands to fill the window
        self.calendar.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )
        ## create a sub-layout for the event list and form
        right_layout = qtw.QVBoxLayout()
        # Add the right layout to the main layout
        main_layout.addLayout(right_layout)
        # start adding widgets to the right layout
        right_layout.addWidget(qtw.QLabel('Events on Date'))
        # right_layout.addWidget(self.event_list)## QListWidget
        # Event list expands to fill the right area so it fills the available space
        self.event_list.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )

        # Create a sub-layout for the event view/add form
        # and add it to the right layout
        # the QGroupBox is a container for the event form
        event_form = qtw.QGroupBox('Event Details')
        right_layout.addWidget(event_form)
        event_form_layout = qtw.QGridLayout()
        event_form.setLayout(event_form_layout)
        
        new_form=qtw.QGroupBox('More Event Details')
        right_layout.addWidget(new_form)
        

        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)#QLineEdit
        event_form_layout.addWidget(self.event_category, 2, 1)#QComboBox added the drop down list
        event_form_layout.addWidget(self.event_time, 2, 2,)#QTimeEdit(qtc.QTime(8, 0))
        event_form_layout.addWidget(self.allday_check, 2, 3)#QCheckBox('All Day')
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)#QTextEdit
        self.newPushButton=qtw.QPushButton('New')
        event_form_layout.addWidget(self.newPushButton, 4,1 )#QPushButton('New')
        event_form_layout.addWidget(self.add_button, 4, 2)#QPushButton('Add/Update')
        event_form_layout.addWidget(self.del_button, 4, 3)#QPushButton('Delete')

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())