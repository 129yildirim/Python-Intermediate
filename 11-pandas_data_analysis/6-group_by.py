import pandas as pd
import numpy as np

df = pd.read_excel('excel_sample.xlsx')

print('Columns are:\t', df.columns)
result = df
result = df[["First Name", "Age"]]

result = df.groupby(["Country", "Gender"]).groups

"""
for name, group in df.groupby("Country"):
    print(name)
    print(group)
"""

result = df.groupby("Country").get_group("France")
result = df.groupby("Gender").get_group("Male")

result = df.groupby("Country")["Age"].sum()
result = df.groupby("Country")["Age"].mean()
result = df.groupby("Gender")["Age"].mean()
result = df.groupby("Country")["Id"].count()
result = df.groupby("Country")["Age"].max()
result = df.groupby("Country")["Age"].max()["Great Britain"]

result = df.groupby("Country")["Age"].agg(np.mean)
result = df.groupby("Country")["Age"].agg([np.mean, np.max, np.min, np.sum])
result = df.groupby("Country")["Age"].agg([np.mean, np.max, np.min, np.sum]).loc["United States"]

print(result)