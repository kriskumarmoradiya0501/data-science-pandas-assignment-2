# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:55:21 2024

@author: 2student87
"""

import pandas as a
import numpy as b

data = {
        'Days':['mon','tue','wed','thu','fri','sat','sun'],
        'items':['Apple','Banana','kiwi','Strawbary','Black Bary','awakado','Chiku'],
        'Quntities':b.random.randint(1,9,7),
        'Price': b.random.randint(100,1001,7)
        }
print(data)
df=a.DataFrame(data)
print(df)
print(df['Price'].sum())