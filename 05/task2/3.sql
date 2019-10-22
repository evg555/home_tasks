/*
 * (по желанию) Подсчитайте произведение чисел в столбце таблицы
 **/

select round(exp(sum(log(value)))) as multi from test;