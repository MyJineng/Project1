# Import dependencies
import numpy as np
import pandas as pd

# Generate population DataFrame from csv file
raw_pop_data = pd.read_csv("country_data/pop.csv", encoding='unicode_escape')

# Remove unnecessary columns
raw_pop_data = raw_pop_data[["Country (or dependency)", "Population"]]

# Remove invalid entries (NaN)
pop_data = raw_pop_data.dropna()

# Rename columns
pop_data.columns = ["Country", "Population"]

# Generate age DataFrame from csv file
raw_age_data = pd.read_csv("country_data/age.csv")

# Take the columns we want
raw_age_data = raw_age_data[["country", "MedianAge2023"]]

# Remove invalid entries (NaN)
age_data = raw_age_data.dropna()

# Rename columns
age_data.columns = ["Country", "Median Age"]

# Generate GDP DataFrame from csv file
raw_gdp_data = pd.read_csv("country_data/gdp.csv")
raw_gdp_data

# Take the columns we want
raw_gdp_data = raw_gdp_data[["country", "GdpPerCapitaIMF_USD_23"]]

# Remove invalid entries (NaN)
gdp_data = raw_gdp_data.dropna()

# Rename columns
gdp_data.columns = ["Country", "GDP Per Capita (USD)"]

# We need to merge our DataFrames
population_statistics = pop_data.merge(gdp_data, how="inner", on="Country").merge(age_data, how="inner", on="Country")

# Convert columns to numbers
population_statistics["Population"] = population_statistics["Population"].replace({'\$':'',',':''}, regex = True)
population_statistics["Population"] = population_statistics["Population"].astype(int)

# Drop rows with invalid entries
population_statistics.dropna()

print(population_statistics)
