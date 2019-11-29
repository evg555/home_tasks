/* Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, 
* catalogs и products в таблицу logs помещается время и дата создания записи, название таблицы, 
* идентификатор первичного ключа и содержимое поля name.
* (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.
*/

drop table if exists logs;
create table logs (
	`table` varchar(150),
	row_id bigint unsigned,
	name varchar(150),
	created_at datetime default current_timestamp
) engine=Archive;


delimiter //

create trigger insert_from_users after insert on users for each row
begin
	insert into logs values ('users', new.id, new.name, now());
end//

create trigger insert_from_catalogs after insert on catalogs for each row
begin
	insert into logs values ('catalogs', new.id, new.name, now());
end//

create trigger insert_from_products after insert on products for each row
begin
	insert into logs values ('products', new.id, new.name, now());
end//

delimiter ;