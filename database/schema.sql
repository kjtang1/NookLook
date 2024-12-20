DROP TABLE IF EXISTS villager;

CREATE TABLE villager (
    id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    personality VARCHAR(50),
    species VARCHAR(50),
    birthday_month VARCHAR(20),
    birthday_day VARCHAR(5),
    catchphrase VARCHAR(100),
    image_url VARCHAR(100)
);