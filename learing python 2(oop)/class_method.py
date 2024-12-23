#class method -> Used for operataions related to the class it self (eg;- number of objects of the class)
#              -> Its first parameter is (cls) unlike (self) for instance method

class students:
    std_no = 0              #these are class varibales
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        students.total_gpa += self.gpa
        students.std_no += 1
       

    def display(self):
        print (f"{self.name} = {self.gpa} gpa")


    @classmethod
    def std_info(cls):                           #this is class method
        print (f"The total number of students = {cls.std_no}")
        avg_gpa = cls.total_gpa/cls.std_no
        print (f"The average gpa of the class is = {avg_gpa}")


std1 = students("manav", 3.1)
std2= students("amusam", 3.6)
std3 = students("himal", 3.7)

std1.display()
std2.display()
std3.display()

students.std_info()
   

    