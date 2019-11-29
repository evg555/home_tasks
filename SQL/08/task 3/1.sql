/*
 * Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
 * с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
 */

delimiter //
create procedure hello ()
begin
	set @current_time = now();

	if (@current_time between date_format(@current_time, "%Y-%m-%d 06:00") and date_format(@current_time, "%Y-%m-%d 12:00")) then
		select "Доброе утро";
	elseif (@current_time between date_format(@current_time, "%Y-%m-%d 12:00") and date_format(@current_time, "%Y-%m-%d 18:00")) then
		select "Добрый день";
	elseif (@current_time between date_format(@current_time, "%Y-%m-%d 18:00") and date_format(@current_time, "%Y-%m-%d 00:00")) then
		select "Добрый вечер";
	else 
		select "Доброй ночи";
	end if;
end//