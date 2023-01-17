import pandas as pd

list = ["red","yellow","blue","magenta","brown","orange","orange","orange"] # list

#print(pd.Series(list))

for i in range(len(list)): # running over the indexes and lokking for the yellow color
    if (list[i]=="yellow"):
        list[i]="white"

for i,element in enumerate(list): # this is a very interesting example where you can print the indexes for each color 
    print(i,element)        

new_list = []
i=0

while (i < len(list)): # test using while
    if (list[i]=="orange"):
        new_list.append(list[i])
        print(i)
    i=i+1


print(list,new_list)    