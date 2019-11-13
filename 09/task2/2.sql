/* При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот, 
 * поиск электронного адреса пользователя по его имени.
 */
 
SET igor@mail.ru:1 Igor:1
SET maria@mail.ru:2 Maria:2
SET oleg@mail.ru:3 Oleg:3
 
 /* поиск имени по email*/
 
GET igor@mail.ru
GET maria@mail.ru
GET oleg@mail.ru

 /* поиск email по имени (смотрим идентификатор рядом с именем и подставляем в запрос) */
 
keys *:1
keys *:2
keys *:3
 
 
 