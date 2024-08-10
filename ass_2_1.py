import pandas as pd
import numpy as np

student = 10

data = {
    'Test 1':np.random.randint(0,11,student),
    'Test 2':np.random.randint(0,11,student),
    'Test 3':np.random.randint(0,11,student),
    'Test 4':np.random.randint(0,11,student),
    'Test 5':np.random.randint(0,31,student),
    'Test 6':np.random.randint(0,71,student)
}

df = pd.DataFrame(data)

print(df.loc[0])
print(df.loc[1])
print(df.loc[2])
print(df.loc[3])
print(df.loc[4])
print(df.loc[5])
print(df.loc[6])
print(df.loc[7])
print(df.loc[8])
print(df.loc[9])



