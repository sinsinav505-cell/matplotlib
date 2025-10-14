import matplotlib.pyplot as plt
import numpy as np

x = np.array([2022,2023,2024,2025])

y = np.array([0,0,23,25])
y1 = np.array([5,6,6,30])

line_style = dict(marker='o',markersize=5,markerfacecolor='Red',markeredgecolor='Red',
         linestyle='solid',linewidth=2)

plt.tick_params(axis='both',
                color='Blue')


fonta = dict(fontsize=15,
             family='monospace',
             fontweight='bold')

plt.title('Line Graph',**fonta,color='Red' )

plt.xlabel('Years',**fonta,color='Green')

plt.ylabel('Students',**fonta,color='Green')

plt.grid(linewidth=0.5,
         color='#7dc8e3',
         linestyle='dashed')

plt.plot(x,y, **line_style,color='#509e2e') 
plt.plot(x,y1, **line_style,color='Blue')

plt.xticks(x)


plt.show()

