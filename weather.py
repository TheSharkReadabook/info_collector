# 기상청_동네예보 조회서비스

# import urllib.request
# from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
# import json

import keys as key


# 초단기실황조회
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
queryParams = '?' + urlencode({quote_plus('ServiceKey'): key.auth_encode_key,
                               quote_plus('pageNo'): '1',
                               quote_plus('numOfRows'): '10',
                               quote_plus('dataType'): 'JSON',
                               quote_plus('base_date'): '20210523',
                               quote_plus('base_time'): '0500',
                               quote_plus('nx'): '56',
                               quote_plus('ny'): '131'})

response = requests.get(url + unquote(queryParams))

json_data = response.json().get('response').get('body').get('items')

# print(json_data)

# json_data = json.loads(json.dumps(response.json()))

for weat_datas in json_data['item']:
    print(weat_datas['baseDate'])
    print(weat_datas['baseTime'])
    print(weat_datas['category'])
    print(weat_datas['fcstDate'])
    print(weat_datas['fcstTime'])
    print(weat_datas['fcstValue'])
    print(weat_datas['nx'])
    print(weat_datas['ny'])
    print('=========================')
