import pandas as pd
import numpy as np
import matplotlib as plt

path_to_file = "I:\GUC\Random Signals and Noise\data.csv"
data = pd.read_csv(path_to_file)
df = pd.DataFrame(data)

print("The Ddat fields\n==========================================================")
print(df)
print("==========================================================\n")
print("The Ddta types\n==========================================================")
print(df.dtypes)
print("==========================================================\n")
df.isnull()

print("no. of categories : ",len(df.columns),"\n==========================================================")
