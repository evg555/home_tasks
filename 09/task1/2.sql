/* (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей. */

delimiter //

create procedure insert_rows (in i_max int)
begin
	declare i int unsigned default 1;

	while i < i_max do
	    insert into users values (null, 'Георгий','1990-10-08', now(), now());
	    set i = i + 1;
    end while;	
end//

delimiter ;

call insert_rows(1000000);