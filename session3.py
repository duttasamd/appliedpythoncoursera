import numpy as np

arr = [1, 2, 3, 4, 5, 6]
arr
x = np.array(arr)
x
y = np.array([[1, 2, 3], [4, 5, 6]])
y.shape
y.reshape(3, 2)
z = np.array(arr)
z.resize(2, 2)
z

a = np.array([-4, -2, 1, 3, 5])
a.sum()
a.max()
a.min()
a.mean()
a.std()

# ------------------------------------
import numpy as np
import timeit as timeit
import pandas as pd

s = pd.Series(np.random.randint(0,1000,10000))
s.head()

def total():
    total = 0
    for item in s:
        total+=item

total()

timeit.timeit(total, number=10)

def vectotal() :
    total = np.sum(s)

timeit.timeit(vectotal, number=10)