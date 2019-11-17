/* top 3 самых оцененных курса */
create view top_3_rating_courses as
select c.title,u.name, u.lastname, c.price, c.rating from courses c
left join users u on c.author_id=u.id
order by rating desc limit 3;

/* top 3 курсов с наибольшим числом студентов */
create view  top_3_max_students_courses as
select c.title, u.lastname, c.price, count(*) as 'count_students' from courses c
inner join users u on c.author_id=u.id
inner join orders o on o.course_id=c.id
group by c.title, u.lastname, c.price
order by count_students desc limit 3;

/* Последние 5 отзывов */
create view  last_5_feedbacks as
select u.name,u.lastname,c.title as 'course',f.title,f.body from feedbacks f 
left join users u on f.user_id=u.id
left join courses c on c.id=f.course_id
order by f.created_at desc limit 5;