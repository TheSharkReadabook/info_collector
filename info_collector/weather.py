# 기상청_동네예보 조회서비스

from urllib.parse import urlencode, unquote, quote_plus
import requests
import numpy as np
from datetime import datetime
from pytz import timezone


import keys as key


def weather():
    weather_data = list()
    base_data = datetime.now(timezone('Asia/Seoul')).strftime('%Y%m%d')
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
    queryParams = '?' + urlencode({quote_plus('ServiceKey'): key.auth_encode_key,
                                   quote_plus('pageNo'): '1',
                                   quote_plus('numOfRows'): '10',
                                   quote_plus('dataType'): 'JSON',
                                   quote_plus('base_date'): base_data,
                                   quote_plus('base_time'): '0500',
                                   quote_plus('nx'): '56',
                                   quote_plus('ny'): '131'})

    response = requests.get(url + unquote(queryParams))

    json_data = response.json().get('response').get('body').get('items')

    # for weat_datas in json_data['item']:
    #     print(weat_datas['baseDate'])  # 발표일자
    #     print(weat_datas['baseTime'])  # 발표시각
    #     print(weat_datas['category'])  # 자료구분코드
    #     print(weat_datas['fcstDate'])  # 예보일자
    #     print(weat_datas['fcstTime'])  # 예보시각
    #     print(weat_datas['fcstValue'])  # 예보 값
    #     print(weat_datas['nx'])  # 예보지점 X 좌표
    #     print(weat_datas['ny'])  # 예보지점 Y 좌표
    #     print('=========================')  # 구분선

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

    return weather_data
