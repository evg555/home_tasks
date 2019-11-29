/*
 *(по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
 *Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
 *Вызов функции FIBONACCI(10) должен возвращать число 55
*/

delimiter //
create function FIBONACCI (n int)
returns int deterministic
begin
	declare i int default 0;
	declare fib1 int default 1;
	declare fib2 int default 1;
	declare fib_sum  int default 0;

	if (n < 1) then
		return 0;
	end if;

	while i < n - 2 do
	    set fib_sum = fib1 + fib2;
	    set fib1 = fib2;
	    set fib2 = fib_sum;
	    set i = i + 1;
    end while;	
	
	return fib2;
end//