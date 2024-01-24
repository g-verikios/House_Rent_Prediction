# %%
#@ IMPORTS
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import pickle

# PARAMETERS (normally given through CLI for eg.)

control_var = {'min_child_weight': 1.5,
               'max_depth': None,
               'eta': 0.05,
               'n_jobs': 16
}

output_file = 'model.bin'

# %% 
# DATA PREPARATION
data = pd.read_csv('House_Rent_Dataset.csv')

# Lets make column names a bit more consistent replacing spaces with _ and using lowercase
data.columns = data.columns.str.lower().str.replace(' ', '_')

# Let's find the categorical columns

categorical_columns = list(data.dtypes[data.dtypes == 'object'].index)

# and numerical columns as well
num_columns = list(data.dtypes[data.dtypes == 'int64'].index)

# Lets make categorical data in columns consistent as well
for c in categorical_columns:
    data[c] = data[c].str.lower().str.replace(' ', '_')

label_encoded_columns = categorical_columns
le = LabelEncoder()

for column in label_encoded_columns:
    data[column] = le.fit_transform(data[column])

df_full_train, df_test = train_test_split(data, test_size=0.2,  random_state=42)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# Useful Functions
def train(df_train, y_train, model):
    
    X_train = df_train.loc[:, df_train.columns!='rent'].values
    model = XGBRegressor(min_child_weight= control_var['min_child_weight'], 
                         max_depth= control_var['max_depth'], 
                         eta= control_var['eta'], 
                         n_jobs=control_var['n_jobs'])
    
    model.fit(X_train, y_train)
    
    return model

def predict(df, model):
    X = df.loc[:, df.columns!='rent'].values
    y_pred = model.predict(X)
    
    return y_pred

def rmse(y_pred, y_val):
    score = float(mean_squared_error(y_pred, y_val))** 0.5 
    return score
# %% 
# ### FINAL MODEL

print('Training the final model...')

model = train(df_full_train, np.log1p(df_full_train.rent.values), control_var)

y_test = np.log1p(df_test.rent.values)

y_pred = predict(df_test, model)

score = rmse(y_pred, y_test)

print("For model %s: RMSE is : %.5f" % (model, score))

# %% 
# SAVE THE MODEL

with open(output_file, 'wb') as f_out:

    pickle.dump(model, f_out)

print(f'the model is saved to {output_file}')