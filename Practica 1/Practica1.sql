-- 1. Clientes con nombre completo, teléfono y país
SELECT customerName, phone, country FROM customers;

-- 2. Clientes con código de cliente entre 200 y 220
SELECT customerNumber, customerName, phone, country FROM customers WHERE customerNumber >= 200 AND customerNumber <= 220;

-- 3. Empleados representantes de ventas (nombre, apellido y correo)
SELECT firstName, lastName, email FROM employees WHERE jobTitle = "Sales Rep";

-- 4. Pedidos cancelados (código de orden y fecha)
SELECT orderNumber, orderDate, status FROM orders WHERE status = 'cancelled';

-- 5. Pedidos entregados en 2004 (códigos de orden)
SELECT orderNumber, orderDate FROM orders WHERE status = "Shipped" AND YEAR(orderDate) = 2004;