# Selection 

import pandas as pd

df = pd.read_csv("pokemon-data.csv")

#print(df)


#==" SELECTION BY COLUMN "==
#print(df["Name"])
#print(df["Name"].to_string())
#print(df["Height"].to_string())
#print(df["Weight"].to_string())
#print(df[["Name", "Height", "Weight"]])
#print(df[["Name", "Height", "Weight"]].to_string())



df = pd.read_csv("pokemon-data.csv", index_col="Name")


#==" SELECTION BY ROW/S "==
#print(df.loc[0])
#print(df.loc["Pikachu"])
#print(df.loc["Charizard", ["Height", "Weight"]])
#print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
#print(df.iloc[0:11])
#print(df.iloc[0:11:2])
#print(df.iloc[0:11:2, 0:3])
 

