-- =========================================
-- PREGUNTA 1 - Total de órdenes por cliente
-- =========================================
SELECT 
    customerNumber,
    COUNT(orderNumber) AS total_ordenes
FROM orders
GROUP BY customerNumber;

-- =========================================
-- PREGUNTA 2 - Ventas totales por producto
-- =========================================
SELECT 
    productCode,
    SUM(quantityOrdered * priceEach) AS total_vendido
FROM orderdetails
GROUP BY productCode;

-- =========================================
-- PREGUNTA 3 - Total de clientes por ciudad
-- =========================================
SELECT 
    city,
    COUNT(customerNumber) AS total_clientes
FROM customers
GROUP BY city;

-- =========================================
-- PREGUNTA 4 - Promedio de pagos por año
-- =========================================
SELECT 
    YEAR(paymentDate) AS anio,
    AVG(amount) AS promedio_pago
FROM payments
GROUP BY YEAR(paymentDate);

-- =========================================
-- PREGUNTA 5 - Número de empleados por oficina
-- =========================================
SELECT 
    officeCode,
    COUNT(employeeNumber) AS total_empleados
FROM employees
GROUP BY officeCode;
