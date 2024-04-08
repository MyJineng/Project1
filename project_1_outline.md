## Project Outline

### Topics:

- What population-wide statistics correlate most closely with propensity for social media usage? (Age, wealth, education... use scatter plots to show correlation and bar graphs to help visualize data by country)
- What about for individual social networks? Is there a difference between indicators for usage of different platforms? (Use scatter plots to show correlation and bar graphs to help visualize data by country/by network)
- What is the trend looking like for social media usage? What can we expect social media usage to look like in 2030? Can we use data for internet usage to make this prediction, or are they separate? (Line graphs)
- When looking at the most popular accounts on a given platform, does the distribution of nationalities look similar to the distribution of social media users by country? (Scatter plots/bar graphs)

### Our datasets:
(1) https://worldpopulationreview.com/country-rankings/social-media-users-by-country (Social media users by country)
(2)
https://worldpopulationreview.com/country-rankings/median-age (Median age by country)
(3)
https://data.worldbank.org/indicator/NY.GDP.PCAP.KD (GDP per capita by country)
(4)
https://gs.statcounter.com/social-media-stats/all/eritrea (Social network market share by country)
(5)
https://www.kaggle.com/datasets/ramjasmaurya/top-1000-social-media-channels (2022 top 1000 influencers for TikTok, YouTube, and Instagram)
(6)
https://data.worldbank.org/indicator/IT.NET.USER.ZS (Internet penetration)
(7)
Social media penetration from Andrew's bar graph in Slack

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
