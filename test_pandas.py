import pandas as pd

#####
# reading a csv file 

cvs_path = 'courses.csv'

# store the data as a dataframe 

df = pd.read_csv(cvs_path) 

# using iloc and loc functions

# iloc just needs to element indexes like a matrix
# in loc, you need to put the name of the row, and column

print(df.head(), df.iloc[0,0], df.loc[0,"Course"])

Newdf = df[ ['Price (euro)'] ]

print(Newdf)

# creating a DataFrame from a dictionary

dict = { 'Name':       ['Murilo', 'Simone', 'Rafael', 'Lucas'], 
         'Surname':    ['Rocha','Favarim','Sousa', 'Ruarez'], 
         'Age':        ['34','35','30','45'], 
         'Profession': ['Chemist','Accountant','Pharma','']
       }

df_dict = pd.DataFrame(dict)

print(df_dict.head())

