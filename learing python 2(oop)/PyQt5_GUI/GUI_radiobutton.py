#radio button = same like checkbox but can only select one option


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRadioButton, QButtonGroup    #QButtonGroup groups together 2 different buttons
#from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    

    def initUI(self):
        self.setGeometry(0,0,500, 500)

#creating radio buttons as objects
        self.radio1 = QRadioButton("check", self)
        self.radio2 = QRadioButton("card", self)
        self.radio3 = QRadioButton("cash", self)
        self.radio4 = QRadioButton("pre_payment", self)
        self.radio5 = QRadioButton("post_payment", self)

#css handeko (use this method if there are multiple elements e.g radio buttons in this case)
        self.setStyleSheet("QRadioButton{"
                        "font-size:50px;"
                        "padding: 10px;"
                        "}")
        

#giving each button a sepreate place so that they dont overlap
        self.radio1.setGeometry(0, 0, 300, 100)
        self.radio2.setGeometry(0, 50, 300, 100)
        self.radio3.setGeometry(0, 100, 300, 100)
        self.radio4.setGeometry(0, 150, 400, 100)
        self.radio5.setGeometry(0, 200, 400, 100)

#creating buttongroup for "type of payment"(i.e. 1st 3 radiobuttons) & "time of payment"(4th and 5th radiobutton)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

#assigning each radiobutton to a button_group
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

#connecting each radiobutton to button_changed() function below
        self.radio1.toggled.connect(self.button_changed)
        self.radio2.toggled.connect(self.button_changed)
        self.radio3.toggled.connect(self.button_changed)
        self.radio4.toggled.connect(self.button_changed)
        self.radio5.toggled.connect(self.button_changed)

    def button_changed(self):
        radio_button = self.sender()         #radio_button is just a local variable     #sender() function detects which button was toogled
        if radio_button.isChecked():          #isChecked is a bulit-in function
            print (f"{radio_button} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()