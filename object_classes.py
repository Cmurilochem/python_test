import math 

# example of how to construct a class

class Circle(object):
    
    # Constructor
    def __init__(self,radius,color): # telling python you are making a new class - the "def __init__(self" part is a standard definition
        self.radius = radius; # data attribute 1
        self.color = color;   # data attribute 2

    # Method
    def add_radius(self,r): # this a method of the class
        self.radius = self.radius + r   
        return self.radius

    # Method
    def area(self):
        a = (math.pi * (self.radius)**2)     
        return a

class Rectangle(object):

    # Constructor

    def __init__(self,color,height,width): # Constructor of the class
        self.color = color; # data attribute 1
        self.height = height; # data attribute 2
        self.width = width;   # data attribute 3

    def area(self):
        a = self.height * self.width
        return a    

# Done

myCircle = Circle(10,"blue") # creating an object/instance of the Circle class

#myCircle.radius = 1 # you can change the data attributes if you want

myCircle.add_radius(2)

print(myCircle.color,myCircle.radius,myCircle.area())  

myRect = Rectangle("blue",10,10)

print(myRect.area())
