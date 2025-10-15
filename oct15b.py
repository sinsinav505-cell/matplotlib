# BAR GRAPH
# ------------------------------------------------------------
# Q3: Create a bar chart showing the number of students enrolled in each course.
# courses = ['AI', 'ML', 'Data Science', 'Web Dev']
# students = [50, 40, 60, 30]
# - Label the x and y axes
# - Add different colors for each bar

import matplotlib.pyplot as plt
import numpy as np

courses = ['AI', 'ML', 'Data Science', 'Web Dev']
students = [50, 40, 60, 30]

plt.xlabel('Courses')
plt.ylabel('Students')

plt.bar(courses,students,color = 'Red')

plt.show()