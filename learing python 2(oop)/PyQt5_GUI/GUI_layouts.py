# layout types -> vertical, horizontal and 




import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
#from PyQt5.QtGui import QIcon




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)

#It is a common practice to make a sepreate function named initUI(self): and calling it on the constructor to organize the code

        self.initUI()        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)      #""bhitra ko just numbering matra ho. run garda each label bhitra dekhinxa
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
       

        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: green")
        label4.setStyleSheet("background-color: yellow")

        #vbox = QVBoxLayout()        #to keep the labels verically
        #hbox = QHBoxLayout()         #to keep the label horizontally
        grid = QGridLayout()

        #vbox.addWidget(label1)         ->this would be the code for QVBoxLayout() function
        grid.addWidget(label1, 0, 0)       #inside brakets -> (label_name, row_in_grid, column_in_grid)
        grid.addWidget(label2, 1, 1)
        grid.addWidget(label3, 1, 2)
        grid.addWidget(label4, 3, 2)

        central_widget.setLayout(grid)




        







def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec ())
if __name__ == "__main__":
    main()