# 뉴스 본문을 추출하여 정제한 후 내용 요약하여 list로 return
import re
import keys as key
import requests
from bs4 import BeautifulSoup
from gensim.summarization.summarizer import summarize
from newspaper import Article
# import json

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
    
    print(news.text[:10])
    
    # if url == 'https://www.ytn.co.kr/_ln/0101_202106011551006187':
    #     selector = '#CmAdContent > span'
    #     r = requests.get(url)

    #     if r.status_code == 200:
    #         print('connect success')
    #         html = r.text
    #         soup = BeautifulSoup(html, 'html.parser')
    #         content = soup.select(selector)
    #         content = re.sub('(<([^>]+)>)','',str(content))
    #         print(summarize(content))
            
    #     else:
    #         print('error occured'+r.status_code)
