#multiple inheritance = a child class inheritating from more than 1 base class
#hiarchical inhertance = a parent class in more than 1 child class
#multi_level inheritance = 3 or more generations (grandparent-->parents-->children...)
#this is code:-
#multiple = child class as it is taking from 2 parent classes
#hiarchical = grandparent class as it is giving to both parents
#multilevel = grandparent --> parent1 & parent2 --> child

class grandparent:
    def __init__(self, eye_color):
        self.eye_color = eye_color

    def display(self):
        #print (f"Displaying from the method of grandparent class = {self.eye_color}")
        print (f"{self.eye_color}")

class parent1(grandparent):
    pass
class parent2(grandparent):
    pass
class child(parent1,parent2):          
    pass
    
color = child("blue")
color.display()                          #using object to call method
print (f"{color.eye_color}")             #using object to call data member
#print (f"Calling from the object of child class. {color.display()}")   #yo line ma 2 choti print bhako xa so euta ma "none" bhanera auxa hola
#print (f"Calling from the object of child class. {color.eye_color}")



