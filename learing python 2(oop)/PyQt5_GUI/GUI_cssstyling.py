#we can apply css to any element in our program by putting them inside ("""  {}  {} """)
#no need to give "" to each css eg font: solid; instead of "font: solid;"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt     #for alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(0,0, 500, 500)


        self.button1 = QPushButton("button1",self)
        self.button2 = QPushButton("button2",self)

#this is like giving individual id which is necessary in CSS
        self.button1.setObjectName("b1")
        self.button2.setObjectName("b2")

        self.button1.setGeometry(0,0, 60, 30)
        self.button2.setGeometry(100, 0, 60, 30)


#this line does not work because alignment only works for QLabel elements. 
        #self.button1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setStyleSheet("""
            QPushButton {
                           width: 100px;
                           height: 30px;
                           border-radius: 40px;
                           border: 5px solid black;}

            QPushButton#b1 {
                           background-color: blue;}

            QPushButton#b2:hover {
                           background-color: red;}
        """)
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()