import pandas as pd

"""
s1 = pd.Series([3, 2, 1, 0])
s2 = pd.Series([12, 32, 43, 15])
data = dict(apples=s1, oranges=s2)
df = pd.DataFrame(data)
print(df)
"""

df = pd.DataFrame()
print(df)
df = pd.DataFrame([7, 5, 9, 8])
print(df)
data = [['michael',5], ['john',70], ['rachel', 60]]
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data, index=[1, 2, 3], columns=['Name', 'Score'])
print(df)

dicti = {"name":['michael', 'john', 'rachel'], "scores":[5, 70, 60]}
df = pd.DataFrame(dicti)
print(df)

df = pd.DataFrame(dicti, index=[320, 231, 534])
print(df)

dict_list = [
    {"Name":"Michael", "Grade":50},
     {"Name":"John", "Grade":60},
      {"Name":"Rachel", "Grade":60} ]
df = pd.DataFrame(dict_list, index=[1, 2, 3])
print(df)