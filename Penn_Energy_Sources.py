import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})
data = pd.read_csv('Pennsylvania_Energy_Consumption_Estimates_2016.csv')
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 20
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size
dims = (10,4)
result = data.groupby(["Category"])['Pennsylvania Energy Consumption Estimates Trillion Btu'].aggregate(np.median).reset_index().sort_values('Pennsylvania Energy Consumption Estimates Trillion Btu', ascending = False)
ax = sns.barplot(x="Pennsylvania Energy Consumption Estimates Trillion Btu", y="Category", palette="Reds_d", data=data, order = result['Category']).set_title('Energy Consumption by Source in Pennsylvania', size = 30)

plt.show()