/*
* 2. Создайте базу данных example, разместите в ней таблицу users, состоящую из двух столбцов, 
* числового id и строкового name.
*/

CREATE DATABASE IF NOT EXISTS example;
USE example;

CREATE TABLE users (
	id INT,
	name VARCHAR(255)
);