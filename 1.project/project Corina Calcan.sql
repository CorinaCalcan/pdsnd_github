/* first slide : which are the top 10 most popular children's movies according to the rental data */
/* The query lists the movie names, the category it is classified in, and the number of times it has been rented out */

SELECT
  f.title,
  c.name,
  COUNT(r.rental_id) AS total_rented_times
FROM category c
JOIN film_category fc
  ON c.category_id = fc.category_id
  AND c.name IN ('Children')
JOIN film f
  ON f.film_id = fc.film_id
JOIN inventory i
  ON f.film_id = i.film_id
JOIN rental r
  ON i.inventory_id = r.inventory_id
GROUP BY 1,
         2
ORDER BY 3 DESC
LIMIT 10;

/* second slide : Who are the 20 top clients in terms of spending and number of rentals per year? */
/* The query lists the top customers, how many times they rented movies, and the overall sum they spent on renting per year */
SELECT
  CONCAT(customer.first_name, ' ', customer.last_name) fullname,
  SUM(payment.amount) total_spending,
  COUNT(DATE_TRUNC('month', payment.payment_date)) total_rentals
FROM customer
JOIN payment
  ON customer.customer_id = payment.customer_id
GROUP BY 1
ORDER BY 2 DESC
LIMIT 20;

/* third slide : Who are the clients who spent the most in the month of March on rentals? ( query limited to first 15)*/
/* The query lists the top 15 customers that spent the most in March on movie rentals */
SELECT
  sub.full_name,
    COUNT(sub.date) march_rentals, SUM(sub.amount) march_total
FROM (SELECT
  CONCAT(customer.first_name, ' ', customer.last_name) full_name, payment.amount amount,
  payment.payment_date date
FROM customer
JOIN payment
  ON customer.customer_id = payment.customer_id
      WHERE payment.payment_date BETWEEN '2007-03-01' AND '2007-03-31'
GROUP BY 1,
         2,
         3
ORDER BY 1) sub

GROUP BY 1
         
ORDER BY 3 DESC, 1
LIMIT 15;

/* fourth slide :the clients who brought the biggest revenue for the year (SUB+WINDOW)*/
/* The query lists the top 10 customers that were the most loyal to the bussiness for the whole year */
SELECT DISTINCT
  sub.full_name,
  SUM(sub.total) OVER (PARTITION BY sub.full_name) total_spending
FROM (SELECT
  CONCAT(customer.first_name, ' ', customer.last_name) full_name,
  SUM(payment.amount) total,
  DATE_TRUNC('month', payment.payment_date) rental_month
FROM customer
JOIN payment
  ON customer.customer_id = payment.customer_id
GROUP BY 1,
         3
ORDER BY 1, 3) sub
GROUP BY 1,
         sub.total
ORDER BY 2 DESC
LIMIT 10;
