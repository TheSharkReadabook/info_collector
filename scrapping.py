from bs4 import BeautifulSoup
import requests


def scrapping():

    selector = '#yDmH0d > c-wiz > div > div.FVeGwb.CVnAc.Haq2Hf.bWfURe > div.ajwQHc.BL5WZb.RELBvb.zLBZs > div > main > c-wiz > div.lBwEZb.BL5WZb.xP6mwf > div > div > div > article > h3 > a'
    headlines = []

    url = 'https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko'
    r = requests.get(url)

    if r.status_code == 200:
        print('connect success')
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select(selector)
        for i in range(len(title)):
            # print(title[i].text.replace(" ", ""))
            headlines.append(title[i].text.replace(" ", ""))
    else:
        print('error occured'+r.status_code)

    print(headlines)

    return headlines
