
# compound data types: lists, tuples, dictionaries, and sets

ratings = ("string",10,9,8,5,7) # this is a tuple - the elemets are imutable: it can accept different python data types (int,float,string,boolean)

list = [1,2.0,1000,"pi"] # this is a list - the elements are mutable but like in tuples, it can accept different python data types (int,float,string,boolean) 

list[0] = "my string" # changing an element in a list

ratings = ratings + (("hard", "rock"),10,2.346) # concatenating tuples

list.extend([1,3.14,90]) # extending the list

list.append(["ok", "dude"]) # append just add one nested term in the list

dict = {"Murilo":10, "Simone":100, "Antonio":1000, "Clezia":10} # this is an example of dictionary: keys ("Murilo") are immutable

set1 = {"Eu","Tu","Eles","Nos","Vos","Eles","Eles"} # this is an example of a set: it does not have orders like lists, tuples 
# and dictionaries and does not accept equal elements

set2 = {"Eu","Tu"}

set3 = set1 & set2 # define common elements between set1 and set2

set1.add("They") # adding an element

set1.remove("They") # remove an item 

print(type(ratings),type(list),ratings[6][1],list,list[1:4])

print(" ")

print(dict,dict.keys(),dict.values(),type(dict))

print(" ")

print(set1,type(set1),set3)

#