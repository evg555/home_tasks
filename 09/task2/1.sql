/* В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов. */


HSET user1 ip 78.59.87.65 count 1 last_date 2019-10-05
HSET user2 ip 195.150.26.01 count 1 last_date 2019-10-21
HSET user3 ip 66.48.159.24 count 1 last_date 2019-10-17