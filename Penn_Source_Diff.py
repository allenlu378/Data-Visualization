import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

#Read consumption and production data
con_data = pd.read_csv('Pennsylvania_Energy_Consumption_Estimates_2016.csv')
pro_data = pd.read_csv('Pennsylvania_Energy_Production_Estimates_2016.csv')
types = ['Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Consumption', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production', 'Production']

#Set figure size
sns.set(font_scale=1.1)
plt.rcParams['figure.figsize']=(20,15)

#Organize data from both data sets
df = pd.DataFrame({'Type': types, 'Energy':  con_data['Pennsylvania Energy Consumption Estimates Trillion Btu'].values.tolist() + pro_data['Pennsylvania Energy Production Estimates Trillion Btu'].values.tolist()}, index = pro_data['Category'].values.tolist()+ pro_data['Category'].values.tolist())

#Create and display graph
ax = sns.barplot(x = df.Energy, y = df.index, hue = df.Type, palette = 'Blues' )
ax.set_title('Consumption and Production of Energy Sources in Pennsylvania', size = 20)
ax.set_xlabel('Energy (Trillion btu)', size = 15)
ax.set_ylabel('Energy Source', size = 15)
plt.show()