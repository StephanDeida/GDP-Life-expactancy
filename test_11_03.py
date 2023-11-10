import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data files
gdp_data = pd.read_csv('gdp-per-capita-maddison.csv')
life_expectancy_data = pd.read_csv('life-expectancy.csv')

# Filter the data for the desired regions
gdp_data = gdp_data[(gdp_data['Year']>= 1950) & (gdp_data['Year'] <= 2018)]
life_expectancy_data = life_expectancy_data[(life_expectancy_data['Year']>=1950) & (life_expectancy_data['Year']<=2018)]

# Merge the two files based on "Entity" and "Year"
merged_data = pd.merge(gdp_data, life_expectancy_data, on=['Entity', 'Year'])

# print(gdp_data["Entity"].unique().tolist(), life_expectancy_data["Entity"].unique().tolist())
# print(len(gdp_data), len(life_expectancy_data), len(merged_data))
# print(merged_data)
# Extract the columns for GDP per capita and life expectancy
gdp_per_capita = merged_data['GDP per capita']
life_expectancy = merged_data['Period life expectancy at birth - Sex: all - Age: 0']

colors = ['red', 'green', 'blue', 'yellow'] 
# Create a scatter plot
plt.scatter(life_expectancy, gdp_per_capita, c=merged_data['Entity'].astype('category').cat.codes, cmap='tab10')

# Add labels and title
plt.ylabel('GDP per capita')
plt.xlabel('Life expectancy')
plt.title('Scatter Plot of GDP per capita vs Life Expectancy')

# Show the plot
plt.show()
