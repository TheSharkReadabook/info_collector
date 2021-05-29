from urllib.parse import urlencode, unquote, quote_plus
import requests
import keys as key
import numpy as np

# 시군구별 실시간 평균정보 조회


def air():
    air_data = list()

    url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'

    queryParams = '?' + urlencode({quote_plus('ServiceKey'): key.auth_encode_key,
                                   quote_plus('returnType'): 'JSON',
                                   quote_plus('numOfRows'): '100',
                                   quote_plus('pageNo'): '1',
                                   quote_plus('sidoName'): '서울',
                                   quote_plus('searchCondition'): 'HOUR'})

    response = requests.get(url + unquote(queryParams))

    json_data = response.json().get('response').get('body')

    print(json_data)

    for datas in json_data['items']:
        air_data.append(datas['cityName'])
        air_data.append(datas['cityNameEng'])
        air_data.append(datas['dataTime'])
        air_data.append(datas['so2Value'])
        air_data.append(datas['coValue'])
        air_data.append(datas['o3Value'])
        air_data.append(datas['no2Value'])
        air_data.append(datas['pm10Value'])
        air_data.append(datas['pm25Value'])

    air_data = np.array(air_data).reshape(-1, 9)

    return air_data
