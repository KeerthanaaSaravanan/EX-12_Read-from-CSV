import pandas as pd
f = pd.read_csv('nba.csv')
print(f.head(10))
print(f.tail())
print('Number of Rows:', len(f.axes[0]))
print('Number of Columns:', len(f.axes[1]))
