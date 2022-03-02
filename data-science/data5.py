import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

os.system('cls')

dt = {
    'col1': [1,2,3,4],
    'col2': [3,4,2,1],
    'col4': [2,3,0,4]
}

ds = pd.DataFrame(dt)

# Matplotlib
x = np.array(ds['col1'])
y = np.array(ds['col2'])
# End matplotlib

plt.plot(x,y)
plt.show()

print(ds)