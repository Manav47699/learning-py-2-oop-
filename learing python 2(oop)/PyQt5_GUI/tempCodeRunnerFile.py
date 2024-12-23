def button_changed(self):
        radio_button = self.sender()         #radio_button is just a local variable     #sender() function detects which button was toogled
        if radio_button.isChecked():          #isChecked is a bulit-in function
            print (f"{radio_button.text()} is selected")
