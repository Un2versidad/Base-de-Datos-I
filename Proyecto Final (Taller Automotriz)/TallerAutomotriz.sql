-- CREAR EL SCHEMA

DROP DATABASE IF EXISTS TallerAutomotriz;
CREATE DATABASE TallerAutomotriz;
USE TallerAutomotriz;

-- BORRAR TABLAS SI EXISTEN (Por Seguridad)

DROP TABLE IF EXISTS DetalleServicio;
DROP TABLE IF EXISTS OrdenesServicio;
DROP TABLE IF EXISTS Mecanicos;
DROP TABLE IF EXISTS Vehiculos;
DROP TABLE IF EXISTS Clientes;

-- CREACIÓN DE TABLAS

CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_registro DATE
);

CREATE TABLE Vehiculos (
    vehiculo_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    anio INT,
    placa VARCHAR(20),
    fecha_ingreso DATE,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);

CREATE TABLE Mecanicos (
    mecanico_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    especialidad VARCHAR(50),
    fecha_contratacion DATE
);

CREATE TABLE OrdenesServicio (
    orden_id INT PRIMARY KEY AUTO_INCREMENT,
    vehiculo_id INT,
    fecha_creacion DATE,
    estado VARCHAR(20),
    costo_estimado DECIMAL(10,2),
    FOREIGN KEY (vehiculo_id) REFERENCES Vehiculos(vehiculo_id)
);

CREATE TABLE DetalleServicio (
    detalle_id INT PRIMARY KEY AUTO_INCREMENT,
    orden_id INT,
    mecanico_id INT,
    descripcion_trabajo TEXT,
    horas_trabajadas DECIMAL(5,2),
    costo_mano_obra DECIMAL(10,2),
    FOREIGN KEY (orden_id) REFERENCES OrdenesServicio(orden_id),
    FOREIGN KEY (mecanico_id) REFERENCES Mecanicos(mecanico_id)
);

-- INSERTS

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
('Mario','Castillo','Geneclientesdetalleservicioral','2023-05-01');

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