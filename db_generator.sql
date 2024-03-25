CREATE DATABASE IF NOT EXISTS budget;

USE budget;

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    lastname VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255),
    description TEXT,
    amount FLOAT,
    category_id INT,
    type BOOLEAN,
    date DATETIME,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO category (name) VALUES ('Food');
INSERT INTO category (name) VALUES ('Health');
INSERT INTO category (name) VALUES ('Leisure');
INSERT INTO category (name) VALUES ('Vehicles');
INSERT INTO category (name) VALUES ('Lodging');
INSERT INTO category (name) VALUES ('Taxes');
INSERT INTO category (name) VALUES ('Daily');
