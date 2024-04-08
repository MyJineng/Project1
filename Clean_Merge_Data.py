#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from pathlib import Path


# In[2]:


# Specify the new directory path
new_directory = 'C:\\Users\\chris\\Documents\\Project 1'

# Change the current working directory
os.chdir(new_directory)

# Print the new current working directory
print("New Current Working Directory:", os.getcwd())


# In[3]:


# Study data files
GDP_csv = Path("Data\\GDP per capita (constant 2015 US$).csv")
age_csv = Path("Data\\age.csv")
social_media_csv = Path("Data\\social-media-users-by-country-2024.csv") 
pop_csv = Path("Data\\pop.csv")


# In[4]:


# Generate population DataFrame from csv file
raw_GDP_data = pd.read_csv(GDP_csv)

# Take the columns we want
raw_GDP_data = raw_GDP_data[["Country Name", "2022 [YR2022]"]]

# Remove invalid entries (NaN)
raw_GDP_data = raw_GDP_data.dropna()

# Specify the name to delete
name_to_delete = "GNI per capita (constant 2015 US$)"

# Read the CSV file
with open("Data\\GDP per capita (constant 2015 US$).csv", 'r', newline='') as file:
    reader = csv.reader(file)
    data = [row for row in reader if row[0] != name_to_delete]

# Write the filtered data to a new CSV file
with open("Data\\GDP per capita (constant 2015 US$).csv", 'w', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(data)

GDP_data = raw_GDP_data.rename(columns={"Country Name": f"Country",
                                           "2022 [YR2022]": f"GDP per capita"})


# Convert "GDP per capita" column to numeric values
GDP_data["GDP per capita"] = pd.to_numeric(GDP_data["GDP per capita"], errors='coerce')

# Filter for GDP values of 20,000 or higher
GDP_data_final = GDP_data.loc[GDP_data["GDP per capita"] >= 20000]

GDP_data_final.head()


# In[5]:


# Generate age DataFrame from csv file
raw_age_data = pd.read_csv(age_csv)

# Take the columns we want
raw_age_data = raw_age_data[["country", "MedianAge2023"]]

# Remove invalid entries (NaN)
raw_age_data = raw_age_data.dropna()

# Rename columns
age_data = raw_age_data.rename(columns={"country": f"Country",
                                        "MedianAge2023": f"Median Age"})

# Median Age of 20 or higher:
age_data_final = age_data.loc[age_data["Median Age"] >= 20]

age_data_final 


# In[6]:


# Generate population DataFrame from csv file
raw_SM_data = pd.read_csv(social_media_csv)

# Take the columns we want
raw_SM_data = raw_SM_data[["country", "SocialMediaUsersTotal2023"]]

# Remove invalid entries (NaN)
raw_SM_data = raw_SM_data.dropna()

# Rename columns
SM_data = raw_SM_data.rename(columns={"country": f"Country",
                                          "SocialMediaUsersTotal2023": f"Social Media Users"})

SM_data


# In[7]:


# Generate population DataFrame from csv file
raw_pop_data = pd.read_csv(pop_csv, encoding='unicode_escape')

# Remove unnecessary columns
raw_pop_data = raw_pop_data[["Country (or dependency)", "Population"]]

# Remove invalid entries (NaN)
pop_data = raw_pop_data.dropna()

# Rename columns
pop_data = raw_pop_data.rename(columns={"Country (or dependency)": f"Country",
                                          "Population": f"Population"})

# Remove the row at index 1 using iloc
pop_data = pop_data.drop(pop_data.index[0])

pop_data


# In[8]:


# Combine the data into a single DataFrame
merged_df = GDP_data_final.merge(age_data_final, how="inner", on=["Country"]).merge(SM_data, how="inner", on=["Country"]).merge(pop_data, how="inner", on=["Country"])

# Convert columns to numeric types
merged_df["Social Media Users"] = pd.to_numeric(merged_df["Social Media Users"], errors='coerce')
merged_df["GDP per capita"] = pd.to_numeric(merged_df["GDP per capita"], errors='coerce')


# Convert columns to numbers
merged_df["Population"] = merged_df["Population"].replace({'\$':'',',':''}, regex = True)
merged_df["Population"] = merged_df["Population"].astype(int)


# Display the data table for preview
merged_df.head()


# In[9]:


# Drop rows with missing values
merged_df.dropna(subset=["Social Media Users", "GDP per capita", "Median Age", "Population"], inplace=True)
merged_df.head()


# In[10]:


# percentage of total population utilizing social media
merged_df["% Population"] = merged_df["Social Media Users"] / merged_df["Population"]
merged_df.head()


# In[11]:


# Calculate line of best fit
def create_scatter1 (df, x_value , y_value, coords = (0,0)) : 
    (slope, intercept, rvalue, pvalue, stderr) = linregress(df[x_value], df[y_value])
    regress_values = df[x_value] * slope + intercept
    line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))
    
    
    # Plot data
    plt.scatter(df[x_value], df[y_value])
    
    # Add line of best fit
    plt.plot(df[x_value],regress_values,"r-")
    plt.annotate(line_eq,coords,fontsize=12,color="red")
    
    # Label chart
    plt.title(f"{x_value} vs. {y_value}")
    plt.xlabel(x_value)
    plt.ylabel(y_value)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    plt.savefig("Chart Images") 
    plt.show()

create_scatter1(merged_df, "% Population", "GDP per capita", (600000000, 200000))


# In[12]:


# Calculate line of best fit
def create_scatter2 (df, x_value , y_value2, coords = (0,0)) : 
    (slope, intercept, rvalue, pvalue, stderr) = linregress(df[x_value], df[y_value2])
    regress_values = df[x_value] * slope + intercept
    line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))
    
    
    # Plot data
    plt.scatter(df[x_value], df[y_value2])
    
    # Add line of best fit
    plt.plot(df[x_value],regress_values,"r-")
    plt.annotate(line_eq,coords,fontsize=12,color="red")
    
    # Label chart
    plt.title(f"{x_value} vs. {y_value2}")
    plt.xlabel(x_value)
    plt.ylabel(y_value2)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    plt.savefig("Chart Images") 
    plt.show()

create_scatter2(merged_df, "% Population", "Median Age", (600000000, 200000))

