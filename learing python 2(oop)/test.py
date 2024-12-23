import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create widgets
        self.button1 = QPushButton("Start", self)
        self.button2 = QPushButton("Stop", self)
        self.button3 = QPushButton("Reset", self)
        self.label = QLabel("00:00:00", self)
        self.timer = QTimer(self)

        # Set label alignment to center
        self.label.setAlignment(Qt.AlignCenter)

        # Window setup
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Stopwatch")

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout
        vbox = QVBoxLayout()
        
        # Add the label to the vertical layout
        vbox.addWidget(self.label)

        # Create a horizontal layout for buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Add the button layout (hbox) to the vertical layout (vbox)
        vbox.addLayout(hbox)

        # Set layout for central widget
        central_widget.setLayout(vbox)

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
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
