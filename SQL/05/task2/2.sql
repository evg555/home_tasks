/*
 * Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
 * следует учесть, что необходимы дни недели текущего года, а не года рождения.
 */

select dayofweek(concat(year(now()), date_format(birthday,  '-%c-%d'))) as weekday, count(*) as total from users group by weekday order by weekday asc;