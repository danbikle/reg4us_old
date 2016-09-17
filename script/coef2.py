# ~/k4/script/coef2.py

# This script uses linear regression to help me rank features.

# Demo:
# ~/anaconda3/bin/python coef2.py

import numpy  as np
import pandas as pd
import pdb

train_df = pd.read_csv('../public/csv/feat.csv')

# I should build a Linear Regression model from slope columns in train_df:
x_train_a = np.array(train_df)[:,3:]
y_train_a = np.array(train_df.pctlead)
from sklearn import linear_model
linr_model = linear_model.LinearRegression()
# I should learn:
train_size_i = 252*30
linr_model.fit(x_train_a[train_size_i:-1], y_train_a[train_size_i:-1])
# Now that I have learned, I should see coef:
print(train_df.tail())
print('linr_model.coef_:')
print(linr_model.coef_)
print('Two most predictive features:')
print('slope6')
print('slope7')

'bye'
