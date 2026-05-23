-- Preview Orders Table
SELECT * FROM orders
LIMIT 5;

-- Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Order Status Analysis
SELECT order_status,
COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;

-- Payment Method Analysis
SELECT payment_type,
COUNT(*) AS total_payments
FROM payments
GROUP BY payment_type;

-- Total Revenue
SELECT SUM(payment_value) AS total_revenue
FROM payments;

-- Average Payment
SELECT AVG(payment_value) AS average_payment
FROM payments;

-- Top 5 Highest Payments
SELECT order_id,
payment_type,
payment_value
FROM payments
ORDER BY payment_value DESC
LIMIT 5;

-- Delivered Orders
SELECT COUNT(*) AS delivered_orders
FROM orders
WHERE order_status = 'delivered';

-- Canceled Orders
SELECT COUNT(*) AS canceled_orders
FROM orders
WHERE order_status = 'canceled';

-- Revenue by Payment Type
SELECT payment_type,
SUM(payment_value) AS total_revenue
FROM payments
GROUP BY payment_type
ORDER BY total_revenue DESC;

-- Installment Analysis
SELECT payment_installments,
COUNT(*) AS total_orders
FROM payments
GROUP BY payment_installments
ORDER BY payment_installments DESC
LIMIT 10;