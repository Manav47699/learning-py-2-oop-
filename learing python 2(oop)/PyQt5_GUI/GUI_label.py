# QLabel is a widget used to display text or images within a graphical user interface (GUI).
# we have to import QLabel from PyQt5.QtWidgets



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt     #for allignment





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0, 500, 500)

        label= QLabel("hello",self)   #here self points to windoes (syntax)
        label.setFont(QFont("Arial", 50))               #we have to import QFonts for this function
        label.setGeometry(0, 0, 500, 500)
        label.setStyleSheet("color: green;"       #This is same like css
                            "background-color: blue;"
                            "font-weight: bold;"
                            "font-style:itallic;"
                            "text-decoration: underline;")
        
       # label.setAlignment(Qt.AlignTop)    
       # label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)    #vertical center
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignHCenter)    #horizontal center
        #label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()