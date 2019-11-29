use vk;



 /* - Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем. */

select from_user_id, count(from_user_id) as 'cnt' from messages where to_user_id = 1 and from_user_id in (
	select from_user_id from friend_request where to_user_id = 1 and status = 'subscribed'
) group by from_user_id order by cnt desc limit 1;




/* - Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.. */

select count(*) as 'cnt_likes' from likes where user_id in (
	select user_id from profiles where TIMESTAMPDIFF(YEAR, birthday, now()) < 18
)




/* - Определить кто больше поставил лайков (всего) - мужчины или женщины? */

select case (gender)
	when 'M' then 'Мужчины'
	when 'F' then 'Женщины'
end, count(*) as 'cnt_likes' from profiles where gender is not null and user_id in (
	select user_id from likes
) group by gender 