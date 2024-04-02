import pandas as pd

path = 'C:\PycharmProjects\project'
clist = ['AD', 'AE', 'AF', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BE', 'BF', 'BG', 'BH', 'BI',
         'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CF', 'CG', 'CH', 'CI', 'CL', 'CM', 'CN',
         'CO', 'CR', 'CU', 'CV', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EE', 'EG', 'ER', 'ES', 'ET', 'FJ',
         'FM',
         'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GT', 'GY', 'HN', 'HR', 'HT', 'HU',
         'ID',
         'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KW', 'KZ', 'LA',
         'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LY', 'MA', 'MC', 'MD', 'ME', 'MM', 'MN', 'MR', 'MT', 'MU',
         'MV',
         'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH',
         'PK', 'PL', 'PS', 'PT', 'PW', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SI', 'SK',
         'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SY', 'SZ', 'TD', 'TG', 'TH', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW',
         'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'WW', 'YE', 'ZA', 'ZM']
mcsv = pd.read_csv(f'{path}\ZW.csv')
mdf = pd.DataFrame(mcsv)
for x in clist:
    csv = pd.read_csv(f'{path}\{x}.csv')
    mktdf = pd.DataFrame(csv)
    mktdf = mktdf.rename(columns={'Facebook': f'{x} Facebook', 'Twitter': f'{x} Twitter', 'Pinterest': f'{x} Pinterest',
                            'Instagram': f'{x} Instagram', 'YouTube': f'{x} YouTube', 'Tumblr': f'{x} Tumblr',
                            'StumbleUpon': f'{x} StumbleUpon', 'reddit': f'{x} reddit', 'Google+': f'{x} Google+',
                            'LinkedIn': f'{x} LinkedIn', 'VKontakte': f'{x} VKontakte', 'orkut': f'{x} orkut',
                            'Digg': f'{x} Digg', 'news.ycombinator.com': f'{x} news.ycombinator.com',
                            'Other': f'{x} Other', 'Delicious': f'{x} Delicious', 'NowPublic': f'{x} NowPublic',
                            'MySpace': f'{x} MySpace', 'Fark': f'{x} Fark', 'Vimeo': f'{x} Vimeo',
                            'Odnoklassniki': f'{x} Odnoklassniki', 'iWiW': f'{x} iWiW', 'Bebo': f'{x} Bebo',
                            'FriendFeed': f'{x} FriendFeed', 'Yahoo! Buzz': f'{x} Yahoo! Buzz', 'Netlog': f'{x} Netlog',
                            'Renren': f'{x} Renren', 'Sina Weibo': f'{x} Sina Weibo', 'Hi5': f'{x} Hi5',
                            'Kaboodle': f'{x} Kaboodle', 'Mixx': f'{x} Mixx', 'Newsvine': f'{x} Newsvine',
                            'Youku': f'{x} Youku', 'Tuenti': f'{x} Tuenti', 'Hyves': f'{x} Hyves',
                            })
    mdf = mdf.merge(mktdf, how='inner', on="Date")

mdf = mdf.drop(index=[180])
print(mdf)
mdf.to_csv("C:\PycharmProjects\project\mkt.csv", index=False, header=True)
