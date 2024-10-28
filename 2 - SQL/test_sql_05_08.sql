1.	Write a SQL statement to create a simple table countries, including columns country_id,country_name and region_id which already exist.

create table countries(
	country_id int  unique primary key,
	country_name varchar(50),
	region_id int
)	

2.	Create the two tables Sales and products and insert some sample data into them.
	Sales table columns: 
sale_id	product_id	quantity_sold	sale_date	total_price

Products table columns:
product_id	product_name	category	unit_price

Filter the Sales table to show only sales with a total_price greater than $100.


create table Sale(
	sale_id int  unique primary key,
    product_id int,
	quantity_sold int,
	sale_date date,
	total_price float
)	


insert into sale(sale_id,product_id,quantity_sold,sale_date,total_price) 
	values(1,20,20,'2004/01/01',1000)

insert into sale(sale_id,product_id,quantity_sold,sale_date,total_price) 
	values(2,10,10,'2004/02/01',10)

insert into sale(sale_id,product_id,quantity_sold,sale_date,total_price) 
	values(3,30,30,'2004/03/01',10000.78)

select *from sales
	

create table Products(
    product_id int,
	product_name varchar(50),
	category varchar(20),
	unit_price int
)	
insert into products(product_id,product_name,category,unit_price) 
	values(20,'A','comp',1000)

insert into products(product_id,product_name,category,unit_price) 
	values(10,'B','electonics',200)

insert into products(product_id,product_name,category,unit_price) 
	values(30,'C','mech',199)

select *from products
	
select sale_id from sales where total_price>100

3.	Retrieve the total_price of all sales, rounding the values to two decimal places.

select round(total_price) from sale 

4.	Calculate the total revenue generated from sales of products in the ‘Electronics’ category.

SELECT SUM(s.total_price) AS total_revenue
FROM sale s
JOIN products p ON s.product_id = p.product_id
WHERE p.category = 'electonics';

5.	Retrieve the product_name and category from the Products table, ordering the results by category in ascending order.

	select product_name,category from products order by category
