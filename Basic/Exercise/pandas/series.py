import pandas as pd
import numpy as np

a = np.arange(4);#single line comment
print(a)

"""
this is multiple line comment
"""

column = pd.Series(a, index=["one", "two", "three", "four"])
print(column)

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))