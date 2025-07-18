-- Creates db and table with primary and foreign key colunms
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    UNIQUE(id),
    FOREIGN KEY(state_id) REFERENCES states(id)
)