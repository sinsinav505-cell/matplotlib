#display the distribution of numerical data

# standard deviation = spread or deviation from mean value(average)

# correlation is the relationship between two variables 
# i.e; if v1 increase v2 will also increas - positive correlation
# if v1 decrease v2 will also decrease -  negative correlation

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(loc=70,scale=10,size=100)
x = np.clip(x,0,85)

plt.hist(x,bins=10,edgecolor='black')

plt.title('Test Score')

plt.xlabel('Marks')
plt.ylabel('Students')

plt.show()
