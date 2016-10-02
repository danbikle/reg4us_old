# whatif_rpt2.py

# This script helps me understand some whatif-scenarios.
# Demo:
# python whatif_rpt2.py

import pandas as pd
import pdb

import matplotlib
matplotlib.use('Agg')
# Order is important here.
# Do not move the next import:
import matplotlib.pyplot as plt

rpt_df = pd.read_csv('../public/csv/whatif_pred.csv')

es_future_delta = -7.0 # future_price - es_price (approx). 

rpt_df['es_whatif_price'] = rpt_df.Whatif_Price + es_future_delta

plot_this_df = rpt_df[['es_whatif_price','Logistic Regression Prediction']]

plot_this2_df = plot_this_df.set_index(['es_whatif_price'])
plot_this2_df.plot.line(title="Prediction vs Price", figsize=(11,7))

# I should plot
plt.grid(True)
plt.savefig('../public/pvprice.png')
plt.close()

'bye'
