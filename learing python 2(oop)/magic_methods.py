#magic methods -> Used to customize objects
#               -> __str__(self), __gt__(self), __add__(self)  and so on

class phones:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):           #object lai print garda address auxa generally. But with this we can show what ever we want.
        return f"{self.name} = Rs. {self.price} "
        
    def __add__(self, other):
        return self.price + other.price
    
    def __getitem__(self, keyword):
        if keyword == "name":
            return self.name
        elif keyword == "price":
            return self.price
    
phone1 = phones("Samsung", 30000)  
phone2 = phones("apple", 100000)
phone3 = phones("vivo", 25000)

print (phone1)                   #__str__(self)

print (phone1.price+phone2.price)            #__add__(self)
#print (phone1+phone2+phone3)      #this is not possible as mathi add function ma hamile 2ta matra jodeko chau. To add more than 2 do as below

total_price = phone1+phone2
total_price += phone3.price       #as "phone3" as a string as wel, we have to specify the data member (price) as well
print (total_price)


print(phone1['name'], phone2["name"], phone3["price"])    #__getitem(self)