import pandas as pd
pd.options.display.max_columns = None
import matplotlib.pyplot as plt
import numpy as np

path = 'C:\PycharmProjects\project'
mktsmall = pd.read_csv(rf'{path}\facebook.csv')
csvs = ['youtube', 'tiktok', 'world', 'instagram']
for x in csvs:
    csv = pd.read_csv(f'{path}\{x}.csv')
    tdf = pd.DataFrame(csv)
    mktsmall = mktsmall.merge(tdf, how='inner', on="country")

mktsmall["tiktok %"] = round((mktsmall['TikTokUsersCountryTotal2023'] / mktsmall["users"] * 100), 2)
mktsmall["youtube %"] = round((mktsmall['YouTubeUsersJuly2023'] / mktsmall["users"] * 100), 2)
mktsmall["facebook %"] = round((mktsmall['FacebookUsersTotal2023'] / mktsmall["users"] * 100), 2)
mktsmall["instagram %"] = round((mktsmall['InstagramUsers2023'] / mktsmall["users"] * 100), 2)

idf = pd.read_csv(rf'{path}\top_1000_instagramers.csv')
idf = idf["country"].value_counts().reset_index()
idf = idf.rename(columns={'country': 'insta_influencers','index': 'country', })

plot = idf.plot(kind="bar", figsize=(20,5))
plot.set_xticklabels(idf["country"], rotation=45)
plt.title("Top 100 Instagram Influencers by Country")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

tdf = pd.read_csv(rf'{path}\top_1000_tiktok.csv')
tdf = tdf["country"].value_counts().reset_index()
tdf = tdf.rename(columns={'country': 'tiktok_influencers','index': 'country', })

plot = tdf.plot(kind="bar", figsize=(20,5))
plot.set_xticklabels(tdf["country"], rotation=45)
plt.title("Top 100 Tiktok Influencers by Country")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

ydf = pd.read_csv(rf'{path}\top_1000_yt.csv')
ydf = ydf["country"].value_counts().reset_index()
ydf = ydf.rename(columns={'country': 'yt_influencers','index': 'country', })

plot = ydf.plot(kind="bar", figsize=(20,5))
plot.set_xticklabels(ydf["country"], rotation=45)
plt.title("Top 100 Youtube Influencers by Country")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

print(idf, tdf, ydf)

mktsmall = mktsmall.merge(idf, how='outer', on="country")
mktsmall = mktsmall[['country', 'instagram %', "tiktok %", "youtube %", 'insta_influencers']]
mktsmall = mktsmall.merge(tdf, how='outer', on="country")
mktsmall = mktsmall[['country', 'instagram %', "tiktok %", "youtube %", 'insta_influencers', 'tiktok_influencers']]
mktsmall = mktsmall.merge(ydf, how='outer', on="country")
mktsmall = mktsmall[['country', 'instagram %', "tiktok %", "youtube %", 'insta_influencers', 'tiktok_influencers', 'yt_influencers',]]
#bargraph
# multi_plot = mktsmall.plot(kind="bar", figsize=(20,5))
# multi_plot.set_xticklabels(mktsmall["country"], rotation=45)
# plt.title("Top 100 Influencers by Country")
# plt.xlabel("Country")
# plt.tight_layout()
# plt.show()
#scatterplot
# mktsmall.plot.scatter(x = 'instagram %', y = 'insta_influencers', s = 100, edgecolor ="red");
# mktsmall.plot.scatter(x = 'tiktok %', y = 'tiktok_influencers', s = 100, edgecolor ="blue");
# mktsmall.plot.scatter(x = 'youtube %', y = 'yt_influencers', s = 100, edgecolor ="green");
# plt.show()