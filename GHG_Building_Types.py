import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
file = open('municpal-building-energy-use-2009-2014.csv','r')
new_file = open('building_types_emitted_GHG.csv','w',newline='')
data = file.readlines()
file_writer = csv.writer(new_file, delimiter=',')
file_writer.writerow(['Year', 'Building Type', 'Emitted GHG'])
for i in range(6):
    for line in data[1:]:
        id, name, address, GFA, year, site_EUI, WNS, source_EUI, WNS_EUI, electricity_use_kbtu, electricity_use_kwh, WNS_electricity, natural_gas_kbtu, natural_gas_therms, WNS_natural_gas, steam_use, total_GHG, GHG_intensity, energy_cost, energy_intensity = line.split(',')
        if((('Nature' in name or 'Pool' in name or 'Park' in name or 'Recreation' in name or 'Gym' in name) and total_GHG != 'Not Available')):
            file_writer.writerow([year.split('/')[2], 'Recreation', total_GHG])
            continue
        if((('School' in name or 'Firehouse' in name or 'Police' in name or 'Court' in name or 'Medic' in name or 'Civic' in name) and total_GHG != 'Not Available')):
            file_writer.writerow([year.split('/')[2], 'Municipal', total_GHG])
            continue
        
new_data = pd.read_csv('building_types_emitted_GHG.csv', nrows = 532)
sns.factorplot(x="Building Type", y="Emitted GHG", col="Year", data=new_data, kind="swarm", col_wrap = 3,size = 5, aspect=.4, )
plt.show()
print(new_data)