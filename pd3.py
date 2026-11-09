'''
DataFrame = A tublar data structure with rows AND colums. (2 Dimensional)
            Similar to an Excel spreadsheet
'''

import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squideward"],
    "Age": [30,35,50]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])


# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]


# Add a new column
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                        index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])

print(df)
#print(df.loc["Employee 1"])
#print(df.iloc[2])