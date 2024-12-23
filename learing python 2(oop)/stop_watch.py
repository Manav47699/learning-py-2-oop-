#stop_watch 
#INCOMPLETE (backend baki xa)


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
#from PyQt5.QtGui import QIcon  


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):
        self.button1 = QPushButton("Start", self)
        self.button2 = QPushButton("Stop" ,self)
        self.button3 = QPushButton("Reset", self)
        self.label = QLabel("00:00:00", self)
        self.timer = QTimer(self)
        
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Stop-watch")

        central_widget = QWidget()                  #creating obj
        self.setCentralWidget(central_widget) 

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.label)       
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        vbox.addLayout(hbox)               ## Add the button layout (hbox) to the vertical layout (vbox)
        central_widget.setLayout(vbox)     #we have to call vbox now as hbox ni vbox bhitrai aako xa nita mathi ko line ma

        self.label.setAlignment(Qt.AlignCenter)      #Putting the label at the center of our console

        self.setStyleSheet("""
            QPushButton{
                           border: 5px double black;
                           font-size: 40px;
                           border-radius: 20px;
                           background-color: green;}
            QLabel{
                           font-size: 100px;
                           background-color: blue;
                           color: white;
                           border-radius: 30px;
                           border: 3px solid black;}
            QPushButton:hover{
                           font-weight: bold;}
        """)

        #self.start.clicked.connect(self.start)
        #self.reset.clicked.connect(self.reset)
        #self.stop.clicked.connect(self.stop)
        

    def start(self):
        pass
    def reset(self):
        pass
    def stop(self):
        pass

        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()