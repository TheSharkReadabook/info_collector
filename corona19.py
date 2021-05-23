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
    createDt = item.find('createdt')  # 등록일시분초
    decideCnt = item.find('decidecnt')  # 확진자 수
    careCnt = item.find('carecnt')  # 치료중 환자 수
    clearCnt = item.find('clearcnt')  # 격리 해제 수
    deathCnt = item.find('deathcnt')  # 사망자 수
    examCnt = item.find('examCnt')  # 검사 진행 수
    resutlNegCnt = item.find('resutlnegcnt')  # 결과 음성 수
    stateDt = item.find('statedt')  # 기준일
    stateTime = item.find('statetime')  # 기준 시간
    accDefRate = item.find('accdefrate')  # 누적 확진률
    accExamCnt = item.find('accExamCnt')  # 누적 검사 수
    accExamCompCnt = item.find('accExamCompCnt')  # 누적 검사 완료 수

print('등록일시분초: '+createDt.text+' 확진자 수: '+decideCnt.text)

