import pandas as pd
import numpy as np

serie = np.random.randint(10, 150, 75).reshape(15, 5)

data_frame = pd.DataFrame(serie, columns=["Col1", "Col2", "Col3", "Col4", "Col5"])

result = data_frame.columns
result = data_frame.head()
result = data_frame.head(3)
result = data_frame.head(8)
result = data_frame.tail()
result = data_frame.tail(3)
result = data_frame["Col1"].head(4)
result = data_frame[["Col1", "Col2"]].head(3)
result = data_frame[5:15][["Col1", "Col2"]].head(4)
result = data_frame > 5
result = data_frame[data_frame > 60]
result = data_frame[data_frame%2 == 0]
result = data_frame[(data_frame > 60) & (data_frame%2 == 0)]
result = data_frame[(data_frame > 60) & (data_frame%2 == 0)]["Col2"]

print(result)
