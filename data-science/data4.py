import os
import pandas as pd

os.system('cls')

dt = {
    'col1': [3,3,4,4],
    'col2': [3,2,1,5],
    'col4': [2,3,0,4]
}

ds = pd.DataFrame(dt)

print(ds.describe())