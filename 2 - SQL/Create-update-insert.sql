--09/07
--CREATING TABLES AND DATABASES
CREATE  TABLE account(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR(50) NOT NULL,
	email VARCHAR(250) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	lat_login TIMESTAMP
)

CREATE  TABLE job(
	job_id SERIAL PRIMARY KEY,
	job_name VARCHAR(200) UNIQUE NOT NULL
)

CREATE  TABLE account_job(
	user_id INTEGER REFERENCES account(user_id)
)

CREATE  TABLE account_job1(
	user_id INTEGER REFERENCES account(user_id),
	job_id INTEGER REFERENCES job(job_id),
	hire_date TIMESTAMP
	)

select *from account
	
insert into account(username,password,email,created_on)
values
('Jose','password','jose@email.com',current_timestamp)

select *from job
	
insert into job(job_name)
values
('Astronaut')

insert into job(job_name)
values
('President')

select *from account_job1
	
insert into account_job1(user_id,job_id,hire_date)
values
(1,1,current_timestamp)

insert into account_job1(user_id,job_id,hire_date)
values
(10,10,current_timestamp)

insert into account(username,password,email,created_on)
values
('Rehan','SR','rehan@email.com',current_timestamp)

insert into job(job_name)
values
('Data Scientist')

select *from account
	
update account set lat_login=current_timestamp

update account set lat_login=created_on

select *from account_job1

update account_job1
set hire_date=account.created_on
from account
where account_job1.user_id=account.user_id

--10/07
SELECT *FROM job
	
--INSERT
INSERT INTO job(job_name)VALUES('Cowboy')
	
SELECT *FROM job

--------------------
--DELETE	
DELETE FROM job WHERE job_name='Cowboy'RETURNING job_id,job_name
SELECT *FROM job

--------------------
	
CREATE TABLE information (info_id SERIAL PRIMARY KEY,title 
	VARCHAR(500) NOT NULL,person VARCHAR(50)NOT NULL UNIQUE)
SELECT * FROM information

--------------------
--ALTER	
ALTER TABLE information RENAME TO new_info
SELECT * FROM information--error=>does not exist
SELECT * FROM new_info

--------------------
	
ALTER TABLE new_info RENAME COLUMN person TO people
SELECT * FROM new_info

--------------------
	
INSERT INTO new_info(title)VALUES('some new title')--ERROR
	
ALTER TABLE new_info ALTER COLUMN people DROP NOT NULL
INSERT INTO new_info(title)VALUES('some new title')
SELECT * FROM new_info

--------------------
	
ALTER TABLE new_info DROP COLUMN people
SELECT * FROM new_info

--------------------
	
ALTER TABLE new_info DROP COLUMN people--error because that column is not exist now

ALTER TABLE new_info DROP COLUMN IF EXISTS people

CREATE TABLE employees(emp_id SERIAL PRIMARY KEY,first_name 
	VARCHAR(50) NOT NULL,last_name VARCHAR(50)NOT NULL,
	birthdate DATE CHECK (birthdate>'1900-01-01'),
	hire_date DATE CHECK (hire_date>birthdate),salary INTEGER CHECK (salary>0) 
)
SELECT *FROM employees

--------------------
	
INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES('Jose','portilla','1990-11-03','2010-01-01',100)
SELECT *FROM employees

--------------------
	
INSERT INTO employees(first_name,last_name,birthdate,hire_date,salary)
VALUES('John','Smith','1990-11-03','2010-01-01',100)
SELECT *FROM employees

--------------------






















