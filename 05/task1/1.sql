/**
 * Пусть в таблице users поля created_at и updated_at оказались незаполненными. заполните их текущими датой и временем.
 */
 
use vk;

update users set created_at = now(), updated_at = now();

/* проверяем */
select firstname, created_at, updated_at from users limit 10;