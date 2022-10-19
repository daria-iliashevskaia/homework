--Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
SELECT employees.first_name, employees.last_name, employees.home_phone, employees.region
FROM employees
WHERE employees.region is NULL;

--Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики,
--но при этом в них не "зарегистрированы" работники

SELECT customers.country
FROM customers
INTERSECT
SELECT suppliers.ad_country
FROM suppliers
EXCEPT
SELECT employees.country
FROM employees;




