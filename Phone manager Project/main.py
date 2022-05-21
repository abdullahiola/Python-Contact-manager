#from PyQt5.Qtcore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui import *
import sys 
import phonenumber as pm

class main(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.searchBtn.clicked.connect(self.search)
        self.ui.SearchBar.textChanged.connect(self.search)

        all_contacts=pm.get_all_contact()
        for contact in all_contacts:
            self.ui.contactList.addItem(f"{contact.firstname.capitalize()} {contact.lastname.capitalize()}")
        
    def search(self):
        search_value =self.ui.SearchBar.text()
        result=pm.search_contact(search_value)
        self.ui.contactList.clear()
        for contact in result:
            self.ui.contactList.addItem(f"{contact.firstname.capitalize()} {contact.lastname.capitalize()}")
        


app=QApplication(sys.argv)
window=main()
window.show()

sys.exit(app.exec_())