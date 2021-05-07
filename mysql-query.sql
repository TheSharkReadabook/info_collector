CREATE TABLE `news_headlines` (
    `id` INT(22) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `date_time` TIMESTAMP DEFAULT NOW()
);

