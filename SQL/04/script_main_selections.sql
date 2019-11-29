/* все активные пользователи из группы Студенты  */

select u.name, u.lastname, u.secondname, u.email from users u 
left join users_groups ug on u.id = ug.user_id
left join `groups` g on ug.group_id = g.id
where u.active = 1 and g.code = 'students';

/* сколько всего активных студентов и авторов курсов */

select g.code, count(g.code) as 'count' from users u
left join users_groups ug on u.id = ug.user_id
left join `groups` g on ug.group_id = g.id
where u.active = 1 and g.code in ('students','teachers')
group by g.code;

/* сколько всего уроков в каждом курсе */

select c.title as 'courses', count(c.title) as 'lessons' from courses c
left join lessons on c.id=lessons.course_id
group by c.title;

/* Открытие пользователю c id=1 курса c id=3 после оплаты */
select c.id,c.title from courses c
left join orders o on o.course_id=c.id
left join payments p on o.id=p.order_id
where o.user_id = 1 and c.id = 3 and p.status = 'payed';

/* какая общая сумма по всем заказам была у пользователя с id=1 */

select count(*) as 'orders_count', sum(o.total_price) as 'total_sum' from orders o
left join users u on o.user_id=u.id
where u.id = 1;

/* сколько заказов было сделано с помощью платежной системе Robokassa */

select count(*) as 'orders' from orders o
left join payments p on o.id=p.order_id
left join payment_systems ps on p.payment_system_id=ps.id
where ps.name = 'Robokassa';