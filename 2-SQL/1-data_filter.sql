--12/07
show timezone

create table timezone(
	ts timestamp without time zone,
	tz timestamp with time zone
)

insert into timezone values(
	timestamp without time zone'2023-03-07 10:50',
	timestamp with time zone'2023-03-07 10:50'
)
select *from timezone

select now()::date
select current_date

select to_char(current_date,'dd/mm/yy')
select to_char(current_date,'ddd')
select to_char(current_date,'ww')

--calculate age
select age(date'2004=03-01')

--age between to dates	
select age(date'2004=03-01',date'2020/03/01')

--extract day
select extract(day from date'1992/11/13')as day

--extract month
select extract(month from date'1992/11/13')as month

--extract year
select extract(year from date'1992/11/13')as year

select date_trunc('year',date'1992/11/13')

--q1
select age(birth_date), *from employees
where (
	extract(year from age(birth_date))
	)>60

--q2
select count(emp_no) from employees
where extract(month from hire_date)=2

--q3
select count(emp_no) from employees
where extract(month from birth_date)=11

--q4	
SELECT MAX(AGE(birth_date))FROM employees


select max(salary) from salaries

select *,max(salary) from salaries--error

select *,max(salary) over() from salaries

select *,max(salary) over() from salaries limit 100

select *,max(salary) over() from salaries
where salary<70000

select *,avg(salary) over()
from salaries

select *,d,dept_name,avg(salary) over()
from salaries
join dept_emp as de using (emp_no)
join departments as d using (dept_no)

select *,d,dept_name,avg(salary) over(
	partition by d.dept_name
)
from salaries
join dept_emp as de using (emp_no)
join departments as d using (dept_no)

select *,d,dept_name,avg(salary) over(
)
from salaries
join dept_emp as de using (emp_no)
join departments as d using (dept_no)
