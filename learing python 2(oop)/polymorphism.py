#polymorphism can be achived by 2ways. They are
#by inheritance &  [this code]
#by duck typing



#1st code is the example of polymerphism by inhertance
import math

class shapes:
    pass
    #def __init__(self, area):     #yo tala inherit vayo vhane ta area(which we are calculating) ta input nai dinu paro nita. constructor ho nita
     #   self.area = area

    #def area(self):
        #print (f"area = {self.area}")    
        #pass
        
class circle(shapes):
    def __init__(self, radius):
        #super().__init__(area)
        self.radius = radius
    def area(self):
        return math.pi * pow(self.radius, 2)

class rectangle(shapes):
    def __init__(self, length, breadth):
        #super().__init__(area)
        self.length = length
        self.breadth = breadth
    def area (self):
        return self.length * self.breadth
    
class roti(circle):
    pass
    
shapes = [circle(3), rectangle(5, 6), roti(5)]
result = [shape.area() for shape in shapes]
print (f"Area of circle, rectangle and roti respectively ={result}")


print('.........................................')

#2nd code (below) is an example of polymerphism by method overwritting

        
class circle:
    def __init__(self, radius):
        #super().__init__(area)
        self.radius = radius
    def area(self):
        return math.pi * pow(self.radius, 2)

class rectangle:
    def __init__(self, length, breadth):
        #super().__init__(area)
        self.length = length
        self.breadth = breadth
    def area (self):
        return self.length * self.breadth
    
#class roti(circle):
  #  pass
    
shapes = [circle(3), rectangle(5, 6)]       #here shape is an object of lists-type
result = [shape.area() for shape in shapes]
print (f"Area of circle, rectangle respectively = {result}")

