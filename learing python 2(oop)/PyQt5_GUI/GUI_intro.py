#GUI intro . yo code garo dekheye pani most of it is just boiler plate

#YO tala ko 3ta line matra actual code ho,baki sab boiler plate marera sardeda hunxa
#self.setWindowTitle("My GUI")
#self.setGeometry(0,0,500,500)     #here the brackets means -> (x_axis, Y_axis, width, height)
#self.setWindowIcon(QIcon("GUI_INTRODUCTION/favicon.png"))    #yei line ko lagi PyQt5.QtGui import gareko




import sys     #print(sys.argv)  # Prints a list of command-line arguments
from PyQt5.QtWidgets import QApplication, QMainWindow

#from PyQt5.QtWidgets import QApplications, QMainWindow
from PyQt5.QtGui import QIcon   #this line is only required if we want an icon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
       # self.setGeometry(0,0,500,500)     #here the brackets means -> (x_axis, Y_axis, width, height)
        #self.showFullScreen()            # Makes the window cover the full screen(without closing button) so  it is bad

#this is how to make the concsole full screen with closing button
        screen_resolution = QApplication.desktop().screenGeometry()
        width = screen_resolution.width()
        height = screen_resolution.height()
        # You can adjust the geometry here to have padding if needed
        self.setGeometry(0, 0, width, height)
        self.setWindowIcon(QIcon("PyQt5_GUI/icon.png"))    #yei line ko lagi PyQt5.QtGui import gareko
        
       
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())

if __name__ == "__main__":
    main()