# Sample Dataset ⿢: Age vs Annual Income by Gender
'''df_income = pd.DataFrame({
    'Age': [22, 25, 27, 29, 30, 32, 35, 37, 40, 45],
    'Annual Income': [25000, 27000, 30000, 33000, 36000, 40000, 45000, 48000, 52000, 60000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})'''

# ⿢ Plot a scatter graph comparing 'Age' and 'Annual Income' from the dataset.
#     - Use different colors or markers for different 'Gender' categories.

import matplotlib.pyplot as plt
import pandas as pd

df_income = pd.DataFrame({
    'Age': [22, 25, 27, 29, 30, 32, 35, 37, 40, 45],
    'Annual Income': [25000, 27000, 30000, 33000, 36000, 40000, 45000, 48000, 52000, 60000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

print(df_income)

colors = df_income['Gender'].map({'Male':'Blue','Female':'red'})

plt.scatter(df_income['Age'],df_income['Annual Income'] , c =colors)

plt.scatter([],[],label='Male',c='Blue')
plt.scatter([],[],label='Female',c='Red')

plt.legend()
plt.show()