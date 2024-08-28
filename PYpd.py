#Pandas allows us to analyze big data and make conclusions based on statistical theories.

#Pandas can clean messy data sets, and make them readable and relevant.

#Relevant data is very important in data science.

#the difference between panda and python is that in panda when slicing the last value is also included whereas in python the last value is not included but when using iloc the last position will again not get included

import pandas as pd
import numpy as np
data = {
    "Name" : ['Monkey D Luffy','Naruto uzumaki','Ichigo','Saitama'],
    "Anime": ['One piece','Naruto','Bleach','One punch man'],
    "Profession": ['Pirate','Ninja','Soul reaper','Superhero'],
    "Powerlevel": [700,800,1000,1000]
}
df = pd.DataFrame(data)#Prints in a clean and sorted form in excel
print(df)




excelpath = 'Anime.xlsx'
df.to_excel(excelpath)#will transfer the data in excel file
df.to_excel(excelpath,index=False)#will tansfer the data in excel without showing the index values in file
print(df.tail()) #will print the last two indexes of list
print(df.head()) #will print the starting 2 indexex of list
print(df.describe()) #will perform statistical functions on numerical values present in the list

#dummy1 = pd.read_csv("dummy.xlsx") #will print excel data in terminal
#dummy['the thing you want to change'] = 'any value'
ser = pd.Series(np.random.rand(6))
print(ser)
print(ser.dtypes) #will print the data types of data,if it will contain even one string it will print as object if not it will print float
print(ser.describe) 
print(type(ser))
ser[5] = "OK"
print(ser)
print(ser.dtypes)
serr = pd.DataFrame(np.random.rand(10,5), index=np.arange(10)) #10 rows,5 columns
print(serr)
print(serr.describe)
print(serr.dtypes)
serr[0][3] = "kallu" #column,rows
print(serr.dtypes)
print(serr)
print(serr.index)
print(serr.columns)
print(serr.T)#Transpose
print(serr.sort_index(axis=0,ascending=False)) #will sort the array in descending order
print(serr.sort_index(axis=1,ascending=False)) 
#VIEW = it doesnt copy but if the new value make changes old will also get changed
serr2 = serr
print(serr)
serr2[0][3] = 6.9
print(serr)
#COPY = remains constant after copying
serr2 = serr.copy() #or  serr[:]
serr2[0][3] = 'sdnsdkn'
print(serr)
serr2.loc[0][3] = 0 #nothing will happen
print(serr)
sur = pd.DataFrame(np.random.rand(5,10),index=np.arange(5))
sur.loc[3][2] = 2342 #The loc property gets, or sets, the value(s) of the specified labels. Specify both row and column with a label.
print(sur)
sur.columns = list('ABCDEFGHIJ')
sur.loc[3,'C'] = 2
print(sur)
sur.loc[3,0] = 'ads' #will make an new column as there is no column named 'O' to access
print(sur)
print(sur.head(2))
surr = sur.drop(0,axis=1) #removing a certain row or column
print(surr.loc[[2,4],['E','I']]) #nothing will be changed from the dataframe we are just seeing/accessing it
print(surr.loc[[1,2],:]) #rest of the columns
sur1 = sur.loc[(sur['A']<0.3) & (sur['C']>0.1)] #will print indexes and columns according to conditions
print(sur1)#here A is less than 0.3 and C is more than 0.1
#iloc = use it if your indexes are numbers  use loc if your indexes name are strings
#we can use iloc even if the name of the rows or columns are given in string whereas in loc we have to enter specific name to access it
print(sur.head(3))
print(sur.iloc[0,5]) #will print oth row and 5th column
print(sur.iloc[[3,4],[6,7]])
print(sur.drop(['B','C'],axis=1))
print(sur.drop(['H'],axis=1,inplace=True)) #With inplace in this it drops it permanently fom the real dataframe
print(sur.drop([1,3],axis=0,inplace=True))
print(sur.reset_index())#it will reset all the index from 0 with an extra column at the start(it doesnt bring backs the dropped columns and indexes)
print(sur.reset_index(drop=True,inplace=True)) #it will remove the index column
print(sur.isnull())#prints true when the column or data is empty or zero otherwise false
sur2  = sur.loc[:, ['B']] = None
print(sur2)
sur3  = sur.loc[:, ['B']] = 56
print(sur3)
data = {
    "Name" : ['Monkey D Luffy','Naruto uzumaki','Ichigo','Ichigo'],
    "Anime": ['One piece','Naruto','Bleach','One punch man'],
    "Profession": ['Pirate','Ninja','Soul reaper','Superhero'],
    "Powerlevel": [700,0,1000,np.nan]
}
df = pd.DataFrame(data)
print(df)
print(df.dropna()) #it wil drop the whole column and row along with the empty index even if only one index is empty
print(df.dropna(how='all')) #it will only drop the whole column and row if all the rows and column are empty/NA
print(df.drop_duplicates(subset=['Name']))
print(df.drop_duplicates(subset=['Name'],keep='first')) #Nothing will happen because by default the first data stays
print(df.drop_duplicates(subset=['Name'],keep=False)) #the after data will stay the first one will be dropped
print(df.shape)
print(df.info)
print(df['Powerlevel'].value_counts(dropna=True)) #it will drop the na values and give unique values
print(df['Powerlevel'].value_counts(dropna=False)) #it will not and give unique values
print(df.notnull())
print(df.isnull())
df['Powerlevel'].fillna(1000,inplace=True) #fills the empty cells
print(df)
df2  = {
    "NAME": ['Sand','Portal','Quake','Leopard','Control','Rubber'],
    "POWERS": ['sand-manipulation','Teleportation','Sea-control','Makes strong','Control anything','properties of rubber'],
    "TYPE": ['Uncommon-logia','legendary','legendary','Zoan-mythcal','Mythical','Rare-Zoan'],
    "USER": ['Sir Crocodile','Blueno','Whitebeard','Rob Lucci','Traflagar D. water law','Monkey D. Luffy'],
    "PRICE(beli)":[420000.,1900000,1000000, 500000, 3200000, 750000]
}
df3 = pd.DataFrame(df2)

a2 = 'anime2.xlsx'
df3.to_excel(a2)
rd = pd.DataFrame(np.random.rand(6,6))
print(rd)

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar1 = pd.Series(calories)

print(myvar1)
print(pd.options.display.max_rows)
pd.options.display.max_rows = 9999 #displays more rows than capacity
rd1 = pd.read_excel('dummy.xlsx')
print(rd1)
rd1.fillna(1000,inplace=True) #comes in handy when we have to fill only one value for all empty cells
print(rd1)

