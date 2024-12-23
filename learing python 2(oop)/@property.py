# @property -> used to add additional logic to data members.
#            ->types = getter, setter, and deleter
#The names length and breadth can't be used as both attributes and properties. so we have to make the property attribute protected i.e (length) and (_length)

class rectangle:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    @property
    def length(self):
        return f"{self._length}cm"
    @property
    def breadth(self):
        return f"{self._breadth}cm"
    


    @length.setter
    def length(self, new_length):
        if new_length>0:
            self._length = new_length
        else:
            print ("Length must be greater than zero")

    

obj1 = rectangle(2,5)
obj1.length =-1
print (obj1.length)
