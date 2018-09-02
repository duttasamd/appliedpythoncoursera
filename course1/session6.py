RESPATH = '~/dev/python/coursera/introdatasciencepython/res/course1_downloads/'

import numpy as np
import pandas as pd

df = pd.read_csv(RESPATH + 'census.csv')
df.head()

df['SUMLEV'].unique()

columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

df = df[columns_to_keep]
df.head()

df = df.set_index(['STNAME', 'CTYNAME'])
df

df.loc['Alabama', 'Coffee County']