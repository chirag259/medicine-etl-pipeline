CREATE DATABASE IF NOT EXISTS pharma_dw;
USE pharma_dw;

CREATE TABLE IF NOT EXISTS sponsor (
    sponsor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS study (
    study_id VARCHAR(50) PRIMARY KEY,
    title TEXT,
    status VARCHAR(50),
    phase VARCHAR(50),
    start_date DATE,
    sponsor_id INT,
    FOREIGN KEY (sponsor_id) REFERENCES sponsor(sponsor_id)
);
