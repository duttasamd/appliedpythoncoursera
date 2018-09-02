RESPATH = '~/dev/python/coursera/introdatasciencepython/res/course1_downloads/'

import numpy as np
import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
df

df['Date'] = ['December 1', 'January 1', 'mid-May']
df

df['Delivered'] = True
df

df['Feedback'] = ['Pos', None, 'Neg']
df

# -----------------------------------------------

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
print()
print(student_df.head())

pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)

pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)