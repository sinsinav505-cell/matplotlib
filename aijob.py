import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

df = pd.read_csv('ai_job_market.csv')

#cleaning

df.drop(['job_id','company_name','posted_date'],axis=1,inplace=True)  #droping unwanted columns while predicting

#print(df.head())

#df.info()

df.isnull().sum()  #checking  if there is any null values


def parse_salary(s):
    try:
        # Remove spaces
        s = s.strip()
        # If it contains a dash, take average
        if '-' in s:
            low, high = s.split('-')
            return (int(low) + int(high)) / 2
        else:
            # If no dash, just convert to int
            return int(s)
    except:
        # If something goes wrong, return NaN
        return float('nan')

df['salary_range_usd'] = df['salary_range_usd'].apply(parse_salary)


x = df.drop('salary_range_usd',axis=1) #everything except salary_range_usd
y = df['salary_range_usd']  #only salary_range_usd

x = pd.get_dummies(x, drop_first=True)
#print(x.shape)

#print(x.head())

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))


new_job = {
    'industry': 'Tech',
    'job_title': 'Data Scientist',
    'skills_required': 'Python, Machine Learning, SQL',
    'experience_level': 'Mid',
    'employment_type': 'Full-time',
    'location': 'New York',
    'company_size': '51-200',
    'tools_preferred': 'TensorFlow'
}


new_job_df = pd.DataFrame([new_job])

new_job_encoded = pd.get_dummies(new_job_df, drop_first=True)
new_job_encoded = new_job_encoded.reindex(columns=x_train.columns, fill_value=0)

predicted_salary = model.predict(new_job_encoded)
print("Predicted Salary (USD):", predicted_salary[0])
