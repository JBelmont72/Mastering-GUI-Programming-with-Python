'''
last is an example of using whatsThis for qlabel. https://www.geeksforgeeks.org/python/pyqt5-whats-this-help-text-for-label-setwhatsthis-method/

JBelmont72: @workspace /explain Write an explanation for the active selection as paragraphs of text.

```python
label = qtw.QLabel('Hello, World!', subWidget)## this creates label and adds to widget in one step
        
        label=qtw.QLabel(f'I\'m here ')
        subWidget.layout = qtw.QVBoxLayout(subWidget)
        subWidget.layout.addWidget(label)
```



Workspace: This code snippet demonstrates two ways to create and add a `QLabel` widget to a parent widget using PyQt (or PySide, as both use similar APIs). The first line creates a `QLabel` with the text "Hello, World!" and immediately assigns it to `subWidget` as its parent. In PyQt, passing the parent widget to the constructor automatically adds the label to that widget's hierarchy, so it will be displayed when the parent is shown.

The next block creates another label with the text "I'm here" but does not specify a parent in the constructor. Instead, it manually sets up a vertical box layout (`QVBoxLayout`) for `subWidget` and then adds the label to this layout using `addWidget`. This approach is more flexible, as it allows you to control the arrangement of multiple widgets within the parent. By assigning the layout to `subWidget` and adding the label to it, you ensure that the label is managed and displayed according to the layout's rules.

A common 'gotcha' is forgetting to set a layout on the parent widget before adding child widgets, which can result in widgets not appearing as expected. Also, note that creating a widget with a parent (as in the first line) does not automatically add it to a layout; it just ensures proper ownership and visibility. Using layouts is recommended for more complex interfaces, as they handle widget positioning and resizing automatically.



JBelmont72: @workspace /explain Write an explanation for the active selection as paragraphs of text.

```python
label = qtw.QLabel('Hello, World!', subWidget)## this creates label and adds to widget in one step
        
        label=qtw.QLabel(f'I\'m here ')
        subWidget.layout = qtw.QVBoxLayout(subWidget)
        subWidget.layout.addWidget(label)
```



Workspace: This code snippet demonstrates two ways to create and add a `QLabel` widget to a parent widget using PyQt (or PySide, as both use similar APIs). The first line creates a `QLabel` with the text "Hello, World!" and immediately assigns it to `subWidget` as its parent. In PyQt, passing the parent widget to the constructor automatically adds the label to that widget's hierarchy, so it will be displayed when the parent is shown.

The next block creates another label with the text "I'm here" but does not specify a parent in the constructor. Instead, it manually sets up a vertical box layout (`QVBoxLayout`) for `subWidget` and then adds the label to this layout using `addWidget`. This approach is more flexible, as it allows you to control the arrangement of multiple widgets within the parent. By assigning the layout to `subWidget` and adding the label to it, you ensure that the label is managed and displayed according to the layout's rules.

A common 'gotcha' is forgetting to set a layout on the parent widget before adding child widgets, which can result in widgets not appearing as expected. Also, note that creating a widget with a parent (as in the first line) does not automatically add it to a layout; it just ensures proper ownership and visibility. Using layouts is recommended for more complex interfaces, as they handle widget positioning and resizing automatically.

JBelmont72: in this statement "In PyQt, passing the parent widget to the constructor automatically adds the label to that widget's hierarchy, so it will be displayed when the parent is shown.' is the parent widget QWidget but i do not see where it is passed(this references the first constructor)

GitHub Copilot: In the statement `label = qtw.QLabel('Hello, World!', subWidget)`, the second argument (`subWidget`) is the parent widget being passed to the `QLabel` constructor. Here, `subWidget` is an instance of `QWidget` that was created earlier in your code. By passing `subWidget` as the parent, you ensure that the label becomes a child of `subWidget` and will be managed and displayed within it. This is a common pattern in PyQt: the parent widget is specified as the second argument when creating child widgets.
'''
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        self.setWindowTitle('Hello Qt')
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: lightblue;")
        self.setCursor(qtc.Qt.PointingHandCursor)#page 27
        self.setWindowOpacity(1.0)#page 27
        # self.setWindowFlags( qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint|)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint)
        self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint |   qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)  
         
        
        # self.setWindowIcon(qtg.QIcon('icon.png'))
        self.setWindowIcon(qtg.QIcon('/Users/judsonbelmont/Documents/Shared_Folders/Mastering-GUI-Programming-with-Python/Chapter02/smile.gif'))
        layout = qtw.QVBoxLayout(self)
        # page 26
        # subWidget = qtw.QWidget(self,toolTip='This is a tooltip')
        subWidget = qtw.QWidget(self,toolTip='This is a tooltip',whatsThis='This is a what\'s this')
        # subWidget = qtw.QWidget(self)
        subWidget.setGeometry(50, 50, 200, 100)
        subWidget.setStyleSheet("background-color: lightgreen;")
        layout.addWidget(subWidget)
        subWidget.setWindowIcon(qtg.QIcon('/Users/judsonbelmont/Documents/Shared_Folders/Mastering-GUI-Programming-with-Python/Chapter02/smile.gif'))
        # subWidget.setWindowIcon(qtg.QIcon('Chapter02/smile.gif'))
        # subWidget.setWindowModality(qtc.Qt.ApplicationModal)
        # subWidget.setWindowFlags(qtc.Qt.WindowStaysOnTopHint)
        # subWidget.setAttribute(qtc.Qt.WA_DeleteOnClose)
        # subWidget.setAttribute(qtc.Qt.WA_QuitOnClose)
        # subWidget.setAttribute(qtc.Qt.WA_ShowWithoutActivating)
        # subWidget.setAttribute(qtc.Qt.WA_TransparentForMouseEvents)
        # subWidget.setAttribute(qtc.Qt.WA_AlwaysShowToolTips)
        ### below are the coonans discussed above about option to construct thr label guis
        label = qtw.QLabel('Hello, World!', subWidget)## this creates label and adds to widget in one step
        ## the comments from co pilot at top refrence these tow methods of constructing and adding Qlabel. the second is preferred
        label=qtw.QLabel(f'I\'m here ')
        subWidget.layout = qtw.QVBoxLayout(subWidget)
        subWidget.layout.addWidget(label)
        label2=qtw.QLabel(f'Look ma no hands!')
        subWidget.layout.addWidget(label2)
        
        
        
        
        label.setGeometry(10, 10, 100, 30)
        label.setStyleSheet("color: black; font-size: 20px;")
        label.setAlignment(qtc.Qt.AlignCenter)
        label.setToolTip('This is  my label')
        label.setWhatsThis('This is a my new label')
        label.setToolTipDuration(20)## this sets tootip duraton
        label.setGeometry(10, 10, 100, 60)
        ## these methods are for text selection
        label.setTextInteractionFlags(qtc.Qt.TextSelectableByKeyboard)## this is for text selection
        # label.setTextInteractionFlags(qtc.Qt.TextBrowserInteraction)# this is for text selection
        # label.setTextInteractionFlags(qtc.Qt.TextEditorInteraction)# this is for text selection       
        # label.setTextInteractionFlags(qtc.Qt.TextSelectableByMouse)## this is for text selection
        # label.setTextInteractionFlags(qtc.Qt.TextSelectableByMouse | qtc.Qt.TextSelectableByKeyboard)## this is for text selection
        # label.setTextInteractionFlags(qtc.Qt.TextSelectableByMouse | qtc.Qt.TextSelectableByKeyboard | qtc.Qt.TextBrowserInteraction)## this is for text selection 
        # label=qtw.QLabel('<b>Hello, My Label!</b>', subWidget,margin=100,indent=20)   
        label=qtw.QLabel('<b>Hello, My Label!</b>',margin=100,indent=20)   
        label.setMargin(0)
        label.setIndent(10)
        label.setWordWrap(True)
       
        myLineEdit = qtw.QLineEdit(subWidget)
        myLineEdit.setGeometry(10, 50, 100, 30)
        myLineEdit.setPlaceholderText('Enter text here')
        myLineEdit.setStyleSheet("background-color: white; color: black; font-size: 16px;")
        myLineEdit.setToolTip('This is a line edit')
        myLineEdit.setWhatsThis('This is a new line edit')
        # myLineEdit.setText('Hello, World!')## if use this, the placeholder text will not be shown

        layout.addWidget(myLineEdit)
        
        
        # End main UI code
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
    
    
## this shows the use of 'setWhatsThis

# importing the required libraries

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys


class Window(QMainWindow):


    def __init__(self):
        super().__init__()


        # set the title
        self.setWindowTitle("Python")

        # setting  the geometry of window
        self.setGeometry(60, 60, 600, 400)

        # creating a label widget
        self.label_1 = QLabel("Label ", self)
        # moving position
        self.label_1.move(100, 100)

        # setting up the border
        self.label_1.setStyleSheet("border :3px solid blue;")

        help_text = "this is a label"

        # setting the information for a label
        self.label_1.setWhatsThis(help_text)

        # accessing the information
        whats_this = self.label_1.whatsThis()

        # creating a label widget to display whatsthis
        self.label_2 = QLabel(whats_this, self)

        # moving the label
        self.label_2.move(100, 130)


        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
