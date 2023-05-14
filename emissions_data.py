import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel('table4_.xlsx', index_col=0)

# Transpose the DataFrame so that years are in rows
df = df.T

for state in df.columns:
    plt.plot(df.index, df[state], marker='o', linestyle='-', label=state)

plt.xlabel('Year')
plt.ylabel('Per Capita CO2 Emissions (metric tons)')
plt.title('Per Capita Energy-Related CO2 Emissions by State (1970–2020)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.savefig("PerCapitaEmissions_trends.png", dpi=300, bbox_inches='tight')
plt.show()

total_emissions = df.sum(axis=1)

plt.figure(figsize=(14, 8))
plt.plot(total_emissions.index, total_emissions, marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Total CO2 Emissions (metric tons)')
plt.title('Total Energy-Related CO2 Emissions for All States (1970–2020)')
plt.grid()
plt.savefig("Total_CO2_Emissions_Trend.png", dpi=300, bbox_inches='tight')
plt.show()


#Plotting average CO2 emissions across the years (1970 to 2020)
average_emissions = df.mean(axis=1)  # axis=1 calculates the mean across columns for each row
average_emissions.plot(figsize=(14, 8), marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Average CO2 Emissions (metric tons)')
plt.title('Average Energy-Related CO2 Emissions for All States (1970–2020)')
plt.grid()
plt.savefig("AverageEmissions_trends.png", dpi=300, bbox_inches='tight')

plt.show()


#Latest Year
latest_year = df.loc[2020].sort_values(ascending=False)

#Top 5 States from 1970 to 2021 (Per Capita CO2 Emissions)

top_5_states = latest_year.head(5)

plt.figure(figsize=(14, 8))
for state in top_5_states.index:
    plt.plot(df.index, df[state], marker='o', linestyle='-', label=state)

plt.xlabel('Year')
plt.ylabel('Per Capita CO2 Emissions (metric tons)')
plt.title('Top 5 Highest Per Capita Energy-Related CO2 Emissions by State (1970–2020)')
plt.legend()
plt.grid()
plt.savefig("Top_5_States_Emissions.png", dpi=300, bbox_inches='tight')
plt.show()

#Using seaborn for the visualization
import seaborn as sns
sns.set(style="darkgrid")

#Seaborn
top_5_states = latest_year.head(5).index

plt.figure(figsize=(14, 8))
sns.lineplot(data=df[top_5_states], dashes=False, markers=True)
plt.xlabel('Year')
plt.ylabel('Per Capita CO2 Emissions (metric tons)')
plt.title('Top 5 Highest Per Capita Energy-Related CO2 Emissions by State (1970–2020)')
plt.legend(title='State', title_fontsize='13', loc='upper right', labels=top_5_states)
plt.savefig("Top_5_States_Emissions_seaborn.png", dpi=300, bbox_inches='tight')
plt.show()

#Making a heat-map for per capita emissions by State
sns.set(style="darkgrid")

df_emissions = df

sns.set(style="darkgrid")

plt.figure(figsize=(18, 10))
sns.heatmap(df, cmap='viridis', linewidths=0.5)

plt.xlabel('Year')
plt.ylabel('State')
plt.title('Per Capita Energy-Related CO2 Emissions by State (1970–2020)')
plt.savefig("heatmap_emissions.png", dpi=300, bbox_inches='tight')
plt.show()

#Heatmap for last 10 years


#top 10 states
# Slice the DataFrame to include only years from 2010 to 2020
df_2010_2020 = df.loc[2010:2020]

# Calculate the average emissions for each state over this period
state_averages = df_2010_2020.mean().sort_values(ascending=False)

# Select the top 10 states with the highest carbon emissions
top_10_states = state_averages.head(10).index

# Create a new DataFrame containing only the top 10 states
df_top_10 = df_2010_2020[top_10_states]

# Reset the index and rename the column to 'Year'
df_top_10 = df_top_10.reset_index().rename(columns={'index': 'Year'})

# Melt the DataFrame to have 'Year', 'State', and 'Emissions' columns
df_melted = df_top_10.melt(id_vars=['Year'], var_name='State', value_name='Emissions')

# Create a box plot
plt.figure(figsize=(15, 8))
sns.boxplot(x='State', y='Emissions', data=df_melted, palette='plasma')
plt.xlabel('State')
plt.ylabel('Per Capita CO2 Emissions')
plt.title('Per Capita Energy-Related CO2 Emissions of Top 10 States (2010–2020)')
plt.xticks(rotation=45)
plt.savefig("Top_10_Emissions_Boxplot.png", dpi=300, bbox_inches='tight')

plt.show()

df.head()

df.dtypes

#The melt function in pandas is used to transform a DataFrame from a wide format to a long format.


# Read the Excel file into a DataFrame
df_electricity = pd.read_excel('electricity .xlsx', index_col=0)

# Transpose the DataFrame so that years are in rows
df_electricity = df_electricity.T

for state in df_electricity.columns:
    plt.plot(df_electricity.index, df[state], marker='o', linestyle='-', label=state)

plt.xlabel('Year')
plt.ylabel('Per Capita CO2 Emissions for Electricity (metric tons)')
plt.title('Per Capita Energy-Related CO2 Emissions by State (Electricity) (1970–2020)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.savefig("Per_Capita_for_Electricity", dpi=300, bbox_inches='tight')

plt.show()

    
df_electricity.index.name ='Year'


# Create a line graph with multiple lines, one for each state
plt.figure(figsize=(14, 8))

for state in df_electricity.columns:
    plt.plot(df_electricity.index, df_electricity[state], marker='o', linestyle='-', label=state)

plt.xlabel('Year')
plt.ylabel('Electricity Production (Billion kWh)')
plt.title('Electricity Production by State (1970–2020)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.savefig("Electricity_by_state.png", dpi=300, bbox_inches='tight')

plt.show()


#Plotting Total Electricity Emissions Across States (1970 to 2020)
total_electricity_emissions = df_electricity.sum(axis=1)

plt.figure(figsize=(14, 8))
plt.plot(total_electricity_emissions.index, total_electricity_emissions, marker='o', linestyle='-')

plt.xlabel('Year')
plt.ylabel('Total CO2 Emissions by Electricity (metric tons)')
plt.title('Total Electricity CO2 Emissions for All States (1970–2020)')
plt.grid()
plt.savefig("Total_Electricity_All_States.png", dpi=300, bbox_inches='tight')

plt.show()

#Finally the project

# Read the Excel file into a DataFrame
coal_emissions = pd.read_excel('coal.xlsx', index_col=0)
natural_gas_emissions = pd.read_excel('natural_gas.xlsx', index_col=0)

coal_emissions = coal_emissions.T
natural_gas_emissions = natural_gas_emissions.T

print(coal_emissions.head())
print(natural_gas_emissions.head())

def transpose_and_reformat(df_all, column_name):
    df_all = df_all.T.reset_index()
    df_all.columns.name = None
    df_all = df_all.rename(columns={'index': 'year'})
    return df_all


coal_emissions = transpose_and_reformat(coal_emissions, 'emissions_coal')
natural_gas_emissions = transpose_and_reformat(natural_gas_emissions, 'emissions_gas')
#everything is working till now

coal_emissions_reset = coal_emissions.reset_index()

if 'index' in coal_emissions.columns:
    coal_emissions_reset = coal_emissions.drop(columns=['index'])

# Use Melt() to reshape your DataFrame
coal_emissions_melted = coal_emissions.melt(id_vars=['State'], var_name='Year', value_name='Emissions_coal')

natural_gas_emissions_reset = natural_gas_emissions.reset_index()
if 'index' in natural_gas_emissions.columns:
    natural_gas_emissions_reset = natural_gas_emissions.drop(columns=['index'])

natural_gas_emissions_melted = natural_gas_emissions.melt(id_vars=['State'], var_name='Year', value_name='Emissions_coal')

emissions_merged_coal_gas = coal_emissions_melted.merge(natural_gas_emissions_melted, on=['State', 'Year'], suffixes=('_coal', '_gas'))

# Rename the columns
emissions_merged_coal_gas = emissions_merged_coal_gas.rename(columns={'Emissions_coal_coal': 'Emissions_coal', 'Emissions_coal_gas': 'Emissions_natural_gas'})

#Read electricity_emissions data
electricity_emissions = pd.read_excel('electricity(2).xlsx', index_col=0)
electricity_emissions = electricity_emissions.T
electricity_emissions = electricity_emissions.reset_index()

electricity_emissions = transpose_and_reformat(electricity_emissions, 'emissions_electricity')

electricity_emissions_melted = electricity_emissions.melt(id_vars=['State'], var_name='state', value_name='emissions_electricity')

electricity_emissions_melted = electricity_emissions_melted.rename(columns={'state': 'Year'})


merged_data_all = emissions_merged_coal_gas.merge(electricity_emissions_melted, on=['State', 'Year'])


# Group the data by year and calculate the sum of emissions for each category
grouped_data_all = merged_data_all.groupby('Year').sum().reset_index()

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(grouped_data_all['Year'], grouped_data_all['Emissions_coal'], label='Coal')
plt.plot(grouped_data_all['Year'], grouped_data_all['Emissions_natural_gas'], label='Natural Gas')
plt.plot(grouped_data_all['Year'], grouped_data_all['emissions_electricity'], label='Electricity')

plt.xlabel('Year')
plt.ylabel('Total Emissions')
plt.title('Total Emissions from Coal, Natural Gas, and Electricity (1970–2020)')
plt.legend()
plt.savefig("Gas_Coal_Electricity_Emissions.png", dpi=300, bbox_inches='tight')
plt.show()

#FINALLY ONTO JUST ELECTRICITY NOw


alabama_emissions = pd.read_excel('alabama.xlsx', index_col=0)

alabama_emissions.reset_index(inplace=True)

alabama_emissions.columns.values[0] = 'Emissions'


electric_power_sector_start = alabama_emissions[alabama_emissions['Emissions'].str.contains('Electric Power Sector', na=False)].index[0]

electric_power_sector_data = alabama_emissions.iloc[electric_power_sector_start:electric_power_sector_start + 5, :]



# Function to process a single state file
def process_state_file(file_name):
    # Load the state's emissions data
    state_emissions = pd.read_excel(file_name, index_col=0)
    state_emissions.reset_index(inplace=True)
    state_emissions.columns.values[0] = 'Emissions'

    # Find the start of the 'Electric Power Sector' data
    electric_power_sector_start = state_emissions[state_emissions['Emissions'].str.contains('Electric Power Sector', na=False)].index[0]
    
    # Slice out the 'Electric Power Sector' data
    electric_power_sector_data = state_emissions.iloc[electric_power_sector_start:electric_power_sector_start + 5, :]
    
    # Get the state's name from the file name
    state_name = os.path.splitext(os.path.basename(file_name))[0]
    
    # Add a 'state' column to the dataframe
    electric_power_sector_data['State'] = state_name

    return electric_power_sector_data


import os

# Path to the directory containing all state files
directory_path = "Electric Emissions" 

all_states_data = pd.DataFrame()

for file_name in os.listdir(directory_path):
    if file_name.endswith(".xlsx"):
        file_path = os.path.join(directory_path, file_name)
        state_data = process_state_file(file_path)
        all_states_data = all_states_data.append(state_data, ignore_index=True)

# Create a dictionary mapping current column names to new column names
column_mapping = {
    'Emissions': 'Sector',
    'Unnamed: 1': 'Fossil Fuels',
    'Unnamed: 2': '1970',
    'Unnamed: 3': '1971',
    'Unnamed: 4': '1972',
    'Unnamed: 5': '1973',
    'Unnamed: 6': '1974',
    'Unnamed: 7': '1975',
    'Unnamed: 8': '1976',
    'Unnamed: 9': '1977',
    'Unnamed: 10': '1978',
    'Unnamed: 11': '1979',
    'Unnamed: 12': '1980',
    'Unnamed: 13': '1981',
    'Unnamed: 14': '1982',
    'Unnamed: 15': '1983',
    'Unnamed: 16': '1984',
    'Unnamed: 17': '1985',
    'Unnamed: 18': '1986',
    'Unnamed: 19': '1987',
    'Unnamed: 20': '1988',
    'Unnamed: 21': '1989',
    'Unnamed: 22': '1990',
    'Unnamed: 23': '1991',
    'Unnamed: 24': '1992',
    'Unnamed: 25': '1993',
    'Unnamed: 26': '1994',
    'Unnamed: 27': '1995',
    'Unnamed: 28': '1996',
    'Unnamed: 29': '1997',
    'Unnamed: 30': '1998',
    'Unnamed: 31': '1999',
    'Unnamed: 32': '2000',
    'Unnamed: 33': '2001',
    'Unnamed: 34': '2002',
    'Unnamed: 35': '2003',
    'Unnamed: 36': '2004',
    'Unnamed: 37': '2005',
    'Unnamed: 38': '2006',
    'Unnamed: 39': '2007',
    'Unnamed: 40': '2008',
    'Unnamed: 41': '2009',
    'Unnamed: 42': '2010',
    'Unnamed: 43': '2011',
    'Unnamed: 44': '2012',
    'Unnamed: 45': '2013',
    'Unnamed: 46': '2014',
    'Unnamed: 47': '2015',
    'Unnamed: 48': '2016',
    'Unnamed: 49': '2017',
    'Unnamed: 50': '2018',
    'Unnamed: 51': '2019',
    'Unnamed: 52': '2020',
   
   
}

# Rename the columns
all_states_data.rename(columns=column_mapping, inplace=True)


###



# Make a list of the year columns
year_columns = [str(year) for year in range(1970, 2021)]

# Melt the DataFrame to long format
all_states_data_long = all_states_data.melt(id_vars=['State', 'Fossil Fuels'], value_vars=year_columns, var_name='year', value_name='emissions')

# Pivot the DataFrame to wide format with separate columns for each type of fossil fuel
all_states_data_pivot = all_states_data_long.pivot_table(index=['State', 'year'], columns='Fossil Fuels', values='emissions').reset_index()

# Now you can calculate the percentages as before
all_states_data_pivot['coal_pct'] = all_states_data_pivot['Coal'] / all_states_data_pivot['Total'] * 100
all_states_data_pivot['Petroleum Products_pct'] = all_states_data_pivot['Petroleum Products'] / all_states_data_pivot['Total'] * 100
all_states_data_pivot['Natural Gas_pct'] = all_states_data_pivot['Natural Gas'] / all_states_data_pivot['Total'] * 100


# Define a function to plot the data for a given state
def plot_state(data, state_name):
    state_data = data[data['State'] == state_name]

    plt.figure(figsize=(10, 6))
    plt.plot(state_data['year'], state_data['coal_pct'], label='Coal')
    plt.plot(state_data['year'], state_data['Petroleum Products_pct'], label='Petroleum Products')
    plt.plot(state_data['year'], state_data['Natural Gas_pct'], label='Natural Gas')

    plt.xlabel('Year')
    plt.ylabel('Emissions (%)')
    plt.title(f' Electricity: Fossil Fuel Emissions breakdown for {state_name}')
    plt.legend()
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)
   
   # Set the frequency of ticks on the x-axis
    plt.xticks(state_data['year'][::5])  # Show a tick every 5 years
    
# Use the function to plot the data for a specific state
plot_state(all_states_data_pivot, 'alabama')
plt.savefig("alabama_electricity.png", dpi=300, bbox_inches='tight')


# Calculate total emissions for each state
total_emissions_electricity = all_states_data_pivot.groupby('State')['Total'].sum().sort_values(ascending=False)

# Get the top 5 states
top_5_states_electricity = total_emissions_electricity.index[:5]

plt.figure(figsize=(12,8))

# Iterate over each state and plot their data
for state in top_5_states_electricity:
    state_data = all_states_data_pivot[all_states_data_pivot['State'] == state]
    plt.plot(state_data['year'], state_data['Total'], label=state)

plt.xlabel('Year')
plt.ylabel('Emissions')
plt.title('Emissions over time for top 5 states')
plt.legend()
# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Set the frequency of ticks on the x-axis
plt.xticks(state_data['year'][::5])  # Show a tick every 5 years
plt.savefig("Electricity_Emissions_Top_5_States.png", dpi=300, bbox_inches='tight')

plt.show()


print(all_states_data_pivot['State'].unique())
print(top_5_states)

import seaborn as sns

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plot the data
sns.lineplot(data=all_states_data_pivot, x='year', y='Coal', label='Coal', ax=ax)
sns.lineplot(data=all_states_data_pivot, x='year', y='Natural Gas', label='Natural Gas', ax=ax)
sns.lineplot(data=all_states_data_pivot, x='year', y='Petroleum Products', label='Petroleum Products', ax=ax)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Emissions')
ax.set_title('Electricity: Change in Fossil Fuel Emissions from 1970 to 2021')

# Set the frequency of ticks on the x-axis
ax.xaxis.set_major_locator(plt.MaxNLocator(10))  # Show a maximum of 10 ticks on the x-axis

plt.savefig("Electricity_Change_In_FossilFuels.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10,6))

# Plot the data
sns.lineplot(data=all_states_data_pivot, x='year', y='Coal_pct', label='Coal', ax=ax)
sns.lineplot(data=all_states_data_pivot, x='year', y='Natural Gas_pct', label='Natural Gas', ax=ax)
sns.lineplot(data=all_states_data_pivot, x='year', y='Petroleum Products_pct', label='Petroleum Products', ax=ax)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Emissions (%)')
ax.set_title('Change in Electricty Sector: Fossil Fuel Emissions from 1970 to 2020 (%)')

# Set the frequency of ticks on the x-axis
ax.xaxis.set_major_locator(plt.MaxNLocator(10))  # Show a maximum of 10 ticks on the x-axis
plt.savefig("Percentage_Change_Electricity_Sector.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()


# Plot the data for each of these states
for state in top_5_states:
    plot_state(all_states_data_pivot, state)
plt.show()

all_states_data_pivot['Total'] = all_states_data_pivot[['Coal', 'Petroleum Products', 'Natural Gas']].sum(axis=1)

def plot_trends(data):
    plt.figure(figsize=(12, 8))

    for fuel in ['Coal', 'Petroleum Products', 'Natural Gas']:
        data[fuel + '_pct'] = data[fuel] / data['Total'] * 100
        plt.plot(data['year'], data[fuel + '_pct'], label=fuel)

    plt.xlabel('year')
    plt.ylabel('Emissions (%)')
    plt.title('Average Emissions from Fossil Fuels Over Time')
    plt.legend()

plot_trends(all_states_data_pivot)
def plot_trends(data):
    plt.figure(figsize=(12, 8))

    for fuel in ['Coal', 'Petroleum Products', 'Natural Gas']:
        data[fuel + '_pct'] = data[fuel] / data['Total'] * 100
        plt.plot(data['year'], data[fuel + '_pct'], label=fuel)

    plt.xlabel('Year')
    plt.ylabel('Emissions (%)')
    plt.title('Average Emissions from Fossil Fuels Over Time')
    plt.legend()

plot_trends(all_states_data_pivot)





