import matplotlib.pyplot as plt 
import numpy as np

x1 = np.array([0,1,2,3,4,5,6,7,8])
y1 = np.array([10,20,50,65,7,60,68,33,85])
y2 = np.array([30,40,55,60,70,80,90,20,25])

plt.title('Test Scores')

plt.xlabel('Hours Studied')
plt.ylabel('Marks')

plt.scatter(x1,y1,label = 'ClassA')
plt.scatter(x1,y2,color='Red',
            s = 45,
            label = 'ClassB')

plt.legend()

plt.show()
