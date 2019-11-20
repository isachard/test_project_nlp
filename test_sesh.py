# IPython log file

import requests
import time
import pandas as pd
import ast



url = 'https://www.reddit.com/hot.json'
header = {'User-agent': 'Bleep blorp bot 0.1'}
res = requests.get(url,headers=header)
the_json = res.json()
print(sorted(the_json.keys()))

def get_posts(url,interations,header,sleep):
    posts = []
    after = None
    for i in range(interations):
#         print(i)
        if after==None:
            params = {}
        else:
            params = {'after' : after}
        res = requests.get(url,params=params,headers=header)
        if res.status_code == 200:
            the_json = res.json()
            posts.extend(the_json['data']['children'])
            after = the_json['data']['after']
        else:
            print(res.status_code)
            break
        time.sleep(sleep)
    return posts

def create_cols(dataframe):
    dataframe['subreddit'] = dataframe['data'].map(lambda x: x['subreddit'])
    dataframe['title'] = dataframe['data'].map(lambda x: x['title'])
    dataframe['name'] = dataframe['data'].map(lambda x: x['name'])
    dataframe['selftext'] = dataframe['data'].map(lambda x: x['selftext'])
    dataframe['domain'] = dataframe['data'].map(lambda x: x['domain'])
    return dataframe\

def create_cols(dataframe):
    dataframe['subreddit'] = dataframe['data'].map(lambda x: x['subreddit'])
    dataframe['title'] = dataframe['data'].map(lambda x: x['title'])
    dataframe['name'] = dataframe['data'].map(lambda x: x['name'])
    dataframe['selftext'] = dataframe['data'].map(lambda x: x['selftext'])
    dataframe['domain'] = dataframe['data'].map(lambda x: x['domain'])
    return dataframe

header = {'User-agent': 'Bleep blorp bot 0.1'}
url = 'https://www.reddit.com/r/puppet/.json'
interations = 250
sleep_sec = 1.5
puppet_df = pd.DataFrame(get_posts(url,interations,header,sleep_sec))
puppet_df = create_cols(puppet_df)
