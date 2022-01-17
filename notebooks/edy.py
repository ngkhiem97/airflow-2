# Import data to pandas dataframe
import pandas as pd

mrt_data = pd.read_csv('../data/training_MRT.csv')
t_data = pd.read_csv('../data/training_T.csv')['T']
v_data = pd.read_csv('../data/training_V.csv')['V']

t_data.head()
v_data.head()

# Merge dataframes
# df = pd.merge(mrt_data, t_data, on='id')
# df = pd.merge(df, v_data, on='id')

