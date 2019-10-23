create database if not exists myproject;
use myproject;

drop table if exists users;
create table users (
	id serial,
	name varchar(50) NOT null,
	lastname varchar(50),
	secondname varchar(50),
	email varchar(100) UNIQUE NOT null,
	phone int,
	password_hash varchar(100),
	active boolean DEFAULT TRUE,
	
	index(name),
	index(lastname),
	index(secondname),
	index(phone),
	index(active)
);


drop table if exists `groups`;
create table `groups` (
	id serial,
	name varchar(150),
	code varchar(150),
	active boolean DEFAULT TRUE,
	
	index(name),
	index(code),
	index(active)
);

drop table if exists users_groups;
create table users_groups (
	users_id bigint unsigned,
	groups_id bigint unsigned,
	
	PRIMARY KEY (users_id, groups_id),
	
	foreign key (users_id) REFERENCES users(id),
	foreign key (groups_id) REFERENCES `groups`(id)
);


drop table if exists profiles;
create table profiles (
	id serial,
	users_id bigint unsigned,
	photo_id bigint unsigned,
	birthdate datetime,
	gender enum('M','F'),
	activity varchar(150),
	about text,	
	
	foreign key (users_id) REFERENCES users(id),
	
	index(birthdate),
	index(gender)
);



drop table if exists courses;
create table courses (
	id serial,
	title varchar(100) not null,
	user_id bigint unsigned,
	price int,
	rating float
);