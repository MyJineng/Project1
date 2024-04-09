
# Internet and Social Media Usage Analysis

## Project Overview

This project aims to analyze the trends in internet and social media usage worldwide from 2014 to 2022. It explores the year-to-year percentage changes in global internet usage and compares it with the growth of social media users, providing insights into how these two metrics are interrelated.

## Features

- **Data Cleaning**: Scripts to clean and prepare the World Bank's internet usage data and social media usage data.
- **Data Analysis**: Examination of year-to-year percentage changes in internet and social media usage.
- **Visualization**: Generation of plots to visually represent the relationship between internet usage and social media growth over the years.

 ## Findings Overview
The analysis reveals that internet and social media penetration are closely correlated yet are influenced by a diverse range of factors including economic development, infrastructure availability, and societal norms. Key insights include:
- A consistent growth in global internet and social media users, with notable year-to-year fluctuations.
- The impact of global events on internet and social media usage rates.
- The varying pace of growth between different regions and countries, highlighting the digital divide.

For detailed insights and visualizations, refer to the output of the script which includes plots and tables 
showing the percentage change in internet and social media usage year-to-year.


  

  ## Data Sources

- Internet usage data: Provided by the World Bank.
- Social media usage data: BarGraph Globalview
=======
# Probing Social Media Usage
Team: Amato, Andrew | Gabriel, Christina | Lopez rodriguez, Gerardo | Schiffner, Steven
### Analyses to be done
1.) Take social media statistics by country and generate scatter plots with different population statistics (Christina)
	i. Merge (1), (2), and (3) on "country" (and potentially more if we want to)
	ii. Clean (remove any countries with incomplete or old data)
	iii. Make plots
	iv. Determine lines of fit etc.

Extraction, Loading, and Transformation:
Created new directory path. Loaded in csv files. Cleaned data: removed columns/rows of dataset that were irrelevant, removed invalid entries, removed missing values, converted string values to numeric values, narrowed data by most recent/relevant values. Merged datasets into one single data frame. Calculated percentage of social media users for each country. Created scatterplots with lines of best fit to illustrate correlation between social media usage and GPD/median age. 

Outcome:
Based on the data, it appears there is a correlation (negative relationship) between the population of social media users and GDP per capita. There is a notable cluster of populations with a GDP between 20,000-105,000 and a social media user population between 0.6%-1.0%. Therefore, it appears countries with a lower GDP had the largest population of social media usage with one significant outlier: Monaco has a large GDP and a very low social media usage. In conclusion, as the social media usage increased, the GDP became lower. Furthermore, it appears there is a correlation (negative relationship) between the population of social media users and median age. There is a notable cluster of age around 37 - 50 years old and a social media user population between 0.6%-0.9%. Therefore, it appears middle-aged age groups have the largest population of social media usage with one significant outlier: population around 55 years old have very low social media usage. In conclusion, most social users appears to be between 30-35 years old.

2.) Same thing but for users of YouTube, TikTok, and Instagram (Steven)
   
Extraction, Loading, and Transformation:
After merging together different DataFrames containing data for the population, GDP, median age, Facebook usage and TikTok usage for various countries, then cleaning the data to convert it to the proper data type and remove rows with bad entries, I placed the data into scatter plots and performed a linear regression analysis.

Outcome:
At first we saw a positive correlation, but after restricting the data to GDPs and median ages above a certain mark in order to remove potential outliers, we saw no correlation almost across the board, except for in the case of TikTok usage vs. median age where we saw a weak negative correlation (r=.55).

3.) Compare internet usage (6) vs. social media usage (7) over time (Gerardo)
	i. Make tables for year-to-year change in social media & internet usage over time
	ii. Plot the values together (double-bar graph or line graph) to see if they are similar as hypothesized
 
Extraction, Loading, and Transformation:
We chose the World Bank data for its reliability and comprehensive coverage of global internet usage. For social media usage, we gathered data reflecting the number of users worldwide from reputable sources. Our Python code played a crucial role in cleaning and preparing this data for analysis. We focused on the years 2014 to 2022 to capture recent trends and used Pandas for data manipulation and Matplotlib for visualization.

Outcome:
The analysis reveals that internet and social media penetration are closely correlated yet are influenced by a diverse range of factors including economic development, infrastructure availability, and societal norms. Key insights include:
A consistent growth in global internet and social media users, with notable year-to-year fluctuations.
The impact of global events on internet and social media usage rates.
 
4.) Compare share of social media users by country (1) with share of top influencers on a given platform by country (5) (Andrew)

Extraction, Loading, and Transformation: 
Youtube, tiktok, and instagram.csv were loaded and compared against world.csv using a foreloop called mktsmall.csv. Next, the percentage of users using each type of platform was calculated. Then, a csv for each platforms top 1000 influencers was used to create dataframes. The data was then transformed into a count of influencers by country before being merged with mktsmall. Data was sourced from World Population Review (users and suicide rate) and Kaggle (top influencers).

Outcome: 
There are no releationships between share of top influencers and share of usage of a given social media platform. Although, the US dominates top social media users, there are some outliers such as South Korea (2nd) for Instagram and India (1st) for Youtube. Tiktok has a more dispursed distribution than Instagram and Youtube. It is interesting that South Korea has many bands and band members in the top 100 Instagram accounts but does not have a presence in Youtube since many of India's top Youtube channels are also music based. The market share of a social media platform does not seem to have an effect on the suicide rate, although Tiktok users as a % of social media users vs the suicide rtae has an R value of -0.56. 

