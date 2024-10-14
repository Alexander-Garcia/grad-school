import pandas as pd
from pulp import *

# read the file
df = pd.read_csv("tnn_data_1200_clicks.csv")
# define our problem - we are doing minimization
lp = LpProblem()
