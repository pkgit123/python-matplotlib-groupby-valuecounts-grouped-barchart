# ==================================================================================================================
# Use groupby and value_counts into grouped bar chart
# https://stackoverflow.com/questions/57618570/how-do-i-turn-groupby-and-value-counts-into-multiple-pie-bar-charts
# https://seaborn.pydata.org/generated/seaborn.load_dataset.html
# https://seaborn.pydata.org/generated/seaborn.get_dataset_names.html#seaborn.get_dataset_names
# ==================================================================================================================

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 999)

%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

print('Seaborn version: ', sns.__version__)

print()
print(sns.get_dataset_names())

# load dataset
df = sns.load_dataset('penguins')

print(df.head())

# set the .groupby() col, the .value_counts() col, and normalize as % 
# notice the transpose `.T`
gb_col_name = 'sex'
str_col_name = 'island'
dfu = df.groupby([gb_col_name])[str_col_name].value_counts(dropna=False, normalize=True).unstack().T

# plot
dfu.plot.bar(figsize=(7, 5))
plt.legend(title=gb_col_name, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel(str_col_name)
plt.ylabel('% of Total')
plt.show()

print(dfu)

