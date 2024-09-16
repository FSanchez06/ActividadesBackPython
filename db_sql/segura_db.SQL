CREATE DATABASE IF NOT EXISTS segura_bd;

USE segura_bd;

CREATE TABLE USUARIOS (
    usuario VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

INSERT INTO USUARIOS (usuario, password) VALUES 
('user1', 'pass1'),
('user2', 'pass2'),
('user3', 'pass3'),
('user4', 'pass4'),
('user5', 'pass5');
