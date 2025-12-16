-- =========================================
-- SISTEMA DE BASE DE DATOS - TALLER AUTOMOTRIZ
-- =========================================
-- VERSIÓN: 2.0
-- FECHA: Diciembre 2025
-- NOTAS: Basado en el SQL original del cliente
--        con mejoras en índices y restricciones
-- =========================================

-- =========================================
-- CREAR SCHEMA DESDE CERO
-- =========================================
DROP DATABASE IF EXISTS TallerAutomotriz;
CREATE DATABASE TallerAutomotriz;
USE TallerAutomotriz;

-- =========================================
-- BORRAR TABLAS SI EXISTEN (POR SEGURIDAD)
-- =========================================
DROP TABLE IF EXISTS DetalleServicio;
DROP TABLE IF EXISTS OrdenesServicio;
DROP TABLE IF EXISTS Mecanicos;
DROP TABLE IF EXISTS Vehiculos;
DROP TABLE IF EXISTS Clientes;

-- =========================================
-- CREACIÓN DE TABLAS
-- =========================================

-- TABLA: Clientes
-- ORIGEN: ORIGINAL (sin cambios estructurales)
-- PROPÓSITO: Almacenar información de los clientes del taller
CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    fecha_registro DATE NOT NULL,
    -- AÑADIDO: Restricción para validar email
    CONSTRAINT chk_email CHECK (email LIKE '%@%')
);

-- TABLA: Vehiculos
-- ORIGEN: ORIGINAL (sin cambios estructurales)
-- PROPÓSITO: Registrar los vehículos de los clientes
CREATE TABLE Vehiculos (
    vehiculo_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio INT NOT NULL,
    placa VARCHAR(20) UNIQUE NOT NULL,
    fecha_ingreso DATE NOT NULL,
    -- AÑADIDO: Restricción para validar año del vehículo
    CONSTRAINT chk_anio CHECK (anio >= 1900 AND anio <= YEAR(CURDATE()) + 1),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id) ON DELETE CASCADE
);

-- TABLA: Mecanicos
-- ORIGEN: ORIGINAL (sin cambios estructurales)
-- PROPÓSITO: Gestionar el personal técnico del taller
CREATE TABLE Mecanicos (
    mecanico_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    especialidad VARCHAR(50) NOT NULL,
    fecha_contratacion DATE NOT NULL
);

-- TABLA: OrdenesServicio
-- ORIGEN: ORIGINAL (sin cambios estructurales)
-- PROPÓSITO: Controlar las órdenes de trabajo del taller
CREATE TABLE OrdenesServicio (
    orden_id INT PRIMARY KEY AUTO_INCREMENT,
    vehiculo_id INT NOT NULL,
    fecha_creacion DATE NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
    costo_estimado DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    -- AÑADIDO: Restricción para estados válidos
    CONSTRAINT chk_estado CHECK (estado IN ('Pendiente', 'En Proceso', 'Finalizado', 'Cancelado')),
    -- AÑADIDO: Restricción para costos positivos
    CONSTRAINT chk_costo CHECK (costo_estimado >= 0),
    FOREIGN KEY (vehiculo_id) REFERENCES Vehiculos(vehiculo_id) ON DELETE CASCADE
);

-- TABLA: DetalleServicio
-- ORIGEN: ORIGINAL (sin cambios estructurales)
-- PROPÓSITO: Detallar los trabajos realizados en cada orden de servicio
CREATE TABLE DetalleServicio (
    detalle_id INT PRIMARY KEY AUTO_INCREMENT,
    orden_id INT NOT NULL,
    mecanico_id INT NOT NULL,
    descripcion_trabajo TEXT NOT NULL,
    horas_trabajadas DECIMAL(5,2) NOT NULL DEFAULT 0.00,
    costo_mano_obra DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    -- AÑADIDO: Restricción para horas y costos positivos
    CONSTRAINT chk_horas CHECK (horas_trabajadas >= 0),
    CONSTRAINT chk_costo_mano_obra CHECK (costo_mano_obra >= 0),
    FOREIGN KEY (orden_id) REFERENCES OrdenesServicio(orden_id) ON DELETE CASCADE,
    FOREIGN KEY (mecanico_id) REFERENCES Mecanicos(mecanico_id) ON DELETE RESTRICT
);

-- =========================================
-- ÍNDICES PARA OPTIMIZACIÓN
-- ORIGEN: AÑADIDO (mejora de rendimiento)
-- =========================================

-- Índices en campos de búsqueda frecuente
CREATE INDEX idx_cliente_email ON Clientes(email);
CREATE INDEX idx_vehiculo_placa ON Vehiculos(placa);
CREATE INDEX idx_vehiculo_cliente ON Vehiculos(cliente_id);
CREATE INDEX idx_orden_vehiculo ON OrdenesServicio(vehiculo_id);
CREATE INDEX idx_orden_estado ON OrdenesServicio(estado);
CREATE INDEX idx_orden_fecha ON OrdenesServicio(fecha_creacion);
CREATE INDEX idx_detalle_orden ON DetalleServicio(orden_id);
CREATE INDEX idx_detalle_mecanico ON DetalleServicio(mecanico_id);

-- =========================================
-- INSERTS (10 registros por tabla)
-- ORIGEN: ORIGINAL (datos del cliente)
-- =========================================

INSERT INTO Clientes (nombre, apellido, telefono, email, fecha_registro) VALUES
('Carlos','Gomez','6001-0001','carlos@gmail.com','2024-01-10'),
('Ana','Lopez','6001-0002','ana@gmail.com','2024-01-12'),
('Pedro','Martinez','6001-0003','pedro@gmail.com','2024-01-15'),
('Laura','Hernandez','6001-0004','laura@gmail.com','2024-01-18'),
('Mario','Diaz','6001-0005','mario@gmail.com','2024-02-01'),
('Sofia','Vargas','6001-0006','sofia@gmail.com','2024-02-05'),
('Daniel','Rios','6001-0007','daniel@gmail.com','2024-02-10'),
('Lucia','Morales','6001-0008','lucia@gmail.com','2024-02-14'),
('Jose','Paredes','6001-0009','jose@gmail.com','2024-02-20'),
('Karla','Santos','6001-0010','karla@gmail.com','2024-02-22');

INSERT INTO Vehiculos (cliente_id, marca, modelo, anio, placa, fecha_ingreso) VALUES
(1,'Toyota','Corolla',2015,'ABC123','2024-03-01'),
(2,'Honda','Civic',2018,'XYZ789','2024-03-02'),
(3,'Nissan','Sentra',2016,'TYU456','2024-03-03'),
(4,'Ford','Focus',2017,'HJK321','2024-03-04'),
(5,'Hyundai','Elantra',2019,'QWE987','2024-03-05'),
(6,'Kia','Rio',2014,'KLO852','2024-03-06'),
(7,'Mazda','3',2020,'PLM741','2024-03-07'),
(8,'Chevrolet','Spark',2013,'UJN951','2024-03-08'),
(9,'BMW','320i',2021,'RFT258','2024-03-09'),
(10,'Audi','A3',2022,'VBG369','2024-03-10');

INSERT INTO Mecanicos (nombre, apellido, especialidad, fecha_contratacion) VALUES
('Luis','Castro','Motor','2023-01-10'),
('Miguel','Soto','Frenos','2023-01-12'),
('Jose','Guerra','Transmisión','2023-01-15'),
('Alberto','Mena','Eléctrica','2023-02-01'),
('Raul','Quiroz','Suspensión','2023-02-10'),
('David','Lara','Motor','2023-03-05'),
('Rene','Acosta','Alineación','2023-03-10'),
('Oscar','Vega','Frenos','2023-04-02'),
('Edgar','Perez','Transmisión','2023-04-15'),
('Mario','Castillo','General','2023-05-01');

INSERT INTO OrdenesServicio (vehiculo_id, fecha_creacion, estado, costo_estimado) VALUES
(1,'2024-03-05','Pendiente',150.00),
(2,'2024-03-06','En Proceso',200.00),
(3,'2024-03-07','Finalizado',300.00),
(4,'2024-03-08','Pendiente',180.00),
(5,'2024-03-09','En Proceso',250.00),
(6,'2024-03-10','Finalizado',400.00),
(7,'2024-03-11','Pendiente',120.00),
(8,'2024-03-12','En Proceso',220.00),
(9,'2024-03-13','Finalizado',500.00),
(10,'2024-03-14','Pendiente',350.00);

INSERT INTO DetalleServicio (orden_id, mecanico_id, descripcion_trabajo, horas_trabajadas, costo_mano_obra) VALUES
(1,1,'Cambio de aceite',1.5,30),
(2,2,'Revisión de frenos',2,50),
(3,3,'Reparación de transmisión',3.5,120),
(4,4,'Diagnóstico eléctrico',1,40),
(5,5,'Suspensión delantera',2.5,90),
(6,6,'Afinamiento de motor',2,80),
(7,7,'Alineación y balanceo',1.5,45),
(8,8,'Cambio de pastillas',1,35),
(9,9,'Ajustes de transmisión',3,110),
(10,10,'Revisión general',2,60);

-- =========================================
-- CONSULTAS DE VERIFICACIÓN
-- ORIGEN: AÑADIDO (para validación del informe)
-- =========================================

-- Verificar conteo de registros por tabla
SELECT 'Clientes' AS Tabla, COUNT(*) AS Total FROM Clientes
UNION ALL
SELECT 'Vehiculos', COUNT(*) FROM Vehiculos
UNION ALL
SELECT 'Mecanicos', COUNT(*) FROM Mecanicos
UNION ALL
SELECT 'OrdenesServicio', COUNT(*) FROM OrdenesServicio
UNION ALL
SELECT 'DetalleServicio', COUNT(*) FROM DetalleServicio;

-- Consulta de ejemplo con JOIN
SELECT 
    c.nombre AS Cliente,
    c.apellido,
    v.marca,
    v.modelo,
    v.placa,
    os.fecha_creacion,
    os.estado,
    os.costo_estimado
FROM Clientes c
JOIN Vehiculos v ON c.cliente_id = v.cliente_id
JOIN OrdenesServicio os ON v.vehiculo_id = os.vehiculo_id
ORDER BY os.fecha_creacion DESC
LIMIT 10;