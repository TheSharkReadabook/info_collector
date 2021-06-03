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
        news_data.append(datas['description'])
        news_data.append(datas['url'])
        news_data.append(datas['urlToImage'])

    # 20행 4열의 2차원 배열로 변환
    news_data = np.array(news_data).reshape(int(len(news_data) / 4), 4)

    return news_data
