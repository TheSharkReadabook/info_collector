CREATE TABLE `news` (
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `description` VARCHAR(256) NOT NULL,
    `url` VARCHAR(256) NOT NULL,
    `urlToImage` VARCHAR(256) NOT NULL
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
    `baseDate` DATE NOT NULL,  # 발표일자
    `baseTime` TIME NOT NULL,  # 발표시각
    `category` CHAR(4) NOT NULL,  # 자료구분코드
    `fcstDate` DATE NOT NULL,  # 예보일자
    `fcstTime` TIME NOT NULL,  # 예보시각
    `fcstValue` CHAR(3) NOT NULL,  # 예보 값
    `nx` INT(3) NOT NULL,  # 예보지점 X 좌표
    `ny` INT(3) NOT NULL  # 예보지점 Y 좌표
);

CREATE TABLE `air`(
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cityName` VARCHAR(255) NOT NULL,  # 시군구
    `cityNameEng` VARCHAR(255) NOT NULL,  # 시군구 영어이름
    `dataTime` TIMESTAMP NOT NULL,  # 측정일시
    `so2Value` VARCHAR(10) NOT NULL,  # 아황산가스 평균농도
    `coValue` VARCHAR(10) NOT NULL,  # 일산화탄소 평균농도
    `o3Value` VARCHAR(10) NOT NULL,  # 오존 평균농도
    `no2Value` VARCHAR(10) NOT NULL,  # 이산화질소 평균농도
    `pm10Value` VARCHAR(10) NOT NULL,  # 미세먼지(pm10) 평균농도
    `pm25Value` VARCHAR(10) NOT NULL  # 초미세먼지(pm2.5) 평균농도
);
    
INSERT INTO `corona19`(`createdt`, `statedt`, `statetime`, `decidecnt`, `carecnt`, `clearcnt`, `deathcnt`, `examCnt`, `resutlnegcnt`, `accdefrate`, `accExamCnt`, `accExamCompCnt`) 
VALUES ("2021-05-23 09:37:54.099", "20210523", "00:00", '135929', '8117', '125881', '1931', '122235', '9278135', '1.4438928819', '9536299', '9414064')
VALUES ("2021-05-23 09:37:54.099", "20210523", "00:00", 135929, 8117, 125881, 1931, 122235, 9278135, 1.4438928819, 9536299, 9414064)


INSERT INTO `weather` (`baseDate`, `baseTime`, `category`, `fcstDate`, `fcstTime`, `fcstValue`, `nx`, `ny`) VALUES ('20210522', '0500', 'POP', '20210528', '1200', '60', 56, 131)

INSERT INTO `air` (`cityName`, `cityNameEng`, `dataTime`, `so2Value`, `coValue`, `o3Value`, `no2Value`, `pm10Value`, `pm25Value`) VALUES ('강남구', 'Gangnam-gu', '2021-05-29 15:00', 0.003, 0.3, 0.042, 0.014, 20, 7)

INSERT INTO `news` (`title`, `url`) VALUES ('TEST', 'TEST')