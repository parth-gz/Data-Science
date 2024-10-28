--12/07
--Assignment 1
create table manufacture(
	log_id serial primary key,
	machine_id integer,
	production_date date,
	production_shift varchar(60),
	production_produced integer, 
	defects integer,
	runtime float
)

select *from manufacture

insert into manufacture (machine_id,production_date,production_shift,production_produced,defects,runtime)
values(1,'2024-06-01','Morning', 500, 5, 8.0),
    (1, '2024-06-01', 'Evening', 450, 3, 7.5),
	(2, '2024-06-01', 'Morning', 480, 2, 7.8), 
	(2, '2024-06-01', 'Evening', 470, 4, 8.1), 
	(3, '2024-06-01', 'Morning', 510, 6, 8.2), 
	(3, '2024-06-01', 'Evening', 520, 1, 7.9), 
	(1, '2024-06-02', 'Morning', 490, 3, 8.0), 
	(1, '2024-06-02', 'Evening', 460, 2, 7.6), 
	(2, '2024-06-02', 'Morning', 475, 1, 7.9), 
	(2, '2024-06-02', 'Evening', 465, 5, 8.3), 
	(3, '2024-06-02', 'Morning', 505, 4, 8.0), 
	(3, '2024-06-02', 'Evening', 515, 3, 8.2);

select max(defects),avg(runtime) from manufacture

--Assignment 2
create table grades(
    grade_id serial primary key,
    student_id int not null,
    course_id int not null,
    grade float,
    grade_date date
)

select * from grades

insert into grades(student_id,course_id,grade,grade_date)
values(1, 101, 85.5, '2024-01-15'), 
	(1, 102, 78.0, '2024-02-20'), 
	(2, 101, 92.0, '2024-01-15'), 
	(2, 103, 88.5, '2024-03-10'), 
	(3, 102, 74.0, '2024-02-20'), 
	(3, 103, 81.5, '2024-03-10'), 
	(4, 101, 67.0, '2024-01-15'), 
	(4, 104, 90.0, '2024-04-05'), 
	(5, 102, 85.0, '2024-02-20'), 
	(5, 104, 87.0, '2024-04-05')

select student_id, avg(grade) as average_grade
from grades
group by student_id
having avg(grade) <80

--Assignment 3
create table customers (
    customer_id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100) not null,
    phone_number varchar(15),
    address varchar(100),
    city varchar(50),
    state varchar(2),
    zip_code varchar(10) not null,
    plan_id int,
    last_call_date date
)

select *from customers
	
insert into customers (first_name, last_name, email, phone_number, address, city, state, zip_code, plan_id, last_call_date)
values
('john', 'doe', 'john.doe@example.com', '123-456-7890', '123 elm st', 'springfield', 'il', '62701', 1, '2024-06-01'),
('jane', 'smith', 'jane.smith@example.com', '987-654-3210', '456 oak st', 'springfield', 'il', '62701', 2, '2024-05-15'),
('alice', 'johnson', 'alice.johnson@example.com', '555-123-4567', '789 pine st', 'shelbyville', 'il', '62565', 3, '2024-04-20'),
('bob', 'brown', 'bob.brown@example.com', '444-555-6666', '101 maple st', 'capital city', 'il', '62702', 1, '2024-06-10'),
('charlie', 'davis', 'charlie.davis@example.com', '333-444-5555', '202 cedar st', 'springfield', 'il', '62701', 2, '2024-03-30'),
('diana', 'evans', 'diana.evans@example.com', '222-333-4444', '303 birch st', 'shelbyville', 'il', '62565', 3, '2024-06-20'),
('ethan', 'foster', 'ethan.foster@example.com', '111-222-3333', '404 spruce st', 'capital city', 'il', '62702', 1, '2024-02-14'),
('fiona', 'garcia', 'fiona.garcia@example.com', '999-888-7777', '505 ash st', 'springfield', 'il', '62701', 2, '2024-05-05'),
('george', 'harris', 'george.harris@example.com', '888-777-6666', '606 walnut st', 'shelbyville', 'il', '62565', 3, '2024-01-25'),
('hannah', 'irvine', 'hannah.irvine@example.com', '777-666-5555', '707 hickory st', 'capital city', 'il', '62702', 1, '2024-06-22');

select
    customer_id,first_name,last_name,email,phone_number,address,city,state,zip_code,plan_id,last_call_date,
case
     when last_call_date >= date '2024-07-13' - interval '1 month' then 'Active'
     when last_call_date >= date '2024-07-13' - interval '3 months' then 'Risk'
     else 'Inactive'
end as Result
from customers;

create table products (
    product_id serial primary key,
    product_name varchar(50),
    category varchar(50),
    quantity int ,
    price float,
    supplier varchar(100) ,
    last_restock_date date 
)

select *from products

insert into products (product_name, category, quantity, price, supplier, last_restock_date) 
values
('Laptop', 'Electronics', 50, 799.99, 'TechSupplier Inc.', '2024-06-01'),
('Smartphone', 'Electronics', 150, 499.99, 'MobileDistributors Ltd.', '2024-05-25'),
('Desk Chair', 'Furniture', 80, 89.99, 'OfficeSupplies Co.', '2024-05-15'),
('Notebook', 'Stationery', 200, 2.99, 'PaperGoods Inc.', '2024-06-10'),
('Water Bottle', 'Accessories', 120, 9.99, 'Lifestyle Products', '2024-06-05'),
('Headphones', 'Electronics', 70, 149.99, 'TechSupplier Inc.', '2024-06-08'),
('Desk Lamp', 'Furniture', 60, 29.99, 'OfficeSupplies Co.', '2024-05-20'),
('Backpack', 'Accessories', 90, 49.99, 'TravelGear Ltd.', '2024-06-12'),
('Pen', 'Stationery', 300, 1.49, 'PaperGoods Inc.', '2024-06-03'),
('Monitor', 'Electronics', 40, 199.99, 'TechSupplier Inc.', '2024-06-15')

select *from products 
where quantity <= 50;


--Assignment 4
create table patients (
    patient_id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
    date_of_birth date,
    gender varchar(10),
    phone_number varchar(15),
    email varchar(100),
    address varchar(100),
    city varchar(50),
    state varchar(20),
    zip_code varchar(10) ,
    medical_history varchar(50),
    last_visit_date date 
)

select *from patients

insert into patients (first_name, last_name, date_of_birth, gender, phone_number, email, address, city, state, zip_code, medical_history, last_visit_date) 
values
('John', 'Doe', '1980-01-15', 'Male', '123-456-7890', 'john.doe@example.com', '123 Elm St', 'Springfield', 'IL', '62701', 'Hypertension', '2024-06-01'),
('Jane', 'Smith', '1990-02-20', 'Female', '987-654-3210', 'jane.smith@example.com', '456 Oak St', 'Springfield', 'IL', '62701', 'Diabetes', '2024-05-25'),
('Alice', 'Johnson', '1975-03-30', 'Female', '555-123-4567', 'alice.johnson@example.com', '789 Pine St', 'Shelbyville', 'IL', '62565', 'Asthma', '2024-06-10'),
('Bob', 'Brown', '1965-04-10', 'Male', '444-555-6666', 'bob.brown@example.com', '101 Maple St', 'Capital City', 'IL', '62702', 'High Cholesterol', '2024-05-15'),
('Charlie', 'Davis', '1985-05-20', 'Male', '333-444-5555', 'charlie.davis@example.com', '202 Cedar St', 'Springfield', 'IL', '62701', 'Allergies', '2024-06-05'),
('Diana', 'Evans', '2000-06-25', 'Female', '222-333-4444', 'diana.evans@example.com', '303 Birch St', 'Shelbyville', 'IL', '62565', 'Migraine', '2024-06-20'),
('Ethan', 'Foster', '1970-07-15', 'Male', '111-222-3333', 'ethan.foster@example.com', '404 Spruce St', 'Capital City', 'IL', '62702', 'Arthritis', '2024-06-12'),
('Fiona', 'Garcia', '1995-08-10', 'Female', '999-888-7777', 'fiona.garcia@example.com', '505 Ash St', 'Springfield', 'IL', '62701', 'Depression', '2024-05-30'),
('George', 'Harris', '1988-09-05', 'Male', '888-777-6666', 'george.harris@example.com', '606 Walnut St', 'Shelbyville', 'IL', '62565', 'Hypertension', '2024-04-25'),
('Hannah', 'Irvine', '1992-10-12', 'Female', '777-666-5555', 'hannah.irvine@example.com', '707 Hickory St', 'Capital City', 'IL', '62702', 'Diabetes', '2024-06-22');

select *from patients
where last_visit_date between '2024-05-01' and '2024-05-31';

--Assignment 5
create table transactions (
    transaction_id serial primary key,
    account_id int ,
    transaction_date timestamp not null,
    transaction_amount float,
    transaction_type varchar(10),
    merchant varchar(100),
    location varchar(100),
    status varchar(20)
);

select *from transactions

insert into transactions (account_id, transaction_date, transaction_amount, transaction_type, merchant, location, status) 
values
(1, '2024-06-01 10:00:00', 1000.00, 'Credit', 'Amazon', 'Online', 'Completed'),
(1, '2024-06-01 12:30:00', 500.00, 'Debit', 'Walmart', 'Springfield', 'Completed'),
(2, '2024-06-02 09:45:00', 15000.00, 'Credit', 'Apple Store', 'Chicago', 'Pending'),
(2, '2024-06-02 11:00:00', 200.00, 'Debit', 'Starbucks', 'Chicago', 'Completed'),
(3, '2024-06-03 14:15:00', 250.00, 'Debit', 'Target', 'Springfield', 'Completed'),
(3, '2024-06-03 16:20:00', 30000.00, 'Credit', 'Tesla', 'San Francisco', 'Pending'),
(4, '2024-06-04 08:30:00', 120.00, 'Debit', 'McDonalds', 'Springfield', 'Completed'),
(4, '2024-06-04 10:50:00', 6000.00, 'Credit', 'Best Buy', 'Chicago', 'Pending'),
(5, '2024-06-05 15:10:00', 70.00, 'Debit', 'CVS Pharmacy', 'Springfield', 'Completed'),
(5, '2024-06-05 17:00:00', 22000.00, 'Credit', 'Louis Vuitton', 'New York', 'Pending');

select  *from transactions
where transaction_amount > 1234
and transaction_date between '2024-06-01' and '2024-06-05';
