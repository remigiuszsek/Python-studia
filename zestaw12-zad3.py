import pandas as pd

myfile = pd.read_csv('dosw12.csv', sep=';')
print(myfile)

# delete where Zmienna1 is not a number

myfile.drop([9], inplace=True)
myfile.drop([30], inplace=True)
print(myfile)