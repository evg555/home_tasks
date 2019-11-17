/* Обновление счета пользователя после совершения транзакции */
delimiter //

create trigger account_update after insert on `transaction` 
for each row
begin
	if (new.debit = 1) then
		update accounts set total = total + new.total where id = new.account_id;
	else
		update accounts set total = total - new.total where id = new.account_id;
	end if;
end//

delimiter ;