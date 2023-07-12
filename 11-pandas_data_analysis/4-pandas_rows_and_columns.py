import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3), index=["A", "B", "C"], columns=["Col1", "Col2", "Col3"])

result = df

result = df["Col1"]

result = df[["Col1", "Col2"]]

result = df.loc['A']

#usage of loc --> loc["row", "column"] => loc["row"] -> loc[ :, "column"]

result = df.loc[:, "Col2"]
result = df.loc[:, ["Col1", "Col2"]]
result = df.loc[:, "Col1":"Col3"]
result = df.loc[:, :"Col3"]
result = df.loc["A", ["Col2", "Col1"]]

df["Col4"] = pd.Series(randn(3), ['A', 'B', 'C'])
df["Col5"] = df["Col1"] + df["Col2"]

#print(df.drop("Col5", axis=1))

print(df)

#print(result)