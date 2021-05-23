<h1>summary</h1>
Data들을 Scrapping 하거나 API로 불러와서 Database에 저장하는 프로그램
각 

scrapping.py 
 - news.google.com에서 헤드라인을 Scrapping 하여 Database에 저장

index.py
 - 프로그램 시작점
 
kakaotalk.py
 - 나에게 보내기 기능(다른 프로젝트로 이동 예정)
 
db.py
 - scrapping.py에서 정보를 전달 받아 database에 insert
 - 각 *.py에서 데이터들을 받아서 database에 insert하는 기능 추가 예정
 
mysql-query.sql
 - database query문

corona19.py
 - 코로나19 관련 정보

weather.py
 - 날씨 정보

keys.py
 - API 사용을 위한 Key값들 저장


<h3>개발 일지</h3>

2021-05-03
mail system은 보류
스크래핑해서 db에 저장하기
mysql 설치 및 db 연결까지 끝냄

다음 작업:
스크래핑 정보를 db에 insert 하기 
python to Database connect success
캡슐화 작업 하기

2021-05-04
index에서 db로 스크래핑 데이터 전송 작업 하기 - ok

2021-05-05
email 대신 kakaotalk으로 대체함
카카오톡으로 나에게 보내기 만들기
error: {'msg': 'this user does not have any scope.', 'code': -402} 해결 중
error 해결 핸드폰 받으면 카톡 왔는지 확인하기 현재 시각 2021-05-05 23:25 - ok
error 카카오톡 개발자 페이지에서 계정 로그인활성화 해야 됨
 
2021-05-06
스크래핑 항목 카카오톡 나에게 보내기 - ok
스크래핑 데이터들 보내기 

2021-05-07
pandas로 전달하는데 0번째 요소 값만 전달됨 - 해결 to_json() 쓰면 됨

2021-05-21
공공데이터에서 코로나 정보 api 사용
데이터 불러와서 db에 저정하는 작업 중
sample data 는 잘 불러왔음

에러 해결 중
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) 
- .json() 대신 .text로 함

2021-05-22
SERVICE_ACCESS_DENIED_ERROR
- key 재발급 함
- 요청 URL이 잘못 됐었음

beautifulsoup으로 parsing
- OK

weather.py에서 날씨 데이터 불러오는 중
- ok
json으로 불러온 데이터 정리 해야 함
- ok


2021-05-23
dust.py SERVICE_KEY_IS_NOT_REGISTERED_ERROR 에러
News 세분화 해서 내용까지 요약해서 저장

weather, corona 필요한 정보 불러와서 database에 저장하기

참고 자료 

[공공데이터(XML, JSON)을 python으로 불러오기_기초]
https://han-py.tistory.com/233

[kakao developers error codes]
https://developers.kakao.com/docs/latest/ko/reference/rest-api-reference#error-code
https://stackoverflow.com/questions/51770485/typeerror-object-of-type-dataframe-is-not-json-serializable

[TypeError: the JSON object must be str, bytes or bytearray, not dict]
https://stackoverflow.com/questions/42354001/python-json-object-must-be-str-bytes-or-bytearray-not-dict

 