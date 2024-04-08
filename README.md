
# Internet and Social Media Usage Analysis

## Project Overview

This project aims to analyze the trends in internet and social media usage worldwide from 2014 to 2022. It explores the year-to-year percentage changes in global internet usage and compares it with the growth of social media users, providing insights into how these two metrics are interrelated.

## Features

- **Data Cleaning**: Scripts to clean and prepare the World Bank's internet usage data and social media usage data.
- **Data Analysis**: Examination of year-to-year percentage changes in internet and social media usage.
- **Visualization**: Generation of plots to visually represent the relationship between internet usage and social media growth over the years.

  ## Data Sources

- Internet usage data: Provided by the World Bank.
- Social media usage data: BarGraph Globalview
=======
# Probing Social Media Usage
Team: Amato, Andrew | Gabriel, Christina | Lopez rodriguez, Gerardo | Schiffner, Steven
### Analyses to be done
1. Take social media statistics by country and generate scatter plots with different population statistics (Christina)
	i. Merge (1), (2), and (3) on "country" (and potentially more if we want to)
	ii. Clean (remove any countries with incomplete or old data)
	iii. Make plots
	iv. Determine lines of fit etc.
2. Same thing but for users of YouTube, TikTok, and Instagram (Steven)
	i. Merge TikTok, Youtube, and IG data for a representative sample of countries with (2), (3), etc
	ii. Clean
	iii. Make plots
	iv. Determine lines of fit etc.
3. Compare internet usage (6) vs. social media usage (7) over time (Gerardo)
	i. Make tables for year-to-year change in social media & internet usage over time
	ii. Plot the values together (double-bar graph or line graph) to see if they are similar as hypothesized
4. Compare share of social media users by country (1) with share of top influencers on a given platform by country (5) (Andrew)
	i. Clean both (1) and (5)
	ii. Calculate overall social media share for each country in (1) - sum up all social media users and then create a new column equal to social media users in a given country divided by worldwide users, format as percent
	iii. Groupby (5) on "country," get count for each one, create a new column equal to count divided by 1000, format as percent
	iv. Remove all countries from (1) that are not present in (5)
	v. Create a chart comparing this data (double bar graph or line graph)
Extraction, Loading, and Transformation: youtube, tiktok, and instagram.csv were loaded and compared against world.csv using a foreloop called mktsmall.csv. Next, the percentage of users using each type of platform was calculated. Then, a csv for each platforms top 1000 influencers was used to create dataframes. The data was then transformed into a count of influencers by country before being merged with mktsmall. Data was sourced from World Population Review (users) and Kaggle (top influencers).
Outcome: There are no releationships between share of top influencers and share of usage of a given social media platform. Although, the US dominates top social media users, there are some outliers such as South Korea (2nd) for Instagram and India (1st) for Youtube. Tiktok has a more dispursed distribution than Instagram and Youtube. The market share of a social media platform does not seem to have an effect on the suicide rate, although Tiktok users as a % of social media users vs the suicide rtae has an R value of -0.56.

