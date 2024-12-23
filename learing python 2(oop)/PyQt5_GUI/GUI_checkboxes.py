#checkboxes


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt        #this is for state == Qt.Checked function

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0,0,500,500)


        self.checkbox = QCheckBox("Bar-Graph", self)
        self.checkbox.setStyleSheet("font-size: 40px;"
                                    "font-family: Arial;")
        self.checkbox.setGeometry(0,0,250,250)
        #self.checkbox.setChecked(True)       #this funtion will make the checkbox checked by default
        self.checkbox.stateChanged.connect(self.checkbox_checked)

#in checkbox_checked, state parameter is not essential i.e code works without it. But is is good practice to let the user know that they have checked or unchecked something
    def checkbox_checked(self, state):     # state == 2 when checked and ==0 when unchecked
        #print (state)
        if state == Qt.Checked:             #Qt.Checked is a bulit-in function to see if the checkbox is checked. We can also do state ==2, but that is less readable
            print("bargraph added")        #printed when check is added
        else:
            print("bargraph removed")       #printed when check is removed





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()