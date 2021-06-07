import keys as key
import requests
from gensim.summarization.summarizer import summarize
from newspaper import Article
import numpy as np
# import json


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
        url = datas['url']
        # newspaper로 크롤링
        news = Article(url, language='ko')
        news.download()
        news.parse()
        try:
            news_data.append(summarize(news.text))
        except:
            news_data.append("none content")
        news_data.append(news.publish_date)

    news_data = np.array(news_data).reshape(int(len(news_data) / 6), 6)

    return news_data
