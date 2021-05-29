from urllib.parse import urlencode, unquote, quote_plus
import requests
import keys as key
import numpy as np

# 시군구별 실시간 평균정보 조회

url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'

queryParams = '?' + urlencode({quote_plus('ServiceKey'): key.auth_encode_key,
                               quote_plus('returnType'): 'JSON',
                               quote_plus('numOfRows'): '100',
                               quote_plus('pageNo'): '1',
                               quote_plus('sidoName'): '서울',
                               quote_plus('searchCondition'): 'HOUR'})

response = requests.get(url + unquote(queryParams))

json_data = response.json().get('response').get('body').get('items')

print(json_data)


for weat_datas in json_data['item']:
    weather_data.append(weat_datas['baseDate'])
    weather_data.append(weat_datas['baseTime'])
    weather_data.append(weat_datas['category'])
    weather_data.append(weat_datas['fcstDate'])
    weather_data.append(weat_datas['fcstTime'])
    weather_data.append(weat_datas['fcstValue'])
    weather_data.append(weat_datas['nx'])
    weather_data.append(weat_datas['ny'])

weather_data = np.array(weather_data).reshape(-1, 8)

