-- 1. Lista de clientes (nombre y código) cuyo código sea mayor a 205 y menor o igual a 300

SELECT customerNumber AS codigo_cliente, customerName AS nombre_cliente

FROM customers

WHERE customerNumber > 205 AND customerNumber <= 300;



-- 2. Lista de empleados con su nombre completo y correo que solo sean representantes de ventas

SELECT jobTitle, CONCAT(firstName, ' ', lastName) AS nombre_completo, email

FROM employees

WHERE jobTitle = 'Sales Rep';



-- 3. Códigos de orden y fecha que se ordenó de los pedidos cancelados

SELECT status, orderNumber AS codigo_orden, orderDate AS fecha_orden

FROM orders

WHERE status = 'Cancelled';



-- 4. Códigos de los pedidos entregados que se solicitaron en el 2004

SELECT shippedDate, status, orderNumber AS codigo_pedido

FROM orders

WHERE status = 'Shipped' AND YEAR(orderDate) = 2004;