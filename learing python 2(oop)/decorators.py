#decorator = decorators are used to add something to a function (basefunction) without editing that function
# for this code, "car" is our base function

def add_warrenty(func):                           #this is a decorator
    def wrapper(*args, **kwargs):                 #a wrapper function makes sure that the base function is only printed when it is called. Thus it is important
        print ("You added a 2 years warenty")
        func (*args, **kwargs)
    return wrapper

@add_warrenty                                      #syntax
def car(type):                                     #base function
    print (f"This is your {type} car ")

car("jeep")                                         #calling the base function