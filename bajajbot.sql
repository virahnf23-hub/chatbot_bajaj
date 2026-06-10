CREATE DATABASE IF NOT EXISTS bajajbot;

USE bajajbot;

CREATE TABLE admin(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(100)
);

INSERT INTO admin(username,password)
VALUES('admin','admin123');


CREATE TABLE chat_history(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_message TEXT,
    bot_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE booking(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    no_hp VARCHAR(20),
    motor VARCHAR(100),
    tanggal DATE,
    keluhan TEXT
);


CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100),
    harga VARCHAR(50)
);


INSERT INTO products(nama,harga)
VALUES
('Bajaj Pulsar N160','Rp 31.000.000'),
('Bajaj Pulsar NS200','Rp 37.000.000');