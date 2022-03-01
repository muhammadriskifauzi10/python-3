import os
import pandas as pd

os.system('cls')

d = {
    'col1' : [1,4,3],
    'col2' : [3,2,1]
}

df = pd.DataFrame(d)

print(df)
print("Length col", df.shape[1])
