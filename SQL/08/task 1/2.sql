/*
 * Создайте представление, которое выводит название name товарной позиции из таблицы products 
 * и соответствующее название каталога name из таблицы catalogs
 */

create view products_catalogs as
select p.name as 'products', c.name as 'catalog' from shop.products p
left join shop.catalogs c on p.catalog_id = c.id;