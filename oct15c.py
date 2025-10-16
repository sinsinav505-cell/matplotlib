# Q4: Plot a grouped bar chart comparing male vs female students in each department.
# departments = ['CSE', 'ECE', 'EEE', 'ME']
# male = [40, 35, 30, 25]
# female = [30, 25, 20, 15]
# - Display bars side by side
# - Add a legend

import matplotlib.pyplot as plt
import numpy as np

departments = ['CSE', 'ECE', 'EEE', 'ME']
male = [40, 35, 30, 25]
female = [30, 25, 20, 15]

plt.subplot(1,2,1)
plt.bar(departments,male)

plt.subplot(1,2,2)
plt.bar(departments,female)
plt.show()