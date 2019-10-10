/*
 * 
 * Проанализировать структуру БД vk, которую мы создали на занятии, и внести предложения по усовершенствованию (если такие идеи есть). Напишите пожалуйста, всё-ли понятно по структуре.
 *
 * 
 *  Усовершенствования:
 * 
 * У пользователей есть свои страницы, где они размещают контент, для этого нужна отдельная сущность user_page
 * 
 * Также есть лента, куда добавляются новости, на которые подписаны пользователи, нужна таблица lenta
 * 
 * YНужна еще сущность post, которая будет состоять из текста и прикрепленного медиа
 * 
 * Нужно связать медиа с теми сущностями, где оно используется (посты, сообщения)
 * В сообщества добавить связь на посты
 *
 */



drop database if exists vk;
create database vk;
use vk;

drop table if exists users;
create table users (
	id serial primary key,
	firstname varchar(100),
	lastname varchar(100),
	email varchar(100) unique,
	password_hash varchar(255),
	phone bigint unsigned,
	
	index (email),
	index (phone)
);


drop table if exists friend_request;
create table friend_request (
	from_user_id bigint unsigned,
	to_user_id bigint unsigned,
	status enum('subscrited', 'unsubscribed','waited','declined'),
	created_at datetime default now(),
	updated_at datetime default now(),
	
	primary key (from_user_id, to_user_id),
	foreign key (from_user_id) references users(id),
	foreign key (to_user_id) references users(id),
	
	index (status)
);

drop table if exists media_types;
create table media_types (
	id serial primary key,
	name varchar(100),
	created_at datetime default now(),
	
	index (name)	
);

drop table if exists media;
create table media (
	id serial primary key,
	media_type_id bigint unsigned,
	user_id bigint unsigned,
	body text,
	filename varchar(150),
	size int,
	metadata json,
	created_at datetime default now(),
	updated_at datetime default now(),
	
	foreign key (user_id) references users(id),
	foreign key (media_type_id) references media_types(id),
	
	index (media_type_id),
	index (user_id),
	index (filename)	
);

drop table if exists photo_album;
create table photo_album (
	id serial primary key,
	name varchar(100),
	user_id bigint unsigned,
	
	foreign key (user_id) references users(id),
	
	index (name),
	index (user_id)
);

drop table if exists photo;
create table photo (
	id serial primary key,
	album_id bigint unsigned,
	media_id bigint unsigned,
	
	foreign key (media_id) references media(id),
	foreign key (album_id) references photo_album(id),
	
	index (album_id),
	index (media_id)
);

drop table if exists messages;
create table messages (
	id serial primary key,
	from_user_id bigint unsigned,
	to_user_id bigint unsigned,
	media_id bigint unsigned,
	body text,
	created_at datetime default now(),
	
	foreign key (from_user_id) references users(id),
	foreign key (to_user_id) references users(id),
	foreign key (media_id) references media(id),
	
	index (from_user_id),
	index (to_user_id),
	index (media_id)
);

drop table if exists profiles;
create table profiles (
	id serial primary key,
	user_id bigint unsigned,
	gender char(1),
	birthday date,
	photo_id bigint unsigned,
	hometown varchar(150),
	created_at datetime default now(),
	
	foreign key (user_id) references users(id),
	foreign key (photo_id) references photo(id),
	
	index (user_id),
	index (gender),
	index (birthday),
	index (hometown)	
);


drop table if exists likes;
create table likes (
	id serial primary key,
	user_id bigint unsigned,
	created_at datetime default now(),
	
	foreign key (user_id) references users(id),
	
	index (user_id)
);


drop table if exists post;
create table post (
	id serial primary key,
	user_id bigint unsigned,
	media_id bigint unsigned,
	body text,
	created_at datetime default now(),
	updated_at datetime default now(),
	
	foreign key (user_id) references users(id),
	foreign key (media_id) references media(id),
	
	index (user_id)
);

drop table if exists communities;
create table communities (
	id serial primary key,
	post_id bigint unsigned,
	name varchar(255),
	
	foreign key (post_id) references post(id),
	
	index (name),
	index (post_id)
);

drop table if exists users_communities;
create table users_communities (
	user_id bigint unsigned,
	community_id bigint unsigned,
	
	foreign key (user_id) references users(id),
	foreign key (community_id) references communities(id),
	
	primary key (user_id, community_id)
);

drop table if exists user_page;
create table user_page (
	id serial primary key,
	user_id bigint unsigned,
	post_id bigint unsigned,
	created_at datetime default now(),
	updated_at datetime default now(),
	
	foreign key (user_id) references users(id),
	foreign key (post_id) references post(id),
	
	index (user_id),
	index (post_id)
);

drop table if exists lenta;
create table lenta (
	id serial primary key,
	user_id bigint unsigned,
	post_id bigint unsigned,
	updated_at datetime default now(),
	
	foreign key (user_id) references users(id),
	foreign key (post_id) references post(id),
	
	index (user_id),
	index (post_id)
);



