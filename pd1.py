'''
Series = A Pandas 1-Dimensional labeled array that can hold any data type
         Think of it like a single column in a spreadsheet (1-Dimensional)
'''
import pandas as pd

#data = [100, 102, 104, 200, 202]
data = [100.1, 102.3, 104.2]
#data = ["A", "B", "C"]
#data = [True, False, True]

series = pd.Series(data)
#series = pd.Series(data, index=["apartment #1","apartment #2","apartment #3"])
#series = pd.Series(data, index=["a","b","c","d","e"])

#series.loc["c"] = 200

print(series)
#print(series.loc["a"])
#print(series.iloc[1])
#print(series[series < 200])
#print(series[series >= 200])

 