
#instance method -> normal methods. called by objects
#static methods -> called directly by class name just like class variables. parameters haru pass garnu parxa
#syntax -> method bhada mathi ko line ma '@staticmethod' lekhdene
#Static methods do not have access to the instance (self) or class (cls)

class my_class:
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
    def print_name(self):
        print (f"name = {self.name}")

    @staticmethod
    def print_age(age):
        print (f"My age is = {age}") 

obj1 = my_class("manav", 25 )   
obj1.print_name()   

my_class.print_age(25)
