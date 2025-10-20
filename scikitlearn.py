import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

data = {
    'Hours studied':[1,2,3,4,5,6,7,8,9,10],
    'Score':[35,40,50,55,60,65,70,75,85,90]
}

df = pd.DataFrame(data)
print(df)

