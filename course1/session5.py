import numpy as np
import pandas as pd

df = pd.read_csv('~/dev/python/coursera/introdatasciencepython/res/course1_downloads/olympics.csv')
df.head()

df = pd.read_csv('~/dev/python/coursera/introdatasciencepython/res/course1_downloads/olympics.csv', index_col = 0, skiprows=1)
df.head()

df.columns

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()

df['Total'] > 30
df.head()

only_gold = df.where(df['Gold'] > 30)
only_gold = only_gold.dropna()
only_gold