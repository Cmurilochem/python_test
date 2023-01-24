def my_func(x,y):
    """ test function """
    z = x**2 + y**2
    return z

def my_printData():
    """ tring function """
    output = "Hey, I am a function"
    return output

def NoWork():
    """ this function do not do anything """
    pass        

def printStuff(stuff):
    """ loop inside a function """
    for i,s in enumerate(stuff):
        print("Index",i,"Number",s)

def printNames(*names): # if you do not know the number of arguments to pass # printNames("Murilo","Simone","Clezia",...,"Antonio")
    """ testing the generic number """
    for name in names:
        print(name)  

def my_function(**kid): # If the number of keyword arguments is unknown # my_function(fname = "Tobias", lname = "Refsnes")
  print("His last name is " + kid["lname"])        

def type_of_album(artist, album, year_released):
    """ test using if and else for return """
    print(artist, album, year_released)
    if (year_released > 1980):
        return "Modern"
    else:
        return "Old"              
