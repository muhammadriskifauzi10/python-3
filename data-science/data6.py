import os
import numpy as np
import pandas as pd

os.system('cls')

dt = {
    'col1': [4,4],
    'col2': [2,2],
}

ds = pd.DataFrame(dt)

x = ds['col1']
y = ds['col2']

s_i = np.polyfit(x,y,1)

print(s_i)