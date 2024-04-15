
# Internet and Social Media Usage Analysis
Team: Amato, Andrew | Gabriel, Christina | Lopez rodriguez, Gerardo | Schiffner, Steven

## Project Overview

This project aims to analyze the trends in internet and social media usage worldwide from 2014 to 2022. It explores the year-to-year percentage changes in global internet usage and compares it with the growth of social media users, providing insights into how these two metrics are interrelated.

## Findings Overview
The analysis reveals that internet and social media penetration are closely correlated yet are influenced by a diverse range of factors including economic development, infrastructure availability, and societal norms. Key insights include:
- A consistent growth in global internet and social media users, with notable year-to-year fluctuations.
- The impact of global events on internet and social media usage rates.
- The varying pace of growth between different regions and countries, highlighting the digital divide.

For detailed insights and visualizations, refer to the output of the script which includes plots and tables 
showing the percentage change in internet and social media usage year-to-year.

### Findings Summary
The analysis involved gathering social media statistics by country and creating scatter plots with various population statistics. The process included merging datasets, cleaning data by removing incomplete or old entries, and converting string values to numeric ones. Scatterplots with lines of best fit were generated to explore correlations between social media usage and GDP/median age.

The findings indicated a negative correlation between social media user population and GDP per capita. Countries with lower GDPs tended to have larger populations of social media users, with Monaco being a significant outlier due to its high GDP and low social media usage. Similarly, there was a negative correlation between social media user population and median age, with middle-aged groups showing the highest usage rates.

A similar analysis was conducted for YouTube, TikTok, and Instagram users, revealing weak correlations and some outliers after data cleaning and linear regression analysis.

Additionally, the comparison between internet and social media usage over time showed consistent growth with fluctuations, influenced by factors like economic development and global events.

Lastly, the analysis comparing the share of social media users by country with the share of top influencers on platforms like YouTube, TikTok, and Instagram found no clear relationships. The distribution of top influencers varied across countries, with some interesting patterns such as South Korea's dominance in Instagram influencers despite not being prominent in YouTube influencers. Instagram influencers were mostly bands and band members so it would be expected that they be as popular as Indian music conglomerates that dominate Youtube such as T-Series. There were also no significant observations regarding social media platform distribution and its correlation with suicide rates.
  
## Data Sources

- Internet usage data: Provided by the World Bank.
- Social media usage data: BarGraph Globalview
- World Population Review: users and suicide rate
  (https://worldpopulationreview.com/country-rankings/social-media-users-by-country)
  (https://worldpopulationreview.com/country-rankings/instagram-users-by-country)
  (https://worldpopulationreview.com/country-rankings/tiktok-users-by-country)
  (https://worldpopulationreview.com/country-rankings/youtube-users-by-country)
  (https://worldpopulationreview.com/country-rankings/suicide-rate-by-country)
- Kaggle: top influencers
  (https://www.kaggle.com/datasets/ramjasmaurya/top-1000-social-media-channels?select=social+media+influencers+-+Tiktok+sep+2022.csv)
