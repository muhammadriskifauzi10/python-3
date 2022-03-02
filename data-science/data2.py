import os
import numpy as np
import pandas as pd

os.system('cls')

dt = {
    'col1': [1,3,2,4],
    'col2': [3,7,1,4],
    'col3': [2,6,1,5]
}

ds = pd.DataFrame(dt)

# Search max value
# t_max = max(dt['col2'])

# Search min value
# t_min = min(dt['col2'])

# Search mean value
t_mean = np.mean(dt['col1'])

print("Value :",t_mean)
print("Row for data :",ds.shape[0])