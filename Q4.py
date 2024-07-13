# Using pandas, write a Python function to clean and preprocess a given DataFrame, which involves handling missing values, normalizing numerical columns, and encoding categorical columns.




import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def clean_and_preprocess(df):
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = df.select_dtypes(include=['object']).columns

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', Pipeline([
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ]), numeric_features),
            ('cat', Pipeline([
                ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ]), categorical_features)
        ])
    
    return preprocessor.fit_transform(df)

data = {
    'age': [25, np.nan, 35, 45, np.nan],
    'salary': [50000, 60000, np.nan, 80000, 90000],
    'city': ['New York', 'Los Angeles', 'Chicago', np.nan, 'San Francisco']
}
df = pd.DataFrame(data)
cleaned_data = clean_and_preprocess(df)
print(cleaned_data)
