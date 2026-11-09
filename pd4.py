import pandas as pd 


'''
#JSON
df = pd.read_json("pokemon-data.json")
'''


#CSV
df = pd.read_csv("pokemon-data.csv")

#print(df) 
print(df.to_string()) 