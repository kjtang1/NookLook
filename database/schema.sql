CREATE TABLE villager (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    personality VARCHAR(50),
    species VARCHAR(50),
    birthday VARCHAR(20)
    catchphrase VARCHAR(100),
    icon_uri VARCHAR(100),
    image_uri VARCHAR(100),
);