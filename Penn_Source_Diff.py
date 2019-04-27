
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
con_data = pd.read_csv('Pennsylvania_Energy_Consumption_Estimates_2016.csv')
pro_data = pd.read_csv('Pennsylvania_Energy_Production_Estimates_2016.csv')

plt.rcParams['figure.figsize']=(8,10)

fig,ax = plt.subplots()

result = sns.barplot(x='Category', y='Pennsylvania Energy Consumption Estimates Trillion Btu', data=con_data, ax=ax, alpha = 0.5, color='blue')
ax2 = ax.twinx()
for item in result.get_xticklabels():
    item.set_rotation(40)
sns.barplot(x='Category', y='Pennsylvania Energy Production Estimates Trillion Btu', data=pro_data, ax=ax2, color='red', alpha = 0.5)
plt.show()