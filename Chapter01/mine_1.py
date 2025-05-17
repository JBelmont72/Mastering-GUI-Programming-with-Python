'''

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
        self.setWindowFlags( qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint|)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuButtonHint | qtc.Qt.WindowContextHelpButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuButtonHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuButtonHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(qtc.Qt.WindowStaysOnTopHint | qtc.Qt.WindowMinMaxButtonsHint | qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint | qtc.Qt.WindowMinimizeButtonHint | qtc.Qt.WindowFullscreenButtonHint | qtc.Qt.WindowTitleHint | qtc.Qt.WindowSystemMenuButtonHint | qtc.Qt.WindowContextHelpButtonHint | qtc.Qt.WindowMaximizeButtonHint)  
         
        
        # self.setWindowIcon(qtg.QIcon('icon.png'))
        self.setWindowIcon(qtg.QIcon('Chapter02/smile.gif'))
        layout = qtw.QVBoxLayout(self)
        # page 26
        # subWidget = qtw.QWidget(self,toolTip='This is a tooltip')
        subWidget = qtw.QWidget(self,toolTip='This is a tooltip',whatsThis='This is a what\'s this')
        # subWidget = qtw.QWidget(self)
        subWidget.setGeometry(50, 50, 200, 100)
        subWidget.setStyleSheet("background-color: lightgreen;")
        layout.addWidget(subWidget)
        # subWidget.setWindowIcon(qtg.QIcon('Chapter02/smile.gif'))
        # subWidget.setWindowModality(qtc.Qt.ApplicationModal)
        # subWidget.setWindowFlags(qtc.Qt.WindowStaysOnTopHint)
        # subWidget.setAttribute(qtc.Qt.WA_DeleteOnClose)
        # subWidget.setAttribute(qtc.Qt.WA_QuitOnClose)
        # subWidget.setAttribute(qtc.Qt.WA_ShowWithoutActivating)
        # subWidget.setAttribute(qtc.Qt.WA_TransparentForMouseEvents)
        # subWidget.setAttribute(qtc.Qt.WA_AlwaysShowToolTips)
        
        label = qtw.QLabel('Hello, World!', subWidget)
        label.setGeometry(10, 10, 100, 30)
        label.setStyleSheet("color: black; font-size: 20px;")
        label.setAlignment(qtc.Qt.AlignCenter)
        label.setToolTip('This is  my label')
        label.setWhatsThis('This is a my new label')
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
