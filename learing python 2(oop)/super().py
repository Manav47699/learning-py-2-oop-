#super() = the constructor of parent class is only inherited to the chlid class if the child class doesn't have its own constructor.
#          If the child class has its own constructor, we have to use super() function.

class grandparent:
    def __init__(self, eye_color):
        self.eye_color = eye_color

    def display(self):
        print (f"Displaying from the method of grandparent class = {self.eye_color}")
        print ("........................................")

#class parent1(grandparent):
  #  pass
#class parent2(grandparent):
   # pass
class child(grandparent): 
    def __init__(self, eye_color, skin_color):
        super().__init__(eye_color)             #yo line bhaeyna bhane error aauxa
        self.skin_color = skin_color
    def displaychild(self):
        
        print("displaying from the method to child")
        print(f"eye color = {self.eye_color}.")   
        print(f"skin color = {self.skin_color}")       
    pass
    
ecolor = child("blue", "white")

 
ecolor.display()          #display() -> method of grand father calss
ecolor.displaychild()     #display() -> method of child class

