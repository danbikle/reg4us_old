# whatif_rpt.py

# This script should be called by whatif.bash

# # This script helps me understand some whatif-scenarios.

# This script should generate some static content each night
# after the market has closed and the most recent GSPC-closing-price
# is available from Yahoo.

# If you have questions, e-me: bikle101@gmail.com

import pandas as pd

rpt_df = pd.read_csv('../public/csv/whatif_pred.csv')
rpt_df.to_html('../app/views/pages/_whatif_pred.erb', index=False)

'bye'

