import matplotlib.pyplot as plt
import numpy as np

fruits = np.array(['Apples','Bananas','Cherries','Dates'])
sales = np.array([400,350,300,450])

line_style = dict(fontsize = 15,
                  family = 'serif',
                  fontweight = 'bold',
                  color = 'Blue')

plt.bar(fruits,sales,color='skyblue')

plt.title('Fruit sales',fontsize=15,color='Blue',family='serif',fontweight='bold')

plt.xlabel('Fruits',**line_style)
plt.ylabel('Sales',**line_style)

plt.show()