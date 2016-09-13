# whatif.py

# This script should apply pctchange to last price.

# Demo:
# python whatif.py -0.4

import pandas as pd
import pdb

# I should check cmd line arg
import sys
if (len(sys.argv) != 2):
  print('You typed something wrong:')
  print('Demo:')
  print('~/anaconda3/bin/python whatif.py -0.4')
  sys.exit()
pctchange_f = float(sys.argv[1]) / 100.0
whatif_df   = pd.read_csv('../public/csv/whatif.csv')
lastp_f     = float(whatif_df[-1:].cp)
newcp_f     = lastp_f * pctchange_f + lastp_f
idxlast_i   = whatif_df[-1:].index[0]
whatif_df.loc[idxlast_i,'cp'] = newcp_f
whatif_df.to_csv('../public/csv/gspc2.csv', float_format='%4.4f', index=False)

'bye'

