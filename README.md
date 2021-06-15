<h1>summary</h1>

출퇴근 시간 등에 필요한 정보(뉴스 등)를 빠르고 쉽게 알 수 있게 한다
1. 카카오톡으로 정보 전송
2. 웹 페이지에 불러와서 다시 볼 수 있음

info_collector
Data들을 Scrapping 하거나 API로 불러와서 Database에 저장하는 프로그램

webapp/infoweb
info_collector에서 Database에 Insert한 정보를 Web에 보기 좋게 불러옴

kkot
Database에서 Data를 불러와서 Kakaotalk 메신저로 보냄

AWS, GCP, Docker, Kubernetes에서 운영 예정

<h3>./info_collector</h3>
index.py
 - 프로그램 시작
 
database.py
 - 각 *.py에서 데이터들을 받아서 database에 insert
 
mysql-query.sql
 - database query문

corona19.py
 - 코로나19 관련 정보

weather.py
 - 날씨 정보

keys.py
 - API 사용을 위한 Key값들 저장 git에 push 하지 않음
 
air.py
 - 대기정보
 
news.py
 - 뉴스 헤드라인
 
<h3>./kkot</h3>
database에 Select 해서 카카오톡으로 전송
 
<h3>./webapp</h3>
server 실행 코드 0.0.0.0은 외부접속 허용 python manage.py runserver 0.0.0.0:80

 
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
index에서 db로 스크래핑 데이터 전송 작업 하기 
- ok

2021-05-05
email 대신 kakaotalk으로 대체함
카카오톡으로 나에게 보내기 만들기
error: {'msg': 'this user does not have any scope.', 'code': -402} 해결 중
error 해결 핸드폰 받으면 카톡 왔는지 확인하기 현재 시각 2021-05-05 23:25 - ok
error 카카오톡 개발자 페이지에서 계정 로그인활성화 해야 됨
 
2021-05-06
스크래핑 항목 카카오톡 나에게 보내기 
- ok
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
weather, corona 필요한 정보 불러와서 database에 저장하기
- ok
weather data -> database 작업 중
- ok 

2021-05-28
dust.py SERVICE_KEY_IS_NOT_REGISTERED_ERROR 에러
- ok
dust.py -> air_condition.py로 변경
air_condition.py 데이터 정리에서 db에 저장하기
- ok

2021-05-29
air_condition.py -> air.py로 변경
air.py '서대문구', pm25 데이터가 공백임. insert할 떄 Error 발생 -> string으로 처리
Headline News 가져와서 DataBase에 저장
- ok

2021-05-30
weather.py에 날자 자동으로 변경해야됨 
- ok
kkot 만듬(프로젝트 합침)
- ok

django project만듬 mysql에 있는 데이터 news.html로 불러오는 중
emplateDoesNotExist 에러 발생
- ok


2021-05-31
api data들 django에 불러옴
디자인만 하면 됨

MYSQL news TABLE description Column Type changed to TEXT and NULL -> YES 

No module named ‘gensim.summarization’
https://discuss.streamlit.io/t/no-module-named-gensim-summarization/11780/1
- gensim 3.8.3으로 설치함

2021-06-03
news.py는 newspaper 모듈로 내용 scrap해서 gensim으로 요약하고 return
- ok

web design은 bootstrap등을 활용해서 디자인 시간 최소화 하기
kakao oven에 디자인 프로토타입 만듬

2021-06-04
index.html
news.title, news.content 불러옴

news에 날짜도 올리기
- ok

weather, air 오늘 날짜만 올라오도록 함
- ok

데이터들은 최근 24시간 내 데이터만 올리도록 하고 중복 되지 않게 하기
- ok


2021-06-06
fcstvalue 확인하여 띄어줘야 함

corona19 일일 확진자는 (오늘 확진자 수 - 어제 확진자 수)
API에서 불러와서 계산하여 Insert

Mysql 오래된 데이터 자동 삭제하기
- 테이블별로 crontab 하기

2021-06-07
코로나 일일 확진자랑 fcstvalue 해결 하기

매일 데이터 갱신 리눅스에서 contab으로 자동화 하기

지역별로 weather, air 데이터 어떻게 할건지 생각

[commit 메시지]
https://blog.ull.im/engineering/2019/03/10/logs-on-git.html

2021-06-15
gcp vm instence에 배포해보기

gcp GKE, SQL 등 사용해서 배포해보기

정보들을 메일로 보내는 기능

웹에 챗봇 기능 구현을 위한 Subproject - 실시간 채팅 channels 
https://victorydntmd.tistory.com/261

======================================================
[refactoring]

SQL문 NOT NULL로 수정하고 NONE(NULL) 데이터는 Try - except 예외처리하기

======================================================
참고 자료
[mysql 오래된 데이터 삭제]
https://ileeyj.tistory.com/194
- weather 테이블의 경우 DELETE FROM weather WHERE baseDate < date_add(date_format( now() , '%Y-%m-%d'), interval -30 day);

[공공데이터(XML, JSON)을 python으로 불러오기_기초]
https://han-py.tistory.com/233

[kakao developers error codes]
https://developers.kakao.com/docs/latest/ko/reference/rest-api-reference#error-code
https://stackoverflow.com/questions/51770485/typeerror-object-of-type-dataframe-is-not-json-serializable

[TypeError: the JSON object must be str, bytes or bytearray, not dict]
https://stackoverflow.com/questions/42354001/python-json-object-must-be-str-bytes-or-bytearray-not-dict

[python double quotes insert sql]
https://stackoverflow.com/questions/16370197/inserting-double-quotes-into-mysql-db

[change git repository]
https://gist.github.com/480/4681b67d2a906db8c6c1321cc678f05f

[소프트웨어 설계 - 공동 모듈 설계]
https://velog.io/@kjh03160/1-%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4-%EC%84%A4%EA%B3%84-3.-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%84%A4%EA%B3%84-1-%EA%B3%B5%ED%86%B5-%EB%AA%A8%EB%93%88-%EC%84%A4%EA%B3%84
