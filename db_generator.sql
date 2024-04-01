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

INSERT INTO user (name, lastname, email, password) VALUES ('Jhon', 'Doe', 'jhonny@yahoo.fr', 'root');

INSERT INTO transaction (user_id, name, description, amount, category_id, type, date) VALUES 
(1, 'McDonalds', 'Bought a Big Mac', -5.99, 1, 0, '2021-01-01 12:00:00'),
(1, 'Doctor', 'Medical consultation', -50.00, 2, 0, '2021-01-02 12:00:00'),
(1, 'Cinema', 'Watched a movie', -10.00, 3, 0, '2021-01-03 12:00:00'),
(1, 'Gasoline', 'Filled the tank', -40.00, 4, 0, '2021-01-04 12:00:00'),
(1, 'Hotel', 'Stayed at a hotel', -100.00, 5, 0, '2021-01-05 12:00:00'),
(1, 'IRS', 'Paid taxes', -187.00, 6, 0, '2021-01-06 12:00:00'),
(1, 'Bread', 'Bought bread', -1.00, 7, 0, '2021-01-07 12:00:00'),
(1, 'Salary', 'Received salary', 1000.00, 7, 1, '2021-01-08 12:00:00');

ALTER TABLE user
ADD is_overdraft BOOLEAN DEFAULT 0;

ALTER TABLE user
CHANGE is_overdraft overdraft INT DEFAULT 0;

UPDATE category SET name = 'Food' WHERE id = 1;
UPDATE category SET name = 'Health' WHERE id = 2;
UPDATE category SET name = 'Leisure' WHERE id = 3;
UPDATE category SET name = 'Transport' WHERE id = 4;
UPDATE category SET name = 'Lodging' WHERE id = 5;
UPDATE category SET name = 'Tax' WHERE id = 6;
UPDATE category SET name = 'Daily expenses' WHERE id = 7;

INSERT INTO category (name) VALUES ('Salary');
INSERT INTO category (name) VALUES ('Other');