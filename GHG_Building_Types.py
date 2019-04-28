import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
file = open('municpal-building-energy-use-2009-2014.csv','r')
new_file = open('building_types_emitted_GHG.csv','w',newline='')
data = file.readlines()
building_types = ['Recreational', 'Municipal', 'Community', 'Transportational', 'Industrial', 'Public Works']
rec_costs = []
mun_costs = []
com_costs = []
tra_costs = []
ind_costs = []
pub_costs = []
years = []
cur_year = 2009
avg_cost_year = 0
file_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
file_writer.writerow(['Year', 'Building Type', 'Emitted GHG'])
for i in range(6):
    for line in data[1:]:
        id, name, address, GFA, year, site_EUI, WNS, source_EUI, WNS_EUI, electricity_use_kbtu, electricity_use_kwh, WNS_electricity, natural_gas_kbtu, natural_gas_therms, WNS_natural_gas, steam_use, total_GHG, GHG_intensity, energy_cost, energy_intensity = line.split(',')
        if((('Nature' in name or 'Pool' in name or 'Park' in name or 'Recreation' in name or 'Gym' in name) and total_GHG != 'Not Available') and year.split('/')[2] == str(cur_year)):
            file_writer.writerow([cur_year, 'Recreation', total_GHG])
            continue
        if((('School' in name or 'Firehouse' in name or 'Police' in name or 'Court' in name or 'Medic' in name or 'Civic' in name) and total_GHG != 'Not Available') and year.split('/')[2] == str(cur_year)):
            file_writer.writerow([cur_year, 'Municipal', total_GHG])
            continue
    
    del rec_costs[:]
    del mun_costs[:]
    years.append(cur_year)
    cur_year+=1
data = pd.read_csv('building_types_emitted_GHG.csv')
sns.catplot(x="Building Type", y="Emitted GHG", col="Year", data=data, kind="swarm", height=4, aspect=.7)
#fig, axes_list = plt.subplots(2, 3, sharex = 'col', sharey='row')
#axes_list[1][0] = sns.swarmplot(x = 'Building Type', y = 'Emitted GHG', data = data)
plt.show()
