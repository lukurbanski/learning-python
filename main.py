#virtual env
# python3 -m venv venv/       # Creates an environment called venv/
# source venv/bin/activate    

import pandas as pd
import numpy as np

# list of strings
x = "Dzisiaj mamy fascynujacy dzien duzo nauki"
lst =  x.split(" ")
# list of int
lst2 = list(range(1,6))
  
df = pd.DataFrame(list(zip(lst, lst2)),
               columns =['Word', 'Value'])

print(df.head(10))
