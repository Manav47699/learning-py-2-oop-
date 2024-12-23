#import QPixmap from PyQt5.QtGui -> this allows loading, manupilating and displaying images 
# we also need Qlabel from PyQt5.QtWidgets
# we put the image path in 
#ALSO, this code puts the image on the center





import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap  



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500 ,500)


        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("PyQt5_GUI/pur_logo.png")
        label.setPixmap(pixmap)

       # label.setScaledContents(True)     #this line make our image the size of our label objects

        label.setGeometry((self.width() - label.width()) //2,     #//2 means integer divison. Yo hamile img lai center ma lagna khojeko. /2 matra garo bhane float value aanu sakxa meaning it will not be the center. so we do //2
                          (self.height() - label.height()) //2,
                          label.width(), label.height())







def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()