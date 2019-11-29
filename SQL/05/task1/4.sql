/*
 * по желанию) »з таблицы users необходимо извлечь пользователей, родившихс¤ в августе и мае. 
 * ћес¤цы заданы в виде списка английских названий ('may', 'august')
 */

use vk;

/* подготовка тестовой среды

update users set birthday = null;
alter table users change birthday birthday varchar(50);

update users set birthday = concat(FLOOR(1 + (RAND() * 30)), ' ', case
	when FLOOR(1 + (RAND() * 11)) = 1 then 'january'
	when FLOOR(1 + (RAND() * 11)) = 2 then 'february'
	when FLOOR(1 + (RAND() * 11)) = 3 then 'march'
	when FLOOR(1 + (RAND() * 11)) = 4 then 'april'
	when FLOOR(1 + (RAND() * 11)) = 5 then 'may'
	when FLOOR(1 + (RAND() * 11)) = 6 then 'june'
	when FLOOR(1 + (RAND() * 11)) = 7 then 'july'
	when FLOOR(1 + (RAND() * 11)) = 8 then 'august'
	when FLOOR(1 + (RAND() * 11)) = 9 then 'september'
	when FLOOR(1 + (RAND() * 11)) = 10 then 'october'
	when FLOOR(1 + (RAND() * 11)) = 11 then 'november'
	when FLOOR(1 + (RAND() * 11)) = 12 then 'decenber'
end);
*/

select firstname, birthday from users where birthday rlike 'may|august' 