#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from pathlib import Path


# In[2]:


pwd


# In[3]:


# Specify the new directory path
new_directory = 'C:\\Users\\chris\\Documents\\Project 1'

# Change the current working directory
os.chdir(new_directory)

# Print the new current working directory
print("New Current Working Directory:", os.getcwd())


# In[4]:


# Study data files
GDP_csv = Path("Data\\GDP per capita (constant 2015 US$).csv")
age_csv = Path("Data\\age.csv")
social_media_csv = Path("Data\\social-media-users-by-country-2024.csv") 


# In[5]:


# Generate population DataFrame from csv file
raw_GDP_data = pd.read_csv(GDP_csv)

# Take the columns we want
raw_GDP_data = raw_GDP_data[["Country Name", "2022 [YR2022]"]]

# Remove invalid entries (NaN)
raw_GDP_data = raw_GDP_data.dropna()


GDP_data = raw_GDP_data.rename(columns={"Country Name": f"Country",
                                           "2022 [YR2022]": f"GDP per capita"})

GDP_data


# In[6]:


# Generate age DataFrame from csv file
raw_age_data = pd.read_csv(age_csv)

# Take the columns we want
raw_age_data = raw_age_data[["country", "MedianAge2023"]]

# Remove invalid entries (NaN)
raw_age_data = raw_age_data.dropna()

# Rename columns
age_data = raw_age_data.rename(columns={"country": f"Country",
                                        "MedianAge2023": f"Median Age"})
age_data


# In[7]:


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


# In[8]:


# Combine the data into a single DataFrame
merged_df = GDP_data.merge(age_data, how="inner", on=["Country"]).merge(SM_data, how="inner", on=["Country"])

# Convert columns to numeric types
merged_df["Social Media Users"] = pd.to_numeric(merged_df["Social Media Users"], errors='coerce')
merged_df["GDP per capita"] = pd.to_numeric(merged_df["GDP per capita"], errors='coerce')

# Display the data table for preview
merged_df.head()


# In[9]:


print(merged_df.dtypes)


# In[10]:


# Drop rows with missing values
merged_df.dropna(subset=["Social Media Users", "GDP per capita", "Median Age"], inplace=True)
merged_df


# In[11]:


# # Check dimensions of the arrays
# print("Social Media Users array length:", len(merged_df["Social Media Users"]))
# print("GDP per capita array length:", len(merged_df["GDP per capita"]))

# # Ensure data alignment and matching dimensions
# if len(merged_df["Social Media Users"]) == len(merged_df["GDP per capita"]):
#     # Calculate line of best fit
#     (slope, intercept, rvalue, pvalue, stderr) = linregress(merged_df["Social Media Users"], merged_df["GDP per capita"])
#     regress_values = merged_df["Social Media Users"] * slope + intercept
#     line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))
# else:
#     print("Data dimensions do not match. Please align the data before performing linear regression.")


# In[12]:


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
    plt.show()

create_scatter1(merged_df, "Social Media Users", "GDP per capita", (600000000, 200000))


# In[13]:


# SM_GDP = merged_df.loc[(merged_df["GDP per capita"] < 200000) & (merged_df["Social Media Users"] < 200000000)]
# create_scatter1(SM_GDP, "Social Media Users", "GDP per capita", (600000000, 200000))


# In[14]:


# Calculate line of best fit
def create_scatter2 (df, x_value2 , y_value2, coords = (0,0)) : 
    (slope, intercept, rvalue, pvalue, stderr) = linregress(df[x_value2], df[y_value2])
    regress_values = df[x_value2] * slope + intercept
    line_eq = "y = " + str(round(slope, 2)) + "x + " + str(round(intercept, 2))
    
    
    # Plot data
    plt.scatter(df[x_value2], df[y_value2])
    
    # Add line of best fit
    plt.plot(df[x_value2],regress_values,"r-")
    plt.annotate(line_eq,coords,fontsize=12,color="red")
    
    # Label chart
    plt.title(f"{x_value2} vs. {y_value2}")
    plt.xlabel(x_value2)
    plt.ylabel(y_value2)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    plt.show()

create_scatter2(merged_df, "Social Media Users", "Median Age", (600000000, 200000))

