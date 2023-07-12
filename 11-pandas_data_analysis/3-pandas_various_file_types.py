import pandas as pd
import sqlite3

df = pd.read_csv('mlb_teams_2012.csv')
#print(df)

df = pd.read_json('dwsample.json', typ="series")
#print(df)

df = pd.read_excel('excel_sample.xlsx')
#print(df)

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")

#print(cursor.fetchall())
df = pd.read_sql('SELECT * FROM customers', connection)
print(df)
df = pd.read_sql('SELECT * FROM invoices', connection)
#print(df)