
# opening a file to read

file1 = open("example_file.txt","r") # opening the file for reading "r", writing "w" or append "a"

print(file1.name,file1.mode)         # file data attributes

file1.close()                        # closing the file

# with open command is similar but always close the file automatically
# e.g.

with open("example_file.txt","r") as file1:

    file_stuff1 = file1.readlines(2) # reads only line 1 and printts the firt 10 characteres

    file_stuff2 = file1.readlines(7) #reads the second line and prints the first 5 chararcters

# as soon as you leave the idented block the file is automatically open

print(file_stuff1)
print(file_stuff2)

#opening file to write

lines = ["Line A\n", "Line B\n", "Line C\n"]

with open("example_file.txt","a") as file2:
     for line in lines:
        file2.write(line)