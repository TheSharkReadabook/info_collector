<h1>summary</h1>
더 나은 프로그램 만들기 위한 toyPoject

정보를 스크래핑 하여 카카오톡 나에게 전송하기

scrapping.py 
스크랩핑 항목
 - 뉴스 헤드라인
 - 오늘의 날씨예보 
 - 기타 등등

index.py
 - 프로그램 시작점
 
kakaotalk.py
 - 나에게 보내기 기능
 
db.py
 - scrapping.py에서 정보를 전달 받아 database에 insert
 
mysql-query.sql
 - 스크래핑 정보 저장할 database query문
 
순서

1. 웹에서 필요한 정보를 스크래핑하여 DATABASE에 저장한다.
 
2. DATABASE에 있는 정보를 'TOdays' 라는 웹 페이지에 불러온다.
 - WebApp 개발 해야 함. -- 다음 프로젝트에서 진행
 
3. DATABASE에 있는 최신 정보를 카카오톡으로 전송한다.


<h3>개발 일지</h3>

2021-05-03
mail system은 보류
스크래핑해서 db에 저장하기
mysql 설치 및 db 연결까지 끝냄

다음 작업:
스크래핑 정보를 db에 insert 하기 
- python to Database connect success
- 캡슐화 작업 하기

2021-05-04
 - index에서 db로 스크래핑 데이터 전송 작업 하기 - ok

2021-05-05
 - email 대신 kakaotalk으로 대체함
 - 카카오톡으로 나에게 보내기 만들기
 - error: {'msg': 'this user does not have any scope.', 'code': -402} 해결 중
 - error 해결 핸드폰 받으면 카톡 왔는지 확인하기 현재 시각 2021-05-05 23:25 - ok
 -- error 카카오톡 개발자 페이지에서 계정 로그인활성화 해야 됨
 
2021-05-06
- 스크래핑 항목 카카오톡 나에게 보내기 - ok
- 스크래핑 데이터들 보내기 

2021-05-07
-- pandas로 전달하는데 0번째 요소 값만 전달됨 - 해결 to_json() 쓰면 됨


참고 자료 
kakao developers error codes
 https://developers.kakao.com/docs/latest/ko/reference/rest-api-reference#error-code
 
 https://stackoverflow.com/questions/51770485/typeerror-object-of-type-dataframe-is-not-json-serializable
 
 

 