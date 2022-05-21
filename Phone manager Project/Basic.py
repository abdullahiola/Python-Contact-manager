
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

'''
#window
class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("window")
        self.resize(500,400)
        
        layout=QBoxLayout(QBoxlayout.LeftToRight)
        self.setLayout(layout)

        greet = QLabel('Hello World')
        greet.setAlignment(Qt.Aligncenter)
        layout.addWidget(greet)

app = QApplication(sys.argv)
screen= Window()
screen.show()
'''



#MessageBox
class MessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setText("This is a MessageBox, used to convey messages")
        self.setInformativeText('informaative text is written here')
        self.setIcon(QMessageBox.Information)
        self.setStandardButtons(QMessageBox.Close)

app=QApplication(sys.argv)

screen= MessageBox()
screen.show()

sys.exit(app.exec_())
'''





#Qwidget
class window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Hello')

        layout=QGridLayout()
        self.setLayout(layout)

        label=QLabel('Hello World')
        layout.addWidget(label, 0, 0)

app=QApplication(sys.argv)

screen = window()
screen.show()

sys.exit(app.exec_())
'''
