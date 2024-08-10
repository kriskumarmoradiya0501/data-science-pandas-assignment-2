# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:23:52 2024

@author: 2student87
"""

import pandas as a
import numpy as b
k=['rainy','cloudy','sunny']
data = {
        'Days':['mon','tue','wed','thu','fri','sat','sun'],
        'Temperature':b.random.randint(0,40,7),
        'Humidity':b.random.randint(60,90,7),
        'Conditions': b.random.choice(k,7)
        }
print(data)
df=a.DataFrame(data)
print(df)