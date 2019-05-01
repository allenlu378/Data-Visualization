# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

#Read data from csv
data_file = open('municpal-building-energy-use-2009-2014.csv','r')
data = data_file.readlines()

#Array detailing which rows to skip
rows_to_skip = []

#Find which rows have unavailable energy costs
for num, line in enumerate(data[1:], 1):
        id, name, address, GFA, year, site_EUI, WNS, source_EUI, WNS_EUI, electricity_use_kbtu, electricity_use_kwh, WNS_electricity, natural_gas_kbtu, natural_gas_therms, WNS_natural_gas, steam_use, total_GHG, GHG_intensity, energy_cost, energy_intensity = line.split(',')
        if energy_cost == 'Not Available':
          rows_to_skip.append(num) 

#Read data from csv and skip rows ==where energy cost is not available
usable_data = pd.read_csv('municpal-building-energy-use-2009-2014.csv', encoding='cp1252', skiprows=rows_to_skip)

#Create and display swarm plot
plt.rcParams['figure.figsize']=(25,10)
sns.set(font_scale=1.2)
sns.boxplot(x="Year Ending", y="Energy Cost ($)", data=usable_data, whis=np.inf, palette = 'Blues')
plt.ylim(0, 50000)
plt.show()





