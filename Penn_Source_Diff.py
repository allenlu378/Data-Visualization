import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

con_data = pd.read_csv('Pennsylvania_Energy_Consumption_Estimates_2016.csv')
pro_data = pd.read_csv('Pennsylvania_Energy_Production_Estimates_2016.csv')

plt.rcParams['figure.figsize']=(15,10)

fig,ax = plt.subplots()

result = sns.barplot(x='Category', y='Pennsylvania Energy Consumption Estimates Trillion Btu', data=con_data, ax=ax, alpha = 0.2, color='blue')
for item in result.get_xticklabels():
    item.set_rotation(20)
    item.set_size(8)
    item.set_ha('right')


production = mpatches.Patch(color='#F8D1D2', label='Production')
consumption = mpatches.Patch(color='#D1D2F9', label='Consumption')
plt.legend(handles=[production,consumption], loc='best')
sns.barplot(x='Category', y='Pennsylvania Energy Production Estimates Trillion Btu', data=pro_data, ax=ax, color='red', alpha = 0.2).set_title('Difference in Pennsylvania Energy Source Production and Consumption', size = 20)
plt.show()