/*
 * Добавить необходимую таблицу/таблицы для того, чтобы можно было использовать лайки для медиафайлов, постов и пользователей.
 * 
 * Можно создать дополнительную таблицу, где хранить id сущности, по которой лайкнули и название сущности
 * 
*/

use vk;

create table liked_entity (
	likes_id bigint unsigned unique,
	entity_id bigint unsigned,
	entity enum('post', 'message', 'media', 'photo_album'),
	
	primary key(likes_id, entity_id, entity),
	
	foreign key (likes_id) references likes(id)
)

