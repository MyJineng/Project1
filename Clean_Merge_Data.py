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

#Andrew
#Loading Data
path = r'..\country_data'
mktsmall = pd.read_csv(rf'{path}\facebook.csv')
csvs = ['youtube', 'tiktok', 'world', 'instagram']
for x in csvs:
    csv = pd.read_csv(f'{path}\{x}.csv')
    tdf = pd.DataFrame(csv)
    mktsmall = mktsmall.merge(tdf, how='inner', on="country")

# creating new columns
mktsmall["tiktok %"] = round((mktsmall['TikTokUsersCountryTotal2023'] / mktsmall["users"] * 100), 2)
mktsmall["youtube %"] = round((mktsmall['YouTubeUsersJuly2023'] / mktsmall["users"] * 100), 2)
mktsmall["facebook %"] = round((mktsmall['FacebookUsersTotal2023'] / mktsmall["users"] * 100), 2)
mktsmall["instagram %"] = round((mktsmall['InstagramUsers2023'] / mktsmall["users"] * 100), 2)
# data frames used for plots later
plotdf = mktsmall[["instagram %", "country"]]
plotbdf = mktsmall[["tiktok %", "country"]]

# resetting index so influencers by country of origin is a colunn
idf = pd.read_csv(rf'{path}\top_1000_instagramers.csv')
idf = idf["country"].value_counts().reset_index()
idf = idf.rename(columns={'country': 'insta_influencers', 'index': 'country', })

# Bargraphs of influencers by country
plot = idf.plot(kind="bar", figsize=(20, 5))
plot.set_xticklabels(idf["country"], rotation=45)
plt.title("Top 100 Instagram Influencers by Country")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

tdf = pd.read_csv(rf'{path}\top_1000_tiktok.csv')
tdf = tdf["country"].value_counts().reset_index()
tdf = tdf.rename(columns={'country': 'tiktok_influencers', 'index': 'country', })

plot = tdf.plot(kind="bar", figsize=(20, 5))
plot.set_xticklabels(tdf["country"], rotation=45)
plt.title("Top 100 Tiktok Influencers by Country")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

ydf = pd.read_csv(rf'{path}\top_1000_yt.csv')
ydf = ydf["country"].value_counts().reset_index()
ydf = ydf.rename(columns={'country': 'yt_influencers', 'index': 'country', })

plot = ydf.plot(kind="bar", figsize=(20, 5))
plot.set_xticklabels(ydf["country"], rotation=45)
plt.title("Top 100 Youtube Influencers by Country")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# mergeing dataframes to get side by side view of countries amount of influencers and market share of total SM users
mktsmall = mktsmall.merge(idf, how='outer', on="country")
mktsmall = mktsmall[['country', 'instagram %', "tiktok %", "youtube %", 'insta_influencers']]
mktsmall = mktsmall.merge(tdf, how='outer', on="country")
mktsmall = mktsmall[['country', 'instagram %', "tiktok %", "youtube %", 'insta_influencers', 'tiktok_influencers']]
mktsmall = mktsmall.merge(ydf, how='inner', on="country")
mktsmall = mktsmall[
    ['country', 'instagram %', "tiktok %", "youtube %", 'insta_influencers', 'tiktok_influencers', 'yt_influencers', ]]
# bargraph
mktsmall = mktsmall.drop(index=[11, 12])
multi_plot = mktsmall.plot(kind="bar", figsize=(20, 5))
multi_plot.set_xticklabels(mktsmall["country"], rotation=45)
plt.title("Top 100 Influencers by Country")

# scatterplots comparing amount of market share by platform to amount of top influencers
plotadf = plotdf.merge(idf, how='outer', on="country")
plotadf.plot.scatter(x='instagram %', y='insta_influencers', s=100, edgecolor="red");
plt.title("Instagram Usage and Market Share of all Users")
plt.scatter(plotadf["instagram %"], plotadf["insta_influencers"])
plt.show()

# Regression lines to find R values
sdf = pd.read_csv(rf'{path}\srate.csv')
plotadf = plotdf.merge(sdf, how='inner', on="country")
(slope, intercept, rvalue, pvalue, stderr) = linregress(plotadf['instagram %'], plotadf["suicide_rate"])
regress_values = plotadf["instagram %"] * slope + intercept
print(f'Instagram users as a % of social media users vs suicide R value: {rvalue.round(2)}')
plotbdf = plotbdf.merge(sdf, how='inner', on="country")

(slope, intercept, rvalue, pvalue, stderr) = linregress(plotbdf['tiktok %'], plotbdf["suicide_rate"])
regress_values = plotbdf["tiktok %"] * slope + intercept
print(f'Tiktok users as a % of social media users vs suicide R value: {rvalue.round(2)}')

# Final scatterplots comparing ssocial media market share to amount of top influencers
idf = idf.merge(sdf, how='inner', on="country")
idf.plot.scatter(x='suicide_rate', y='insta_influencers', s=100, edgecolor="red");
plt.title("Instagram vs Suicide")
ydf = ydf.merge(sdf, how='inner', on="country")
ydf.plot.scatter(x='suicide_rate', y='yt_influencers', s=100, edgecolor="red");
plt.title("Youtube vs Suicide")
tdf = tdf.merge(sdf, how='inner', on="country")
tdf.plot.scatter(x='suicide_rate', y='tiktok_influencers', s=100, edgecolor="red");
plt.title("TikTok vs Suicide")
plt.show()
