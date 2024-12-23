#duck-typing :- It is another way of achiving polymerphism without inheritance
#Python doesn’t check the type of car or person. It only cares whether the object has the required move method. This is the essence of duck typing.
#Objects must have minimum necessary attributes/methods
class car:
    alive = False
    def move(self):
        print ("car can move")

class person:
    alive = True
    def move(self):
        print ("A person can also move")

class tree:
    alive = True
    def stay(self):
        print ("A tree can't move") 

moves = [car(), person(), tree()] 
for obj in moves:
    obj.move()   
    print (obj.alive)                   