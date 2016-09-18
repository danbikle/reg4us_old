# ~/reg4us/script/coef.py

# This script uses linear regression to help me rank features.

# Demo:
# ~/anaconda3/bin/python coef.py

import numpy  as np
import pandas as pd
import pdb

gspc_df = pd.read_csv('../public/csv/gspc2.csv')

# I should compute pctlead:
gspc_df['pctlead'] = (100.0 * (gspc_df.cp.shift(-1) - gspc_df.cp) / gspc_df.cp).fillna(0)

# I should compute pctlag1,2,3,4,5,6,7,8,9
gspc_df['pctlag1'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(1)) / gspc_df.cp.shift(1)).fillna(0)
gspc_df['pctlag2'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(2)) / gspc_df.cp.shift(2)).fillna(0)
gspc_df['pctlag3'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(3)) / gspc_df.cp.shift(3)).fillna(0)
gspc_df['pctlag4'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(4)) / gspc_df.cp.shift(4)).fillna(0)
gspc_df['pctlag5'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(5)) / gspc_df.cp.shift(5)).fillna(0)
gspc_df['pctlag6'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(6)) / gspc_df.cp.shift(6)).fillna(0)
gspc_df['pctlag7'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(7)) / gspc_df.cp.shift(7)).fillna(0)
gspc_df['pctlag8'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(8)) / gspc_df.cp.shift(8)).fillna(0)
gspc_df['pctlag9'] = (100.0 * (gspc_df.cp - gspc_df.cp.shift(9)) / gspc_df.cp.shift(9)).fillna(0)

# I should prep training data.
obsv_i    = 252*30 # 30 yr
pred_sr = (gspc_df.cdate < '2016')
gspc_a = np.array(gspc_df[pred_sr])[-obsv_i:-1]

x_train_a = gspc_a[:,3:]
y_train_a = gspc_a[:,2]

from sklearn import linear_model
linr_model = linear_model.LinearRegression()
linr_model.fit(x_train_a, y_train_a)

# I should see coef:
print('linr_model.coef_:')
print(linr_model.coef_)
print('most predictive features:')
print('pctlag2')
print('pctlag7')
'bye'
