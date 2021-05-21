# 공공데이터활용지원센터_보건복지부 코로나19 감염 현황

# https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%EC%9D%BC%EC%9E%90%EB%B3%84+%ED%98%84%ED%99%A9&conditionType=search&org=&orgFilter=&orgFullName=

#https://data.go.kr/iim/api/selectAPIAcountView.do

# 가져올 데이터
# STATE_DT 기준일
# STATE_TIME 기준시간
# DECIDE_CNT 확진자 수
# CLEAR_CNT 격리해제 수
# EXAM_CNT 검사진행 수
# DEATH_CNT 사망자 수
# CARE_CNT 치료중 환자 수

# import urllib.request

auth_encode_key = 'cn%2Bb4YHUt6kHfeUFqhp1bF1IKyn8PshwcLUk%2FDfn3OhWXDImh5j2MLaK5MtkSoERg4%2BTfPZhq%2Fb2j17ak0ko%2Bg%3D%3D'
# auth_decode_key = 'cn+b4YHUt6kHfeUFqhp1bF1IKyn8PshwcLUk/Dfn3OhWXDImh5j2MLaK5MtkSoERg4+TfPZhq/b2j17ak0ko+g=='

# corona_xml_data = urllib.request.urlopen('http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey='+auth_encode_key+'&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315').read().decode('utf-8')


# Python 샘플 코드 #

from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests

# 데이터를 받고자하는 사이트의 포멧에 맞게 url을 수정하고 보내는 코드
url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : auth_encode_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'JSON', quote_plus('dataCd') : 'ASOS', quote_plus('dateCd') : 'DAY', quote_plus('startDt') : '20100101', quote_plus('endDt') : '20100601', quote_plus('stnIds') : '108' })

print('queryParams: ', queryParams)

get_data = requests.get(url + unquote(queryParams))

print('get_data :', get_data)

result_data = get_data.json()

print('result_data :', result_data)

# print(result_data['response']['body']['items']['item'][0]['maxTa'])



