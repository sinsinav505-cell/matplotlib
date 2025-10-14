import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,15,4])
mylabels = ["Apples","Bananas","Oranges","Grapes"]

plt.pie(x,labels=mylabels,
        autopct="%1.1f%%")

plt.title('Fruit Sales',fontsize=15,
          family='monospace',
          fontweight='bold',
          color='Green')
plt.show()