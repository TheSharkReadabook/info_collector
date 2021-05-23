# 공공데이터활용지원센터_보건복지부 코로나19 감염 현황

from urllib.parse import urlencode, unquote, quote_plus
from bs4 import BeautifulSoup
import requests
import keys as key

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
queryParams = '?' + urlencode({quote_plus('ServiceKey'): key.auth_encode_key,
                               quote_plus('pageNo'): '1',
                               quote_plus('numOfRows'): '10',
                               quote_plus('dataType'): 'XML',
                               quote_plus('dataCd'): 'ASOS',
                               quote_plus('dateCd'): 'DAY',
                               quote_plus('startDt'): '20200310',
                               quote_plus('endDt'): '20200315',
                               quote_plus('stnIds'): '108'})


response = requests.get(url + unquote(queryParams))

soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find_all('item')

print(data)

for item in data:
    createDt = item.find('createdt')
    decideCnt = item.find('decidecnt')

print('기준일: '+createDt.text+' 확진자 수: '+decideCnt.text)

