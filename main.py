import numpy as np
from functions.functions import * 
#from mypackage.module1 import square,double
#from mypackage.module2 import mean
import mypackage as mpcg

list_num = [1,3,2,5,6]

list = ["eu", "tu", "ele", "nos"]

print(list_num[::2])

new_list = sorted(list_num) # organing the list in crescent way using a function

list_num.sort() # organing the list in crescent way using a method of the object

print(new_list,list_num) 

print(my_func(2,2))
print(my_printData())
print(NoWork())
print(printStuff(list_num))

print(printNames("Murilo","Simone","Clezia"))

my_function(fname = "Tobias", lname = "Samet")

#print(help(my_func))

print(mpcg.module1.square(2),mpcg.module1.double(2),mpcg.module2.mean(list_num))

