# EX-12: Read-from-CSV

## AIM:
To write a python program to read contents from a CSV file.
## ALGORITHM:
### Step 1:
Import pandas module as pd.
### Step 2:
Using pd.read_csv() method read the CSV file.
### Step 3:
Using df.head() print the first 10 rows of the CSV file.
### Step 4:
Using df.tail() print the last 5 rows of the CSV file
### Step 5:
Using len(df.axes[]) print the toatal number of rows and columns with argyment 0 for row and argument 1 for column.
## PROGRAM:
```
'''
Program to read contents from a CSV file.
Developed By:Keerthana S
Register Number: 23013398
'''
import pandas as pd
f = pd.read_csv('nba.csv')
print(f.head(10))
print(f.tail())
print('Number of Rows:', len(f.axes[0]))
print('Number of Columns:', len(f.axes[1]))

```
## OUTPUT:
![Screenshot 2023-12-23 133300](https://github.com/KeerthanaaSaravanan/EX-12_Read-from-CSV/assets/145742596/224fa1c5-211b-4b37-bf2e-586688f6e0ed)
![Screenshot 2023-12-23 134945](https://github.com/KeerthanaaSaravanan/EX-12_Read-from-CSV/assets/145742596/540639f9-4991-4282-be69-1e46d3705e98)


## RESULT:
The  program successfully reads contents from a CSV file and prints each record. 
