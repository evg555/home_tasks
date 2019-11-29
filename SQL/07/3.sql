/*(по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
* Поля from, to и label содержат английские названия городов, поле name — русское. 
* Выведите список рейсов flights с русскими названиями городов.
*/

select id, 
(select name from cities where label = `from`) as 'from',
(select name from cities where label = `to`) as 'to'
from flights