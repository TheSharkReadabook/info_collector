CREATE TABLE `news_headlines` (
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `date_time` TIMESTAMP DEFAULT NOW()
);

 CREATE TABLE `corona19` (
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `createdt` TIMESTAMP NOT NULL,  #  등록일시분초
    `statedt` DATE NOT NULL,  # 기준일
    `statetime` TIME NOT NULL,  # 기준 시간
    `decidecnt` VARCHAR(255) NOT NULL,  # 확진자 수
    `carecnt` VARCHAR(255) NOT NULL,  # 치료중 환자 수
    `clearcnt` VARCHAR(255) NOT NULL,  # 격리 해제 수
    `deathcnt` VARCHAR(255) NOT NULL,  # 사망자 수
    `examCnt` VARCHAR(255) NOT NULL,  # 검사 진행 수
    `resutlnegcnt` VARCHAR(255) NOT NULL,  # 결과 음성 수
    `accdefrate` VARCHAR(255) NOT NULL,  # 누적 확진률
    `accExamCnt` VARCHAR(255) NOT NULL,  # 누적 검사 수
    `accExamCompCnt` VARCHAR(255) NOT NULL  # 누적 검사 완료 수
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
                                   
                                   
INSERT INTO `corona19`(`createdt`, `statedt`, `statetime`, `decidecnt`, `carecnt`, `clearcnt`, `deathcnt`, `examCnt`, `resutlnegcnt`, `accdefrate`, `accExamCnt`, `accExamCompCnt`) 
VALUES ("2021-05-23 09:37:54.099", "20210523", "00:00", '135929', '8117', '125881', '1931', '122235', '9278135', '1.4438928819', '9536299', '9414064')
VALUES ("2021-05-23 09:37:54.099", "20210523", "00:00", 135929, 8117, 125881, 1931, 122235, 9278135, 1.4438928819, 9536299, 9414064)


INSERT INTO `corona19`(`createdt`, `statedt`,                `statetime`, `decidecnt`, `carecnt`, `clearcnt`,                `deathcnt`, `examCnt`, `resutlnegcnt`, `accdefrate`,                 `accExamCnt`, `accExamCompCnt`
)                 VALUES("2021-05-23 09:37:54.099", "20210523", "00:00", 135929, 8117, 125881, 1931, 122235, 9278135, 1.4438928819, 9536299, 9414064)



