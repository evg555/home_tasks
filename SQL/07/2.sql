/*
 * Выведите список товаров products и разделов catalogs, который соответствует товару.
 */ 

select p.name as 'Товар', c.name as 'Каталог' from products p left join catalogs c on p.catalog_id = c.id