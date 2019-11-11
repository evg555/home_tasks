/* Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, 
* catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы, 
* идентификатор первичного ключа и содержимое поля name.
* (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.
*/

drop table if exists logs;
create table logs (
	table_name varchar(150),
	row_id bigint unsigned,
	row_name varchar(150),
	created_at datetime default now()
) ENGINE=ARCHIVE;