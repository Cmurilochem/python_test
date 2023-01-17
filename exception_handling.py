
try:
    getfile = open("myfile","r")
    getfile.write("My file for exception handling\n")
except IOError:
    print("Unable to open or read the data file\n")
else:
    print("The file was written succefully") 
#finally:
#    getfile.close()
#    print("File is now closed")  

a = 1

try:
    b = int(input("Please, enter a number to divide a\n"))
    a = a/b # code to try to execute
except ZeroDivisionError:
    print("Numbers cannot be divided by zero") #code to execute if you are diving by zero
except ValueError:
    print("You did not provide a number") # code to execute if you do no provide a number
except:
    print("Something went wrong") # code to execute if other exception occured
else:
    print("Success a=",a) # code to execute if there is no problem
finally:
    print("Final of try") # code to execute no matter what       
