# GRADES #

# Importing Libraries #

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing Dataframes #
marks = pd.read_csv('grades.csv', index_col=0, na_values=['??', '????'
                     ])

# Inserting Grades class column #

marks.insert(9, 'Grades', '')

# Classifying the Grades #

for i in range(0, len(marks['grandtotal']), 1):
    if marks['grandtotal'][i] > 88.25:
        marks['Grades'][i] = 'AA'
    elif marks['grandtotal'][i] > 78.25 and marks['grandtotal'][i] \
        <= 88.25:
        marks['Grades'][i] = 'AB'
    elif marks['grandtotal'][i] > 68.25 and marks['grandtotal'][i] \
        <= 78.25:
        marks['Grades'][i] = 'BB'
    elif marks['grandtotal'][i] > 58.25 and marks['grandtotal'][i] \
        <= 68.25:
        marks['Grades'][i] = 'BC'
    elif marks['grandtotal'][i] > 48.25 and marks['grandtotal'][i] \
        <= 58.25:
        marks['Grades'][i] = 'CC'
    elif marks['grandtotal'][i] > 38.25 and marks['grandtotal'][i] \
        <= 48.25:
        marks['Grades'][i] = 'CD'
    elif marks['grandtotal'][i] > 30 and marks['grandtotal'][i] \
        <= 38.25:
        marks['Grades'][i] = 'DD'
    else:
        marks['Grades'][i] = 'FF'

# Grades Visualiztion #
counts = [4,46,129,74,49,32,4,12]  # grades['Grades'].value_counts() <- was used
grades = ['AA','AB','BB','BC','CC','CD','DD','FF']
index = np.arange(len(grades))
plt.bar(index, counts, color=['green','blue','yellow','orange','cyan','purple','orange','red'])
plt.title('Bar plot of Grades')
plt.xlabel('Grades')
plt.ylabel('Frequency')
plt.xticks(index,grades)
plt.show()