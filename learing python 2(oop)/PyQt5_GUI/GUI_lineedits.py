#line edits --> text box (same thing)
#Q) this code also has a button. On clicking the button somthing happens.
#SO it is not just line edits, thus the code might look long

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton,QLabel
#from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(0,0,500,500)

        self.text_box = QLineEdit(self)
        self.text_box.setGeometry(0,0,500, 20)
        self.text_box.setPlaceholderText("Enter your name here")    #placeholder
        self.text_box.setStyleSheet("font-size: 25px;")

        self.button = QPushButton("click here to submit", self)
        self.button.setGeometry(250, 20, 150, 30)
        self.button.clicked.connect(self.on_clicking)

        self.label = QLabel("", self)                  #making a label that will say noting for now
        self.label.setGeometry(200, 100, 250, 120)

    def on_clicking(self):

        self.label.setText("Your answer has been submitted")

        text = self.text_box.text()     #here "text" variable gets whatever was written in the text box
        print (text)                    #printing "text" to the terminal


        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()