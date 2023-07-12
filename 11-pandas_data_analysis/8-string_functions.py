import pandas as pd

data = pd.read_excel('excel_sample.xlsx')

data.dropna(inplace=True)

data["Last Name"] = data["Last Name"].str.upper()

data["index"] = data["First Name"].str.find('a')

data["Date"] = data["Date"].str.replace('/', '-')

print(data)
print(type(data))
print(type(data[["First Name", "Last Name"]]))
print(type(data["First Name"]))
