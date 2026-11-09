'''
Series = A Pandas 1-Dimensional labeled array that can hold any data type
         Think of it like a single column in a spreadsheet (1-Dimensional)
'''
import pandas as pd

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)


#series.loc["Day 3"] += 500

#print(series)
#print(series.loc["Day 1"])
print(series[series >= 2000])
print(series[series < 2000])
