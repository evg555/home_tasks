/*
* 3. Создайте дамп базы данных example из предыдущего задания, 
* разверните содержимое дампа в новую базу данных sample.
*/

/* Предварительно поместить дамп example.sql в папку, откуда будет запускаться команда,
* либо создать базу данных sample и выполнить в командной строке
* mysql -u root -p sample < example.sql
-*/


CREATE DATABASE IF NOT EXISTS sample;
USE sample;

SOURCE example.sql;