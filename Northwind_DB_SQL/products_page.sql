--Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц.
--Вывести наименование продуктов, кол-во единиц в продаже,
--имя контакта поставщика и его телефонный номер.

SELECT products.product_name, products.units_in_stock, suppliers.contact_name, suppliers.phone
FROM products
JOIN categories ON categories.category_id = products.category_id
JOIN suppliers ON suppliers.suppliers_id = products.fk_suppliers
WHERE (categories.category_name = 'Beverages' OR categories.category_name = 'Seafood')
AND products.discontinued = 0
GROUP BY products.product_name, products.units_in_stock, suppliers.contact_name, suppliers.phone
HAVING products.units_in_stock<20;