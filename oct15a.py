# Q2: Plot two lines on the same graph — sales of Product A and Product B over 6 months.
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# productA = [120, 150, 170, 190, 210, 230]
# productB = [100, 130, 160, 180, 200, 250]
# - Use different colors and line styles
# - Add a legend

import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
productA = [120, 150, 170, 190, 210, 230]
productB = [100, 130, 160, 180, 200, 250]

line_style = dict(marker='.',markersize=6,markerfacecolor='black',markeredgecolor='black',
         linestyle='dashed',linewidth=2)

plt.plot(months,productA,**line_style,color="Red",label='Product A')
plt.plot(months,productB,**line_style,color="Blue",label='Product B')

plt.legend()
plt.show()
