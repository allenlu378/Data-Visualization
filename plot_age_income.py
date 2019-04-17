'''
plot_age_income.py 
reads data from the age_income_feb14.csv
and creates a scatter plot.
The data are from U.S. Census Bureau's February 2014 
Current Population Survey. 

(c) 2014 Project Lead The Way
'''
import matplotlib.pyplot as plt
import numpy as np
# Get the income/age data from CSV
municipal_file = open('municpal-building-energy-use-2009-2014.csv','r')
municipal = municipal_file.readlines()
consumption_file = open('municpal-building-energy-use-2009-2014.csv','r')
consumption = consumption_file.readlines()
####
# Transform the data from strings to signed integers
####
years=[]
energy_costs=[]
total_GHG_arr = []
energy_consumptions = []
energy_source_consumption = []
for line in consumption[5:]: # Omit header lines
    category, energy_estimate = line.split(',')
    energy_source_consumption.append(category)
    energy_source_consumption.append(float(energy_estimate.rstrip())) # omit space, -, $, \n
plt.barh(np.arange(len(energy_source_consumption)), energy_consumptions)


for line in municipal[1:]: # Omit header lines
    id, name, address, GFA, year, site_EUI, WNS, source_EUI, WNS_EUI, electricity_use_kbtu, electricity_use_kwh, WNS_electricity, natural_gas_kbtu, natural_gas_therms, WNS_natural_gas, steam_use, total_GHG, GHG_intensity, energy_cost, energy_intensity = line.split(',')
    if energy_cost == 'Not Available':
        continue;
    years.append(year.split('/')[2])
    energy_costs.append(energy_cost) # omit space, -, $, \n

        
        
fig, ax  = plt.subplots(1, 1)
ax.plot(years, energy_costs, 'ro')
ax.set_title('Total Energy Cost for Buildings in Pittsburg from 2009-2014')
ax.set_xlabel('Year')
ax.set_ylabel('Total Energy Cost($)')

fig.show()
del years[:]
for line in data[1:]: # Omit header lines
    id, name, address, GFA, year, site_EUI, WNS, source_EUI, WNS_EUI, electricity_use_kbtu, electricity_use_kwh, WNS_electricity, natural_gas_kbtu, natural_gas_therms, WNS_natural_gas, steam_use, total_GHG, GHG_intensity, energy_cost, energy_intensity = line.split(',')
    if total_GHG == 'Not Available':
        continue;
    years.append(year.split('/')[2])
    total_GHG_arr.append(total_GHG) # omit space, -, $, \n
fig, ax  = plt.subplots(1, 1)
ax.plot(years, total_GHG_arr, 'ro')
ax.set_title('Total Greenhouse Gas Emission for Buildings in Pittsburg from 2009-2014')
ax.set_xlabel('Year')
ax.set_ylabel('Greenhouse Gas Emission(Metric Tons CO2e)')

fig.show()