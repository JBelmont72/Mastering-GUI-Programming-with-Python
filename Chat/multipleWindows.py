'''
/Users/judsonbelmont/Documents/Shared_Folders/Mastering-GUI-Programming-with-Python/Chat/multipleWindows.py
https://chatgpt.com/c/68602b54-be4c-800f-8a73-95fbaaa16184
opening multiple windows using import uic

The self.second_window reference ensures the second window stays in memory.
You can also use QDialog instead of QMainWindow if it's a temporary popup.
You can open as many windows as you like this way—just repeat the pattern.
you don’t have to assign None before creating and showing a third window, but doing so helps manage whether a new instance is created each time you open the window.

what does 'self.second_window = None' do?
Just a way to:

Initialize a variable to store a reference to the window.
Later, check if it's already open to avoid creating it again.

Use this if you want to open a window once and reuse it

what happens if you open the second/ third/etc Window Without NONE:

def open_third_window(self):
    third_window = ThirdWindow()
    third_window.show()
⛔ Problem: If you don’t store a reference (like self.third_window = ...), the new window may be immediately garbage collected, and it won’t stay open.

✅ Solution: Store the instance in an attribute or list:

def open_third_window(self):
    self.third_window = ThirdWindow()  # this keeps it alive
    self.third_window.show()
    
OR if you want multiple third windows (e.g. duplicates):

def open_third_window(self):
    new_window = ThirdWindow()
    new_window.show()
    self.open_windows.append(new_window)  # track open ones

| Goal                           | Do This                                   |
| ------------------------------ | ----------------------------------------- |
| Open once, reuse               | Use `self.third_window = None` + check    |
| Open fresh copy each time      | Create a new instance and store reference |
| Multiple third windows at once | Store instances in a list                 |


'''

# from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
# from PyQt5 import uic
# import sys
# class ThirdWindow(QMainWindow):
#     def __init__(self):
#         super(ThirdWindow,self).__init__()
#         uic.loadUi('Chat/Third.ui',self)
#         self.label=self.findChild(QLabel,'label')
#         self.main=self.findChild(QPushButton,'pushButton_2')
#         print("self.main:", self.main)  # Should not be None
#         self.second = self.findChild(QPushButton,'pushButton_3')
#         self.multiple=self.findChild(QPushButton,'pushButton')
#         self.multiple.clicked.connect(lambda : self.open_MainWindow())
#         self.main.clicked.connect(lambda : self.open_MainWindow())

#     def open_MainWindow(self):
#         print('open MainWindow from ThirdWindow')
        
# class SecondWindow(QMainWindow):
#     def __init__(self):
#         super(SecondWindow,self).__init__()
#         uic.loadUi('Chat/Second.ui',self)
#         self.setWindowTitle('My Own Second Window')
#         self.label=self.findChild(QLabel,'label')
#         self.main=self.findChild(QPushButton,'pushButton_2')
#         self.third=self.findChild(QPushButton,'pushButton_3')
#         self.multiple=self.findChild(QPushButton,'pushButton')
#         self.show()
#         ## connect buttons  
#         self.main.clicked.connect(lambda : self.openMain())

    
#     def openMain(self):
#         print('second window says Open MainWindow')
#         self.MainWindow=MainWindow()
#         if self.MainWindow== None:
#             self.MainWindow.show()
        

# class MainWindow(QMainWindow):
#     def __init__(self):
#         self.open_windows=[]
#         self.i =0 
#         super(MainWindow,self).__init__()
#         uic.loadUi('Chat/Main.ui', self)
#         self.label=self.findChild(QLabel,'label')
#         self.PushSecond=self.findChild(QPushButton,'pushButton_2')
#         self.PushThird=self.findChild(QPushButton,'pushButton_3')
#         self.PushMultiple=self.findChild(QPushButton,'pushButton')
#         ## connect the buttons to second and third windows, and opening multiple windows
#         self.PushSecond.clicked.connect(lambda: self.openSecond())
#         self.PushThird.clicked.connect(lambda : self.open_third_window(self.i))
#         self.show()
        
     
#     def openSecond(self):
#         print('open second window')
#         self.SecondWindow=SecondWindow()
#         if self.SecondWindow==None:
#             self.SecondWindow.show()


# ## Use this if you want to open a window once and reuse it
#     # def openSecond(self):
#     #     if self.SecondWindow== None:
#     #         self.SecondWindow=SecondWindow()
#     #     self.SecondWindow.show()

    
    
# ## you don’t have to assign None before creating and showing a third window, but doing so helps manage whether a new instance is created each time you open the window.
#     def open_third_window(self,var):
#         var =(var+1)
        
#         new_window = ThirdWindow()
#         new_window.show()
#         self.open_windows.append(new_window)  # track open ones
        
        
        
#         new_window.setWindowTitle(f'my thirdWindow Number {len(self.open_windows)}')

#         # Example: If at least two ThirdWindows are open, do something with both
#         # new_window.setWindowTitle(f'my thirdWindow Number {var}')
#         if len(self.open_windows) >= 2:
#             win1 = self.open_windows[0]
#             win2 = self.open_windows[1]
#             # Example 1: Change the label text of the first window
#             if win1.label is not None:
#                 win1.label.setText("First ThirdWindow updated!")
#             else:
#                 print("Warning: win1.label is None. Check 'label' objectName in Third.ui.")
#             # Example 2: Disable a button in the second window
#             win2.main.setEnabled(False)
#             new_window.setWindowTitle(f'my thirdWindow Number {len(self.open_windows)}')
#     # def open_third_window(self):
#     #     if ThirdWindow()==None:
#     #         self.ThirdWindow=ThirdWindow()
#     #     self.ThirdWindow.show()
            
#     # def open_third_window(self):
#     #     print('Open Third Window from MainWindow')
#     #     self.ThirdWindow=ThirdWindow()
#     #     if self.ThirdWindow== None:
#     #         self.ThirdWindow.show()

    
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     window=MainWindow()
#     window.show()
#     sys.exit(app.exec_())

## examplefrom chat


# from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton
# from PyQt5 import uic
# import sys
# class ThirdWindow(QMainWindow):
#     def __init__(self):
#         super(ThirdWindow,self).__init__()
#         uic.loadUi('Chat/Third.ui',self)
#         self.label=self.findChild(QLabel,'label')
#         self.main=self.findChild(QPushButton,'pushButton_2')
#         print("self.main:", self.main)  # Should not be None
#         self.second = self.findChild(QPushButton,'pushButton_3')
#         self.multiple=self.findChild(QPushButton,'pushButton')
#         self.multiple.clicked.connect(lambda : self.open_MainWindow())
#         self.main.clicked.connect(lambda : self.open_MainWindow())

#     def open_MainWindow(self):
#         print('open MainWindow from ThirdWindow')
        
# class SecondWindow(QMainWindow):
#     def __init__(self):
#         super(SecondWindow,self).__init__()
#         uic.loadUi('Chat/Second.ui',self)
#         self.setWindowTitle('My Own Second Window')
#         self.label=self.findChild(QLabel,'label')
#         self.main=self.findChild(QPushButton,'pushButton_2')
#         self.third=self.findChild(QPushButton,'pushButton_3')
#         self.multiple=self.findChild(QPushButton,'pushButton')
#         self.show()
#         ## connect buttons  
#         self.main.clicked.connect(lambda : self.openMain())

    
#     def openMain(self):
#         print('second window says Open MainWindow')
#         self.MainWindow=MainWindow()
#         if self.MainWindow== None:
#             self.MainWindow.show()
        

# class MainWindow(QMainWindow):
#     def __init__(self):
         
#         super(MainWindow,self).__init__()
#         uic.loadUi('Chat/Main.ui', self)
#         self.label=self.findChild(QLabel,'label')
#         self.PushSecond=self.findChild(QPushButton,'pushButton_2')
#         self.PushThird=self.findChild(QPushButton,'pushButton_3')
#         self.PushMultiple=self.findChild(QPushButton,'pushButton')
#         ## connect the buttons to second and third windows, and opening multiple windows
        


#         # Connect buttons
#         self.PushSecond.clicked.connect(self.open_second_window)
#         self.PushThird.clicked.connect(self.open_new_third_window)
#         self.PushMultiple.clicked.connect(self.list_third_windows)

#         # State tracking
#         self.second_window = None
#         self.third_windows = []  # list of ThirdWindow instances
# ## this function as written opens only one SecondWindow compared to the function  following, but this one must be instantiated in the main program
#     def open_second_window(self):
#         if self.second_window is None:
#             self.second_window = SecondWindow()
#         self.second_window.show()

# ## this function opens as many second windows as I click on
#     # def open_second_window(self):
#     #     print('open second window')
#     #     self.SecondWindow=SecondWindow() # i think because i am creating a new instance each time
#     #     if self.SecondWindow==None:
#     #         self.SecondWindow.show()


#     def open_new_third_window(self):
#         new_win = ThirdWindow()
#         self.third_windows.append(new_win)
#         new_win.setWindowTitle(f"Third Window #{len(self.third_windows)}")
#         new_win.show()

#     def list_third_windows(self):
#         print("Currently open third windows:")
#         for i, win in enumerate(self.third_windows):
#             if win.isVisible():
#                 print(f"  [{i}] Visible - {win.windowTitle()}")
#             else:
#                 print(f"  [{i}] Closed - {win.windowTitle()}")

    
    
    
# ###~~~~~~    
# if __name__ =='__main__':
#     app=QApplication(sys.argv)
#     window=MainWindow()
#     window.show()
#     sys.exit(app.exec_())
    
'''
"Why is self.second_window = None needed, but I don't need self.third_window = None?"
Here’s a clear explanation:

✅ You do need self.third_window = None if you want to:

Check whether it’s already open (like you do with second_window)
Avoid opening multiple instances
Reuse a previously opened window object
Close and reopen it cleanly
🧠 Why self.second_window = None was necessary

You had this code:

if self.second_window is None:
    self.second_window = SecondWindow(self)
    self.second_window.show()
This means you’re checking whether it’s already created — so self.second_window must already exist, or you’ll get an error. That’s why it needs to be initialized earlier:

self.second_window = None  # ✅ allows safe if-check
🔍 Why self.third_window = None might not seem necessary

If you're not checking or reusing the third window — and you're just doing this:

self.third_window = ThirdWindow(self)
self.third_window.show()
… then there's no need to initialize it beforehand. You're assigning a new value directly — no prior value is being referenced.

So this works just fine:

def open_third_window(self):
    self.third_window = ThirdWindow(self)  # No need to check if None
    self.third_window.show()
✅ Rule of Thumb

Use Case	Do you need self.X = None?
Check if it already exists (if self.X is None)	✅ Yes
Always recreate new instance	❌ No
Want to reuse or close then reopen	✅ Yes
👩‍💻 Recommendation

If you ever plan to track or limit windows (e.g., prevent duplicates), initialize it like:

self.third_window = None
If you're fine with always making new ones, don't worry about it.

https://chatgpt.com/c/68602b54-be4c-800f-8a73-95fbaaa16184
/Users/judsonbelmont/Documents/Shared_Folders/Mastering-GUI-Programming-with-Python/Chat/multipleWindows.py
best complete program starts at line 310
'''



from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import uic
import sys

class ThirdWindow(QMainWindow):
    def __init__(self):
        super(ThirdWindow, self).__init__()
        uic.loadUi('Chat/Third.ui', self)
        self.label = self.findChild(QLabel, 'label')
        self.main = self.findChild(QPushButton, 'pushButton_2')
        self.second = self.findChild(QPushButton, 'pushButton_3')
        self.multiple = self.findChild(QPushButton, 'pushButton')

        self.multiple.clicked.connect(self.open_MainWindow)
        self.main.clicked.connect(self.open_MainWindow)

    def open_MainWindow(self):
        print('open MainWindow from ThirdWindow')

class SecondWindow(QMainWindow):
    def __init__(self, main_window):
        super(SecondWindow, self).__init__()
        uic.loadUi('Chat/Second.ui', self)
        self.setWindowTitle('My Own Second Window')

        self.label = self.findChild(QLabel, 'label')
        self.main = self.findChild(QPushButton, 'pushButton_2')
        self.third = self.findChild(QPushButton, 'pushButton_3')
        self.multiple = self.findChild(QPushButton, 'pushButton')

        self.main_window = main_window  # 👈 Save reference to existing MainWindow
        self.main.clicked.connect(self.openMain)
        self.show()
##~~   Below  This will re-show the original MainWindow (which had been hidden, not closed or deleted). You don’t need to create a new one or track it separately.
    def openMain(self):
        print('SecondWindow: "Return to MainWindow" pressed.')
        if self.main_window.isHidden():
            self.main_window.show()
            self.main_window.raise_()  # Bring it to front (optional)

    def closeEvent(self, event):
        print("SecondWindow closed — resetting MainWindow pointer.")
        self.main_window.second_window = None
        super().closeEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Chat/Main.ui', self)

        self.label = self.findChild(QLabel, 'label')
        self.PushSecond = self.findChild(QPushButton, 'pushButton_2')
        self.PushThird = self.findChild(QPushButton, 'pushButton_3')
        self.PushMultiple = self.findChild(QPushButton, 'pushButton')

        self.PushSecond.clicked.connect(self.open_second_window)
        self.PushThird.clicked.connect(self.open_new_third_window)
        self.PushMultiple.clicked.connect(self.list_third_windows)

        self.second_window = None
        self.third_windows = []

    def open_second_window(self):
        if self.second_window is None:
            self.second_window = SecondWindow(self)  # 👈 Pass self (MainWindow)
        self.second_window.show()
        self.second_window.raise_()  # 👈 Bring window to front (optional)
## in this function I also add a qui to the second THirdWindow contructed
    def open_new_third_window(self):
        new_win = ThirdWindow()
        self.third_windows.append(new_win)
        new_win.setWindowTitle(f"Third Window #{len(self.third_windows)}")
        new_win.label.setText(f'Third Window number {len(self.third_windows)} ')
        if len(self.third_windows) == 2:
            print('my second Third Window')
            # Add label2 to the second ThirdWindow
            new_win.label2 = QLabel('my new label in 3d window', new_win)
            new_win.label2.setGeometry(10, 50, 200, 30)
            new_win.label2.show()
        new_win.show()

    def list_third_windows(self):
        print("Currently open third windows:")
        for i, win in enumerate(self.third_windows):
            if win.isVisible():
                print(f"  [{i}] Visible - {win.windowTitle()}")
            else:
                print(f"  [{i}] Closed - {win.windowTitle()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

## if i want to add a dialog box to confirm if I really want to close the mainwindow, use this:
# from PyQt5.QtWidgets import QMainWindow, QMessageBox

# class MainWindow(QMainWindow):
#     def closeEvent(self, event):
#         reply = QMessageBox.question(
#             self,
#             "Exit Confirmation",
#             "Are you sure you want to exit?",
#             QMessageBox.Yes | QMessageBox.No,
#             QMessageBox.No
#         )

#         if reply == QMessageBox.Yes:
#             print("MainWindow is closing.")
#             event.accept()
#         else:
#             print("MainWindow close canceled.")
#             event.ignore()
