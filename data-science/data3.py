import os
import pandas as pd

os.system('cls')

dt = pd.read_csv('assets/csv/data-python1.csv', header=0, sep=",")

# Clear Nan from data
dt.dropna(axis=0, inplace=True)

# Change dtype object to float
# dt["col1"] = dt["col1"].astype(float)

# For col1
for x in dt["col1"]:
    if(x > 10):
        dt["col1"] = dt["col1"].replace([x], "Lebih")

# For col2
for x in dt["col2"]:
    if(x > 10):
        dt["col2"] = dt["col2"].replace([x], "Lebih")

# For col3
for x in dt["col3"]:
    if(x > 10):
        dt["col3"] = dt["col3"].replace([x], "Lebih")
        
dt["col1"] = dt["col1"].replace(["Lebih"], 0)

print(dt.info())
