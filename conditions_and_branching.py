
# simple example of if elif else statments

age = int(input("What is your age ?\n")) # input value from command line

print(type(age))    

limit = 18

if (age>limit):

    print("You can enter the AC/DC show")
    print("Move on...")

elif (age==limit):

    print("You can enter the Iron Maiden show")    
    print("Move on...")

else:

    print("You cannot enter")
    print("Fuck off")

# additing or and operators

album_year = 1990

if (album_year<1980) or (album_year>1989):
    print("The album was made in the 70's or 90's")
else:
    print("The album was made in the 80's")

print(1==2,"a"=="A")