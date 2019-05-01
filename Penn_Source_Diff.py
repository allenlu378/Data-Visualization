import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

#Read consumption and production data
con_data = pd.read_csv('Pennsylvania_Energy_Consumption_Estimates_2016.csv')
pro_data = pd.read_csv('Pennsylvania_Energy_Production_Estimates_2016.csv')

#Set figure size
plt.rcParams['figure.figsize']=(20,15)

#Create graph, rotate labels, and display graph
df = pd.DataFrame({'consumption': con_data['Pennsylvania Energy Consumption Estimates Trillion Btu'].values, 'production': pro_data['Pennsylvania Energy Production Estimates Trillion Btu'].values}, index=pro_data['Category'].values)
ax = df.plot(kind = 'bar', rot = 15, colormap = 'Paired')
ax.set_title('Consumption and Production of Energy Sources in Pennsylvania', size = 20)
xticks = ax.get_xticklabels()
ax.set_xlabel('Energy Source', size = 15)
ax.set_ylabel('Energy (Trillion btu)', size = 15)
for tick in xticks:
    tick.set_ha('right')
plt.show()