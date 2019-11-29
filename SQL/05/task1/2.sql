/*
 * Таблица users была неудачно спроектирована. 
 * Записи created_at и updated_at были заданы типом VARCHAR 
 * и в них долгое время помещались значения в формате "20.10.2017 8:10". 
 * Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
 */

use vk;

/* создаем тестовую ситуацию
alter table users change created_at created_at varchar(50);
alter table users change updated_at updated_at varchar(50);

update users set created_at = "20.10.2017 8:10", updated_at = "20.10.2017 8:10";
*/

update users set created_at = str_to_date(created_at, "%d.%c.%Y %H:%i"), updated_at = str_to_date(updated_at, "%d.%c.%Y %H:%i");

alter table users change created_at created_at datetime default now();
alter table users change updated_at updated_at datetime default now();