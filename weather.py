from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus

import requests


auth_encode_key = '3ugM3AN5WOzmGr%2BFfJkNxTYJXs2rzsoN2WNDj0790pT8hHCq9SPR3AKQm%2BsfRdZLu%2BlqwEwOKP%2BJlZ%2BGcnA4Aw%3D%3D'
auth_decode_key = '3ugM3AN5WOzmGr+FfJkNxTYJXs2rzsoN2WNDj0790pT8hHCq9SPR3AKQm+sfRdZLu+lqwEwOKP+JlZ+GcnA4Aw=='


url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : auth_encode_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('base_date') : '20210522', quote_plus('base_time') : '0600', quote_plus('nx') : '1', quote_plus('ny') : '1'})

print('queryParams: ', queryParams)

response = requests.get(url + unquote(queryParams))

print('response :', response.url)

result_data = response.json()

print('result_data :', result_data)




#json으로 받아올 경우
# print(result_data['response']['body']['items']['item'][0]['maxTa'])



