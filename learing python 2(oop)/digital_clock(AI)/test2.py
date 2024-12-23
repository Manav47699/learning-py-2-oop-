# time_gui.py

import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
import time_module

class TimeDisplay(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 300, 200)

        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)  # Update every second

    def show_time(self):
        current_time = time_module.get_current_time()
        self.label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimeDisplay()
    ex.show()
    sys.exit(app.exec_())
