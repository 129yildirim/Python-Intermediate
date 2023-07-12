import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)

df = pd.DataFrame(data, index=['a', 'c', 'e', 'f', 'g'], columns=['col1', 'col2', 'col3'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

result = df

result = df.drop("col1", axis=1)
result = df.drop(['b', 'd'], axis=0)
result = df.isnull()
result = df.isnull().sum()
result = df["col1"].isnull().sum()

new_column = [np.nan,30,np.nan,51,np.nan,35,np.nan]
df["col4"] = new_column

result = df
result = df["col4"].isnull().sum()
result = df[df["col4"].isnull()]
result = df[df["col4"].notnull()]
result = df[df["col4"].notnull()]["col4"]

result = df.dropna() # if there is a nan in a row, it doesn't show that row. axis=0(default)
result = df.dropna(axis=1)
result = df.dropna(how="any")#default
result = df.dropna(how='all')
result = df.dropna(subset=["col1", "col2", "col3"], how='all')
result = df.dropna(thresh=2) # if there are at least 2 NaN values in that row, drop it.
result = df.fillna("no input")
result = df.fillna(1.0)


print(result)