#digital clock
#PyQt5 does not support while loop. So we use QTImer from PyQt5.QtCore to update time at regular interval
"""
import datetime
import time

while True:


    get_time = datetime.datetime.now()
    print(f"\r{get_time}", end=" ", flush=True)
    #get_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print (get_time)
    time.sleep(1)
"""

import datetime
#import time       #this is not needed as we are using QTimer


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setWindowIcon(QIcon("digital_clock_icon.jpg"))


        #self.setGeometry(0, 0, 200, 100)
        #self.setGeometry(self.screen().size().width() - 200, self.screen().size().height() - 100, 200, 100)
#selecting the geometry such that the console appers at the bottom right corner

        screen_geometry = self.screen().availableGeometry()  # Get the screen area excluding taskbars
        self.setGeometry(screen_geometry.width() - 200, screen_geometry.height() - 100, 200, 100)



       
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)  # Center the text in the label

      
        self.label.setStyleSheet("font-size: 30px; font-weight: bold; color: green;")

      
        layout = QVBoxLayout()
        layout.addWidget(self.label)

       
        container = QWidget(self)
        container.setLayout(layout)


        self.setCentralWidget(container)

        self.setStyleSheet("background-color: black;")


#using QTimer to update time
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)     #updates every 1000 miliseconds ie 1 second


    def show_time(self):
#we cant use while loops in pyqt5, so we use QTimer()
        """
        while True:
            current_time = datetime.datetime.now()
            time.sleep(1)
            self.label.setText(current_time)
        """
#we must format the time into a string ans settext() function doesn't take time directly
        get_time = datetime.datetime.now()
        #displayed_time = get_time.strftime("%H:%M:%S AP")
#using %I instead of %H changes the time to 12 hrs format and %p gives am or PM
        displayed_time = get_time.strftime("%I:%M:%S %p")

        self.label.setText(displayed_time)
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

