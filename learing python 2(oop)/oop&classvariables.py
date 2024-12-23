#python object oriented programming and class variables(instance and class variable)
#this code contains how to use class, constructors, methods and objects in python oop
class students:
    batch = 2080                  #this is a class variable(i.e. declared outside a constructor)
    numof_obj = 0                  #................this is a class variable used to print the number of objects of this class


    def __init__(self, name, roll_no, address):   #this is contructor i.e it initializes the values  #bracket bhitra ko parameter haru data members ho
        self.name = name 
        self.roll_no = roll_no
        self.address = address
        students.numof_obj += 1                   #................(syntax socha na yeslai)
    def  study(self):                             #this is a method i.e.class bhitra ko function
        print (f"Name = {self.name}||Roll no = {self.roll_no}||Adress = {self.address}||")      #printing instance variable(those inside a constructor)
        print (f"Batch {self.batch}")                                                            #printing class variable(those outside a constructor)
 
#below is how we create an object. here std1, std2, std3 are objects of student class       
std1 = students("Manav", 41, "dharan")
std2 = students("Mausam", 45, "dharan")
std3 = students("himal", 34, "Jhapa")

std1.study()        #calling the method of student class using object of the same class
std2.study()
std3.study()

print (f"The total number of students(objects) = {students.numof_obj}")        #as it is also a class variable, we prefer to call it directly by the class name i.e. students

print ("IT IS CONSIDERED A GOOD PRACTICE TO CALL A CLASS VARIABLE DIRECTLY WITH THE CALL NAME INSTEAD OF A CLASS VARIABLE(AS ALL CLASS VARIBALE PRINTS THE SAME THING) FOR BETTER READBILTY")
print (f"{students.batch}")     #better
print (f"{std1.batch}")          #also works but confusing


