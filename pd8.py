'''
Arregate function = Reduces a set a values into a single summary value
                    Used to summarize and analyze  data
                    Often used with the groupby() function
'''
import pandas as pd

df = pd.read_csv("pokemon-data.csv")

print(df.head())
print(60*"=")
print(df.head())










      
#print(60*"=")











# Whole Dataframe
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())


# Single column
#print(df["Height"].mean())
#print(df["Height"].sum())
#print(df["Height"].min())
#print(df["Height"].max())
#print(df.count())

'''
group = df.groupby("Type1")

#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())
#print(group["Height"].count())
'''

  
