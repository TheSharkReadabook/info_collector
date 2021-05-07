카카오톡 나에게 알림
- 알림 종류 : 미세먼지 경보, 뉴스, 주식 등
- database에 저장하여 웹 페이지에도 업로드
- 매일 정보를 알 수 있게함.
- 매일 오전 7시경 자동 전송 또는 사용자가 원하는 시간대로 스케줄링

scrapping.py 
정보 스크랩핑
스크랩핑 항목
 - 뉴스 헤드라인
 - 오늘의 날씨예보
 - [옵션]로또 번호 보내기
 - 금일 상영 영화

index.py
 - 프로그램 시작점
 
kakaotalk.py
 - 나에게 보내기 기능
 
current_time.py
 - 현재 시각 KST 가져와서 전달
 
db.py
 - scrapping.py에서 정보를 전달 받아 database에 insert
 
rules
- git 잘 활용할 것

순서

1. 웹에서 필요한 정보를 스크래핑하여 DATABASE에 저장한다.
 - 스크래핑 날짜는 추후 스케줄링
2. DATABASE에 있는 정보를 'TOdays' 라는 웹 페이지에 불러온다.
 - WebApp 개발 해야 함. -- 2번 보류 완성 후 마지막 즈음에 추가
3. DATABASE에 있는 최신 정보를 카카오톡으로 전송한다.
 - 전송 날자는 사용자가 스케줄링
4. Scrapping 항목이나 기능 등 추가하여 완성
5. refactoring
