import keys as key
import requests
# import json
import numpy as np


def news():
    news_data = list()

    url = 'https://newsapi.org/v2/top-headlines?country=kr&apiKey='

    response = requests.get(url + key.newsapi_key)

    json_data = response.json()

    # print(json.dumps(json_data, indent="\t"))

    for datas in json_data['articles']:
        news_data.append(datas['title'])
        news_data.append(datas['url'])

    news_data = np.array(news_data).reshape(int(len(news_data) / 2), 2)

    return news_data
