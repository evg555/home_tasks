/*
 * В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию. * 
*/

delimiter //
create trigger check_null_fields_update before update on products
for each row
begin
	if (new.name is null and new.description is null) then
		set new.name = old.name;
		set new.description = old.description;
	end if;	
end//

create trigger check_null_fields_insert before insert on products
for each row
begin
	if (new.name is null and new.description is null) then
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insert failed (all required fields are empty)';
	end if;	
end//