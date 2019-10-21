create database if not exists myproject;
use my_project;

drop table if exists courses;
create table courses (
	id serial,
	title varchar(100) not null,
	user_id bigint unsigned,
	price int,
	rating float
);
