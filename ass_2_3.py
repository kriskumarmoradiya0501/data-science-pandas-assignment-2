# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:17:10 2024

@author: 2student87
"""


import pandas as a
import numpy as b

data = {
        'Employees':['Sahil','Smit','Harmin','Mantri'],
        'Departments':['CMPICA BCA','CSPIT CE','DEPSTAR CS','IIIM'],
        'Hours Worked':b.random.randint(1,8,4),
        'Projects Completed': b.random.randint(0,11,4)
        }
print(data)
df=a.DataFrame(data)
print(df)