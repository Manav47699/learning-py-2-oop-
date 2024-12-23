#buttons!!
#Note -> yo code ma jastai "MainWindow" ma 2 ta function/method cha bhane euta method ma banako objects(e.g button) lai arko method le chindaina. So we have to call every object with "self." prefix(e.g. self.button)


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout     #these are not necessay, only used for allignment
#from PyQt5.QtGui import QIcon
#from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setGeometry(0,0,500,500)


        self.button = QPushButton("Click here!", self)
        self.button.setStyleSheet("color: golden;"
                             "background-color: red;"
                             "border-radius: 30px;"
                             "height: 100px;"
                             "border: solid;"
                             "border-size: 10px;")
        self.button.clicked.connect(self.on_clicking)

        self.label = QLabel("Please click this button -->>", self)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.button)

        central_widget = QWidget(self)
        central_widget.setLayout(hbox)

        self.setCentralWidget(central_widget)

    def on_clicking(self):
        self.label.setText("Thank you")    
        print ("button clicked")
        self.button.setDisabled(True)
        




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()