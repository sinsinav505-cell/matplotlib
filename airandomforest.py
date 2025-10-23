import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

df = pd.read_csv('ai_job_market.csv')

df.drop(['job_id', 'company_name', 'posted_date'], axis=1, inplace=True)

def parse_salary(s):
    try:
        s = s.strip()
        if '-' in s:
            low, high = s.split('-')
            return (int(low) + int(high)) / 2
        else:
            return int(s)
    except:
        return np.nan
    
df['salary_range_usd'] = df['salary_range_usd'].apply(parse_salary)

df.dropna(subset=['salary_range_usd'], inplace=True)

df['num_skills'] = df['skills_required'].apply(lambda x: len(str(x).split(',')))
df['num_tools'] = df['tools_preferred'].apply(lambda x: len(str(x).split(',')))

df.drop(['skills_required', 'tools_preferred'], axis=1, inplace=True)

categorical_cols = ['industry', 'job_title', 'experience_level', 'employment_type', 'location', 'company_size']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

X = df.drop('salary_range_usd', axis=1)
y = df['salary_range_usd']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R² Score:", r2)

new_job = {
    'industry': 'Tech',
    'job_title': 'Data Scientist',
    'experience_level': 'Mid',
    'employment_type': 'Full-time',
    'location': 'New York',
    'company_size': '51-200',
    'num_skills': 3, 
    'num_tools': 1 }

new_job_df = pd.DataFrame([new_job])
new_job_df = pd.get_dummies(new_job_df)


new_job_df = new_job_df.reindex(columns=X_train.columns, fill_value=0)

predicted_salary = model.predict(new_job_df)
print("Predicted Salary (USD):", predicted_salary[0])