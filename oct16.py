#subplot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])

figure,axes = plt.subplots(2,2)

axes[0,0].plot(x, x*2, color='Red')
axes[0,0].set_title('x*2')

axes[0,1].plot(x, x**2, color='Blue')
axes[0,1].set_title('x**2')

axes[1,0].plot(x, x**2, color='Green')
axes[1,0].set_title('x**3')

axes[1,1].plot(x, x**4, color='Yellow')
axes[1,1].set_title('x**4')

plt.tight_layout()
plt.show()
