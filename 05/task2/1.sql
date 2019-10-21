/**
 * Подсчитайте средний возраст пользователей в таблице users
 */

select round(avg(datediff(now(), birthday) / 365.25)) as avg_age from users;