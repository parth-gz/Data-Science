SELECT COUNT(*) FROM customer
WHERE First_name LIKE 'J%'

SELECT COUNT(*) FROM customer
WHERE First_name LIKE 'J%' AND Last_name LIKE 'S%'

SELECT *FROM customer
WHERE First_name ILIKE 'j%' AND Last_name ILIKE 's%'

SELECT count(*) FROM customer
WHERE First_name LIKE '%her%' 

SELECT * FROM customer
WHERE First_name NOT LIKE '%_her%' 


SELECT * FROM customer
WHERE First_name LIKE 'A%'  AND last_name NOT LIKE 'B%' 
ORDER BY last_name


select count(amount)from payment 
where amount>5

select count(*) from actor
where first_name LIKE 'P%'

select Count(distinct(district)) from address

select distinct(district) from address

select count(*) from film
where rating='R'
AND replacement_cost between 5 AND 15

select count(*) from film
where title LIKE '%Truman%' 

--Aggregate functions	
select min(replacement_cost) from film

select max(replacement_cost) from film

select min(replacement_cost),max(replacement_cost) from film

--5/7
--GROUP BY
select *from payment

select customer_id,staff_id,sum(amount) from payment
group by staff_id,customer_id

select staff_id,customer_id,sum(amount) from payment
group by customer_id,staff_id

select staff_id,customer_id,sum(amount) from payment
group by customer_id,staff_id
order by staff_id

select staff_id,customer_id,sum(amount) from payment
group by customer_id,staff_id
order by staff_id,customer_id

select staff_id,customer_id,sum(amount) from payment
group by customer_id,staff_id
order by sum(amount)

--date and time
SELECT DATE(payment_date) FROM payment

SELECT DATE(payment_date) FROM payment
GROUP BY DATE(payment_date)

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount)

SELECT DATE(payment_date),SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC

--challenges
--we have two staff member,with saff id 1 and 2 we want to give a bonus to the staff member that handle the most payment(most in termsa of payment,not total dollar amount)
--how many payment did each staff member handle and who gets the bonus	
SELECT staff_id,COUNT(amount) from payment
GROUP BY staff_id
	
--corporate HQ is conducting A study on relationship between replacement cost and a movie MPAA rating(eg G ,PG,R etc)
--what is avg replacement cost per MPAA rating
--note:you may need to expand  the avg column to view correct result
SELECT rating,AVG(replacement_cost) from film
GROUP BY  rating

SELECT rating,ROUND(AVG(replacement_cost),2) from film
GROUP BY  rating

--challenge 3
--we are running a promotion to reward our top 5 customer with cupons
--what is the customer ids of the top 5 customer by total spend?	
SELECT customer_id,SUM(amount) from payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5

--HAVING
SELECT customer_id,SUM(amount) FROM payment
GROUP BY customer_id 
HAVING SUM(amount)>100

--8\7
SELECT customer_id,COUNT(*) FROM payment 
GROUP BY customer_id 
HAVING COUNT(*)>=40

SELECT customer_id,SUM(amount) from payment
WHERE staff_id=2
GROUP BY customer_id
HAVING SUM(amount)>100

--Alias AS
SELECT amount AS rental_price FROM payment

SELECT SUM(amount) AS net_revenue FROM payment

SELECT COUNT(amount) AS num_tranc FROM payment

SELECT COUNT(*) AS num_tranc FROM payment

SELECT customer_id,SUM(amount) from payment
GROUP BY customer_id

SELECT customer_id,SUM(amount) AS total_spent from payment
GROUP BY customer_id

SELECT customer_id,SUM(amount) from payment
GROUP BY customer_id
HAVING SUM(amount)>100

SELECT customer_id,SUM(amount) AS total_spent from payment
GROUP BY customer_id
HAVING SUM(amount)>100

SELECT customer_id,SUM(amount) AS total_spent from payment
GROUP BY customer_id
HAVING total_spent>100--error

SELECT customer_id,amount FROM payment 
WHERE amount>2

SELECT customer_id,amount AS new_name FROM payment 
WHERE new_name>2--error

--JOINS
select * FROM payment
	
SELECT * FROM customer

SELECT payment_id,payment.customer_id,first_name FROM payment
INNER JOIN customer
ON payment.customer_id=customer.customer_id

SELECT payment_id,payment.customer_id,first_name FROM customer
INNER JOIN payment
ON payment.customer_id=customer.customer_id

--FULL OUTER JOIN
SELECT * FROM customer
FULL OUTER JOIN payment
ON customer.customer_id=payment.customer_id

--LEFT OUTER JOIN
SELECT *FROM film
	
SELECT *FROM inventory

SELECT film.film_id,title,inventory_id FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id,store_id FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id,store_id FROM film
LEFT JOIN inventory ON
inventory.film_id=film.film_id
WHERE inventory.film_id IS null

--RIGHT OUTER JOIN	
SELECT film.film_id,title,inventory_id,store_id FROM film
RIGHT JOIN inventory ON
inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id,store_id FROM inventory
RIGHT JOIN film ON
inventory.film_id=film.film_id

SELECT film.film_id,title,inventory_id,store_id FROM film
RIGHT JOIN inventory ON
inventory.film_id=film.film_id
WHERE inventory.film_id IS null

09/07
--Challenges 1
select * from customer	
select * from address	
SELECT district,email FROM address
INNER JOIN customer ON
address.address_id=customer.address_id
WHERE district='California'

--2
select * from film_actor	
select * from film
select * from actor
	
SELECT title,first_name,last_name FROM actor
INNER JOIN film_actor 
ON actor.actor_id=film_actor.actor_id
INNER JOIN film 
ON film_actor.film_id=film.film_id
WHERE first_name='Nick' AND last_name='Wahlberg'

--10/07	
--CONDITIONAL EXPRESSION
SELECT *FROM customer

SELECT customer_id FROM customer
SELECT customer_id,
CASE
	WHEN (customer_id<=100)THEN 'Premium'
	WHEN(customer_id BETWEEN 100 AND 200)THEN'Plus'
	ELSE'Normal'
END
FROM customer

--------------------
	
SELECT customer_id,
CASE
	WHEN (customer_id<=100)THEN 'Premium'
	WHEN(customer_id BETWEEN 100 AND 200)THEN'Plus'
	ELSE'Normal'
END AS customer_class
FROM customer

--------------------
	
SELECT customer_id,
CASE customer_id
	WHEN 2 THEN 'Winner'
	WHEN 5 THEN 'Second place'
	ELSE 'Normal'
END AS raffle_results	
FROM customer
--------------------------
	
SELECT *FROM film
SELECT rental_rate FROM film

SELECT rental_rate,
CASE rental_rate
	WHEN 0.99 THEN '1'
	WHEN 4.99 THEN '5'
	WHEN 2.99 THEN '3'
	ELSE 'NORMAL'
END 	
FROM film

-----------------
	
SELECT
SUM(CASE rental_rate
	WHEN 0.99 THEN 1
	ELSE 0 
END) AS number_of_bargains
FROM film





