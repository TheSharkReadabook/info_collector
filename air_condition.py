from urllib.parse import urlencode, unquote, quote_plus
import requests
import keys as key

url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'
queryParams = '?' + urlencode({quote_plus('ServiceKey'): key.auth_encode_key,
                               quote_plus('returnType'): 'JSON',
                               quote_plus('numOfRows'): '100',
                               quote_plus('pageNo'): '1',
                               quote_plus('sidoName'): '서울',
                               quote_plus('searchCondition'): 'DAILY'})

response = requests.get(url + unquote(queryParams))

print(response.url)
print(response.content)

json_data = response.json().get('response').get('body').get('items')

print(json_data)
