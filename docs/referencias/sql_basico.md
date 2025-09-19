# Comandos SQL Básicos - Referencia Rápida

## 📊 DDL (Data Definition Language)

### Crear Base de Datos
```sql
CREATE DATABASE nombre_bd;
USE nombre_bd;  -- MySQL
\c nombre_bd;   -- PostgreSQL
```

### Crear Tabla
```sql
CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INTEGER,
    email VARCHAR(150) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Modificar Tabla
```sql
-- Agregar columna
ALTER TABLE personas ADD COLUMN telefono VARCHAR(20);

-- Modificar columna
ALTER TABLE personas ALTER COLUMN telefono TYPE VARCHAR(15);

-- Eliminar columna
ALTER TABLE personas DROP COLUMN telefono;
```

### Eliminar Tabla
```sql
DROP TABLE personas;
```

## 📝 DML (Data Manipulation Language)

### Insertar Datos
```sql
-- Insertar un registro
INSERT INTO personas (nombre, apellido, edad, email) 
VALUES ('Juan', 'Pérez', 25, 'juan@email.com');

-- Insertar múltiples registros
INSERT INTO personas (nombre, apellido, edad, email) VALUES
    ('María', 'García', 30, 'maria@email.com'),
    ('Carlos', 'López', 28, 'carlos@email.com');
```

### Consultar Datos
```sql
-- Seleccionar todo
SELECT * FROM personas;

-- Seleccionar columnas específicas
SELECT nombre, apellido FROM personas;

-- Con condiciones
SELECT * FROM personas WHERE edad > 25;

-- Ordenar resultados
SELECT * FROM personas ORDER BY apellido ASC;

-- Limitar resultados
SELECT * FROM personas LIMIT 10;
```

### Actualizar Datos
```sql
-- Actualizar un registro
UPDATE personas 
SET edad = 26 
WHERE id = 1;

-- Actualizar múltiples campos
UPDATE personas 
SET edad = 31, email = 'maria_garcia@email.com' 
WHERE nombre = 'María';
```

### Eliminar Datos
```sql
-- Eliminar registro específico
DELETE FROM personas WHERE id = 1;

-- Eliminar con condición
DELETE FROM personas WHERE edad < 18;

-- Eliminar todos los registros (¡cuidado!)
DELETE FROM personas;
```

## 🔍 Consultas Avanzadas

### WHERE - Condiciones
```sql
-- Operadores de comparación
SELECT * FROM personas WHERE edad = 25;
SELECT * FROM personas WHERE edad > 25;
SELECT * FROM personas WHERE edad BETWEEN 20 AND 30;

-- Operadores lógicos
SELECT * FROM personas WHERE edad > 25 AND nombre = 'Juan';
SELECT * FROM personas WHERE edad < 20 OR edad > 60;

-- Patrones de texto
SELECT * FROM personas WHERE nombre LIKE 'J%';
SELECT * FROM personas WHERE email LIKE '%@gmail.com';

-- Valores nulos
SELECT * FROM personas WHERE telefono IS NULL;
SELECT * FROM personas WHERE telefono IS NOT NULL;
```

### Funciones Agregadas
```sql
-- Contar registros
SELECT COUNT(*) FROM personas;
SELECT COUNT(telefono) FROM personas;  -- No cuenta nulos

-- Valores máximo y mínimo
SELECT MAX(edad) FROM personas;
SELECT MIN(edad) FROM personas;

-- Promedio y suma
SELECT AVG(edad) FROM personas;
SELECT SUM(edad) FROM personas;
```

### GROUP BY y HAVING
```sql
-- Agrupar por campo
SELECT edad, COUNT(*) as cantidad 
FROM personas 
GROUP BY edad;

-- Filtrar grupos
SELECT edad, COUNT(*) as cantidad 
FROM personas 
GROUP BY edad 
HAVING COUNT(*) > 1;
```

## 🔗 JOINs

### INNER JOIN
```sql
SELECT p.nombre, c.nombre as ciudad
FROM personas p
INNER JOIN ciudades c ON p.ciudad_id = c.id;
```

### LEFT JOIN
```sql
SELECT p.nombre, c.nombre as ciudad
FROM personas p
LEFT JOIN ciudades c ON p.ciudad_id = c.id;
```

### RIGHT JOIN
```sql
SELECT p.nombre, c.nombre as ciudad
FROM personas p
RIGHT JOIN ciudades c ON p.ciudad_id = c.id;
```

## 🎯 Consejos

1. **Usa MAYÚSCULAS** para palabras clave SQL
2. **Indenta** tu código para mejor legibilidad
3. **Comenta** consultas complejas
4. **Usa alias** para nombres largos
5. **Siempre usa WHERE** en UPDATE y DELETE
6. **Prueba** en entorno de desarrollo primero