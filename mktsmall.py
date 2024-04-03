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
idf = idf.rename(columns={'country': 'influencers','index': 'country', })
mktsmall = mktsmall.merge(idf, how='inner', on="country")
mktsmall = mktsmall[['country', 'instagram %', 'influencers']]
bargraph
multi_plot = mktsmall.plot(kind="bar", figsize=(20,5))
multi_plot.set_xticklabels(mktsmall["country"], rotation=45)
plt.title("Top 100 Instagram Influencers by Country")
plt.xlabel("Country")
plt.show()
plt.tight_layout()


