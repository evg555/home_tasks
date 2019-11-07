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

drop table if exists `hometasks`;
create table `hometasks` (
	id serial,
	lesson_id bigint unsigned,
	user_id bigint unsigned,
	link varchar(150),
	comment text,
	
	foreign key (lesson_id) REFERENCES lessons(id),
	foreign key (user_id) REFERENCES users(id),
	
	index(lesson_id),
	index(user_id)	
);

drop table if exists `tests`;
create table `tests` (
	id serial,
	lesson_id bigint unsigned,
	name varchar(150),
	
	foreign key (lesson_id) REFERENCES lessons(id),
	
	index(lesson_id),
	index(name)	
);


drop table if exists `questions`;
create table `questions` (
	id serial,
	test_id bigint unsigned,
	title varchar(150),
	
	foreign key (test_id) REFERENCES tests(id),
	
	index(test_id),
	index(title)	
);

drop table if exists `answers`;
create table `answers` (
	id serial,
	user_id bigint unsigned,		
	question_id bigint unsigned,	
	
	foreign key (user_id) REFERENCES users(id),
	foreign key (question_id) REFERENCES questions(id),
	
	index(user_id),
	index(question_id)	
);

drop table if exists feedbacks;
create table feedbacks (
	id serial,
	user_id bigint unsigned,		
	course_id bigint unsigned,	
	title varchar(150) default '', 
	body text,
	
	foreign key (user_id) REFERENCES users(id),
	foreign key (course_id) REFERENCES courses(id),
	
	index(user_id),
	index(course_id)	
);



drop table if exists feedbacks;
create table feedbacks (
	id serial,
	user_id bigint unsigned,		
	course_id bigint unsigned,	
	title varchar(150) default '', 
	body text,
	
	foreign key (user_id) REFERENCES users(id),
	foreign key (course_id) REFERENCES courses(id),
	
	index(user_id),
	index(course_id)	
);


drop table if exists discounts;
create table discounts (
	id serial,
	name varchar(150),
	`type` enum('%', 'RUB'),
	total int,
	
	index(name)	
);

drop table if exists coupons;
create table coupons (
	id serial,
	name varchar(150),
	discount_id bigint unsigned,
	active bool,
	date_start datetime default now(),
	date_end datetime,
	
	foreign key (discount_id) REFERENCES discounts(id),
	
	index(name),
	index(active),
	index(date_start),
	index(date_end)
);


drop table if exists orders;
create table orders (
	id serial,
	user_id bigint unsigned,		
	course_id bigint unsigned,	
	coupon_id bigint unsigned default null,
	total_price float,
	
	foreign key (user_id) REFERENCES users(id),
	foreign key (course_id) REFERENCES courses(id),
	foreign key (coupon_id) REFERENCES coupons(id),
	
	index(user_id),
	index(course_id)	
);

drop table if exists accounts;
create table accounts (
  id serial,
  user_id bigint unsigned,
  total float,
  locked bool,
  locked_at datetime DEFAULT CURRENT_TIMESTAMP,
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  updated_at datetime DEFAULT CURRENT_TIMESTAMP,
  
  foreign key (user_id) references users(id),
  
  index(user_id),
  index(created_at),
  index(updated_at)
);


drop table if exists `transaction`;
create table `transaction` (
  id serial,
  account_id bigint unsigned,
  total float,
  debit bool,
  comment text,
  created_at datetime DEFAULT CURRENT_TIMESTAMP,
  
  foreign key (account_id) references accounts(id),
  
  index(account_id),
  index(created_at)
);

drop table if exists payment_systems;
create table payment_systems (
  id serial,
  name varchar(150),
  comment text,
  
  index(name)
);


drop table if exists payments;
create table payments (
  id serial,
  order_id bigint unsigned,
  account_id bigint unsigned,  
  payment_system_id bigint unsigned,
  status enum('payed','declined'),  
  comment text,  
  payed_at datetime DEFAULT CURRENT_TIMESTAMP,  
  total float,
  
  foreign key (order_id) references orders(id),
  foreign key (account_id) references accounts(id),
  foreign key (payment_system_id) references payment_systems(id),
  
  index(order_id),
  index(account_id),
  index(payment_system_id),
  index(payed_at)
);

