/*
 * (по желанию) »з таблицы catalogs извлекаютс¤ записи при помощи запроса.
 *  SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
 * ќтсортируйте записи в пор¤дке, заданном в списке IN.
 */

SELECT * FROM catalogs WHERE id IN (5, 1, 2) order by case
	when id = 5 then '1'
	when id = 1 then '2'
	when id = 2 then '3'
end;
	