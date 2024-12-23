#inheritance = Allows a class to inherit data members and methods from another class
#here parentclass = students & children = manav, mausam, himal
class students:
    facuilty= "BCT"
    def __init__(self, height):
        self.handsome= True
        self.height = height
    
    def display(self):
        print (f"Handsome = {self.handsome}, height = {self.height}")
        print (f"Facuilty = {students.facuilty}")

class manav(students):
    grade = "3.1"

class mausam(students):
    grade = "3.6"
class himal(students):
    grade = "3.6"


info1 = manav(6.2)
info2 = mausam(5.9)
info3 = himal(5.6)

info1.display()
info2.display()
info3.display()


        