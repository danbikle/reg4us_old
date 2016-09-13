# whatif_rpt.py

# This script should be called by whatif.bash

# # This script helps me understand some whatif-scenarios.

# This script should generate some static content each night
# after the market has closed and the most recent GSPC-closing-price
# is available from Yahoo.

# If you have questions, e-me: bikle101@gmail.com

import pandas as pd
import pdb

pdb.set_trace()
rpt_df   = pd.read_csv('../public/csv/whatif_pred.csv')
rpt_df


bye
lastp_f     = float(whatif_df[-1:].cp)
newcp_f     = lastp_f * pctchange_f + lastp_f
idxlast_i   = whatif_df[-1:].index[0]
whatif_df.loc[idxlast_i,'cp'] = newcp_f
whatif_df.to_csv('../public/csv/gspc2.csv', float_format='%4.4f', index=False)


'bye'

