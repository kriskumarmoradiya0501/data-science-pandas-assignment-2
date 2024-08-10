# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:33:42 2024

@author: 2student87
"""


import pandas as a
import numpy as b

data = {
        'Student':['Sahil','Smit','Harmin','Mantri'],
        'C language Grades':b.random.randint(0,101,4),
        'DBMS Grades':b.random.randint(0,101,4),
        'DataScience Grades': b.random.randint(0,101,4),
        }
print(data)
df=a.DataFrame(data)
print(df)
df['Average'] = df.mean(axis=1)
i = 0
while i<4:
    print(df.loc[i])
    i+=1
