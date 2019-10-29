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
	user_id bigint unsigned,
	group_id bigint unsigned,
	
	PRIMARY KEY (user_id, group_id),
	
	foreign key (user_id) REFERENCES users(id),
	foreign key (group_id) REFERENCES `groups`(id)
);


drop table if exists profiles;
create table profiles (
	id serial,
	user_id bigint unsigned,
	photo_id bigint unsigned,
	birthdate datetime,
	gender enum('M','F'),
	activity varchar(150),
	about text,	
	
	foreign key (user_id) REFERENCES users(id),
	
	index(birthdate),
	index(gender)
);


drop table if exists courses;
create table courses (
	id serial,
	title varchar(100) not null,
	user_id bigint unsigned,
	created_at datetime default now(),
	updated_at datetime default now(),	
	price int,
	rating float,
	
	foreign key (user_id) REFERENCES users(id),
	
	index(title),
	index(price),
	index(rating)
);


drop table if exists lessons;
create table lessons (
	id serial,
	course_id bigint unsigned,
	title varchar(100) not null,
	created_at datetime default now(),
	updated_at datetime default now(),	
	
	foreign key (course_id) REFERENCES courses(id),
	
	index(title)
);

drop table if exists content;
create table content (
	id serial,
	lesson_id bigint unsigned,
	name varchar(100) not null,
	content_type enum('text','video','audio'),
	body text,
	link varchar(255),
	created_at datetime default now(),
	updated_at datetime default now(),	
	
	foreign key (lesson_id) REFERENCES lessons(id),
	
	index(name),
	index(content_type)
);


