### База данных Northwind Traders

Имеющая база данных касается компании Northwind Traders. База данных фиксирует все транзакции продаж и поставки товаров, производимых компанией, своим клиентам.

БД содержит следующую подробную информацию:

1. Клиенты Northwind Traders, которые покупают у компании товары (таблица *customers*)
2. Информация о товарах, которыми торгует компания (таблица *products*)
3. Группы / категории товаров (таблица *categories*)
4. Сведения о сотрудниках Northwind Traders (таблица *employees*)
5. Сведения о грузоперевозчиках, которые доставляют товары конечным покупателям (таблица *shippers*)
6. Сведения по договорам / заказам (таблица *orders*)
7. Детальная информация по договорам / заказам (таблица *order_details*)
8. Информация по поставщикам, готовым поставлять товары, на которых строится бизнес Northwind Traders (таблица *suppliers*)

![ER-диаграмма БД](C:\Users\Dusya\PycharmProjects\pythonProject\Northwind_DB_SQL\ER-diagram.PNG)

Проект включает:
- схематическое изображение структуры БД (ER-diagram.png)
- работу с данными, представленными по [ссылке на json файл с информацией о поставщиках](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2dbad09f-30ef-4728-a0e0-bd6842ed6858/suppliers.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221019T075619Z&X-Amz-Expires=86400&X-Amz-Signature=0a104ca5732958a3f8e22f86e3ac0945e4ae0111a19fda337a878381f9b6973f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22suppliers.json%22&x-id=GetObject) (suppliers_table_form.py)
- скрипты для заполнения таблицы suppliers на основе json файла (suppliers_table.sql, main.py)
- скрипты для написания SQL-запросов для выборки данных для страниц внутреннего портала Northwind Traders