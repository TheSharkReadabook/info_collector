# 기상청_동네예보 조회서비스

import urllib.request
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
from keys import *

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : auth_encode_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('base_date') : '20151201', quote_plus('base_time') : '0600', quote_plus('nx') : '18', quote_plus('ny') : '1' })

response = requests.get(url + unquote(queryParams))

print(response.url)

print(response.text)

