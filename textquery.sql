# Query for V1
SELECT
  name AS categories,
  COUNT(*) counts
FROM category
JOIN film_category
  ON category.category_id = film_category.category_id
JOIN film
  ON film_category.film_id = film.film_id
JOIN inventory
  ON inventory.film_id = film.film_id
JOIN rental
  ON inventory.inventory_id = rental.inventory_id
WHERE category.name = 'Animation'
OR category.name = 'Children'
GROUP BY category.name
ORDER BY categories;

# Query for V2
WITH t1 AS
  (SELECT Concat(first_name, ' ', last_name) AS NAME,
          Sum(payment.amount) total
   FROM customer
   JOIN payment ON customer.customer_id= payment.customer_id
   GROUP BY 1
   ORDER BY 2 DESC
   LIMIT 3)
SELECT Date_trunc('month', payment.payment_date) months,
       Count(*) paynotimes,
       Sum(payment.amount) totalamt,
       t1.NAME
FROM customer
JOIN payment ON customer.customer_id= payment.customer_id
JOIN t1 ON Concat(first_name, ' ', last_name) = t1.NAME
WHERE NAME = t1.NAME
  AND payment.payment_date BETWEEN '20070101' AND '20080101'
GROUP BY 1,
         4
ORDER BY t1.NAME;

## Query for V3

WITH t1 AS
  (SELECT concat(first_name, ' ', last_name) AS name,
          sum(payment.amount) total
   FROM customer
   JOIN payment ON customer.customer_id= payment.customer_id
   GROUP BY 1
   ORDER BY 2 DESC
   LIMIT 10),
     t2 AS
  (SELECT date_trunc('month', payment.payment_date) months,
          sum(payment.amount) totalamt,
          t1.name,
          lead(sum(payment.amount)) over(PARTITION BY t1.name
                                         ORDER BY date_trunc('month', payment.payment_date)) lags,
                                    lead(sum(payment.amount)) over(PARTITION BY t1.name
                                                                   ORDER BY date_trunc('month', payment.payment_date))- sum(payment.amount) difference
   FROM customer
   JOIN payment ON customer.customer_id= payment.customer_id
   JOIN t1 ON concat(first_name, ' ', last_name) = t1.name
   WHERE name = t1.name
     AND payment.payment_date BETWEEN '20070101' AND '20080101'
   GROUP BY 1,
            3
   ORDER BY t1.name)
SELECT t2.name,
       max(difference) biggest_difference
FROM t2
GROUP BY 1
ORDER BY biggest_difference DESC
LIMIT 1;

## query for V4
SELECT store.store_id store_id,
       date_part('year', rental_date) AS years,
       date_part('month', rental_date) AS months,
       count(*) counts
FROM rental
JOIN staff ON rental.staff_id = staff.staff_id
JOIN store ON staff.store_id = store.store_id
GROUP BY 3,
         2,
         1
ORDER BY counts DESC;