CREATE TABLE `news_headlines` (
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `date_time` TIMESTAMP DEFAULT NOW()
);

 CREATE TABLE `corona19` (
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `createdt` TIMESTAMP,  #  등록일시분초
    `statedt` DATE,  # 기준일
    `statetime` TIME,  # 기준 시간
    `decidecnt` INT(16),  # 확진자 수
    `carecnt` INT(16),  # 치료중 환자 수
    `clearcnt` INT(16),  # 격리 해제 수
    `deathcnt` INT(16),  # 사망자 수
    `examCnt` INT(16),  # 검사 진행 수
    `resutlnegcnt`INT(16),  # 결과 음성 수
    `accdefrate`INT(31),  # 누적 확진률
    `accExamCnt` INT(16),  # 누적 검사 수
    `accExamCompCnt` INT(16)  # 누적 검사 완료 수
 );

CREATE TABLE `weather`(
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `baseDate` DATE,  # 발표일자
    `baseTime` TIME,  # 발표시각
    `category` CHAR(4),  # 자료구분코드
    `fcstDate` DATE,  # 예보일자
    `fcstTime` TIME,  # 예보시각
    `fcstValue` CHAR(3),  # 예보 값
    `nx` INT(3),  # 예보지점 X 좌표
    `ny` INT(3)  # 예보지점 Y 좌표
);
    
SELECT * FROM `news_headlines` A, (SELECT * FROM `news_headlines`
                                  GROUP BY `title` 
                                   HAVING COUNT(`title`))