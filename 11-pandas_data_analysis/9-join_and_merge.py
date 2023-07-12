import pandas as pd

customers = {
    "CustomerId":[1, 2, 3, 4],
    "First Name" : ['Michael', 'John', 'Rachel', 'Will'],
    "Last Name" : ['Brown', 'Green', 'Blue', 'Purple']
}

orders = {
    'OrderId' : [10, 11, 12, 13],
    'CustomerId' : [1, 2, 5, 7],
    'Order Date' : [2013, 2012, 2010, 2018]
}
df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)
#print(df_customers)
#print(df_orders)
result = pd.merge(df_customers, df_orders, how='inner')
result = pd.merge(df_customers, df_orders, how='left')
result = pd.merge(df_customers, df_orders, how='right')
result = pd.merge(df_customers, df_orders, how='outer')
result = pd.merge(df_customers, df_orders, how='cross')

result = pd.concat([df_customers, df_orders], ignore_index=True)
result = pd.concat([df_customers, df_orders], axis=1)

print(result)