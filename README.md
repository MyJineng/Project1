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
	Outcome: There are no releationships between share of top influencers and share of usage of a given social media platform. Although, the US dominates top social media users, there are some outliers such as South Korea (2nd) for Instagram and India (1st) for Youtube. Tiktok has a more dispursed distribution than Instagram and Youtube. The market share of a social media platform does not seem to have an effect on the suicide rate, although Tiktok users as a % of social media users vs the suicide rtae has an R value of -0.56.
