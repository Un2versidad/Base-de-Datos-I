# Sistema de Base de Datos - Taller Automotriz

## 📋 Descripción

Este proyecto contiene el diseño completo de una base de datos para un taller automotriz. Incluye el script SQL original para MySQL, código Python que genera documentación profesional en Word conectándose directamente a la base de datos MySQL, y diagramas ER.

## 📦 Contenido del Proyecto

```
taller-automotriz/
│
├── TallerAutomotriz_Completo.sql   # Script SQL original (MySQL)
├── TallerAutomotriz_Final.sql      # Script SQL con mejoras documentadas
├── generar_informe.py              # Script Python para generar Word
├── requirements.txt                # Dependencias Python
├── diagrama_er.mmd                 # Diagrama Mermaid
├── README.md                       # Este archivo
│
└── generados/
    ├── informe_final.docx          # Documento Word generado
    └── diagrama_er.png             # Imagen del diagrama (opcional)
```

## 🚀 Instalación y Uso

### Requisitos Previos

- **Python 3.8 o superior**
- **MySQL 8.0+** (instalado y corriendo)
- **MySQL Workbench** (recomendado para ejecutar el SQL)

### Paso 1: Ejecutar el Script SQL en MySQL

**Opción A: Usando MySQL Workbench (Recomendado)**

1. Abre MySQL Workbench
2. Conecta a tu servidor MySQL local
3. Abre el archivo `TallerAutomotriz_Completo.sql`
4. Ejecuta el script completo (botón ⚡ Execute)
5. Verifica que se creó la base de datos `TallerAutomotriz` con 5 tablas

**Opción B: Usando línea de comandos**

```bash
mysql -u root -p < TallerAutomotriz_Completo.sql
```

### Paso 2: Instalar Dependencias Python

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install python-docx pandas mysql-connector-python
```

### Paso 3: Configurar Credenciales MySQL

Edita el archivo `generar_informe.py` y actualiza estas líneas según tu configuración:

```python
DB_CONFIG = {
    'host': 'localhost',           # Tu servidor MySQL
    'user': 'root',                # Tu usuario MySQL
    'password': 'tu_contraseña',   # Tu contraseña MySQL
    'database': 'TallerAutomotriz',
    'port': 3306                   # Puerto MySQL (por defecto 3306)
}
```

### Paso 4: Generar el Informe Word

```bash
python generar_informe.py
```

**Esto creará:**
- ✅ `informe_final.docx` - Documento Word completo con toda la documentación

**El script verificará:**
- ✅ Conexión a MySQL
- ✅ Existencia de la base de datos
- ✅ Que todas las tablas tengan datos
- ✅ Ejecutará consultas y generará el informe

### Paso 5: Generar Imagen del Diagrama ER (Opcional)

**Instalar Mermaid CLI:**

```bash
npm install -g @mermaid-js/mermaid-cli
```

**Generar imagen:**

```bash
mmdc -i diagrama_er.mmd -o diagrama_er.png -b transparent
```

## 🔧 Solución de Problemas

### Error: "Can't connect to MySQL server"

**Soluciones:**
- Verifica que MySQL esté corriendo: `mysql --version`
- En Windows: Abre "Servicios" y verifica que "MySQL80" esté iniciado
- Verifica el puerto: Por defecto es 3306
- Verifica credenciales en `DB_CONFIG`

### Error: "Access denied for user"

**Soluciones:**
- Verifica tu usuario y contraseña en MySQL Workbench
- Actualiza `DB_CONFIG` con las credenciales correctas
- Si no tienes contraseña, deja el campo vacío: `'password': ''`

### Error: "Unknown database 'TallerAutomotriz'"

**Soluciones:**
- Ejecuta el script SQL primero en MySQL Workbench
- Verifica que se creó la base de datos: `SHOW DATABASES;`

### Error: "No module named 'mysql.connector'"

**Solución:**
```bash
pip install mysql-connector-python
```

## 📊 Estructura de la Base de Datos

### Tablas (todas del SQL original)

1. **Clientes** - Información de clientes del taller
   - 10 registros
   - Campos: cliente_id, nombre, apellido, telefono, email, fecha_registro

2. **Vehiculos** - Vehículos registrados en el sistema
   - 10 registros
   - Campos: vehiculo_id, cliente_id, marca, modelo, anio, placa, fecha_ingreso

3. **Mecanicos** - Personal técnico del taller
   - 10 registros
   - Campos: mecanico_id, nombre, apellido, especialidad, fecha_contratacion

4. **OrdenesServicio** - Órdenes de trabajo generadas
   - 10 registros
   - Campos: orden_id, vehiculo_id, fecha_creacion, estado, costo_estimado

5. **DetalleServicio** - Detalles de trabajos realizados
   - 10 registros
   - Campos: detalle_id, orden_id, mecanico_id, descripcion_trabajo, horas_trabajadas, costo_mano_obra

### Relaciones

```
Clientes (1) ──→ (N) Vehiculos
Vehiculos (1) ──→ (N) OrdenesServicio
OrdenesServicio (1) ──→ (N) DetalleServicio
Mecanicos (1) ──→ (N) DetalleServicio
```

## 📝 Contenido del Informe Word

El documento `informe_final.docx` incluye:

1. **Portada** 
   - Título profesional
   - Autor y fecha
   - Información de la base de datos

2. **Descripción General**
   - Propósito del sistema
   - Alcance y módulos
   - Supuestos del diseño

3. **Descripción de Tablas** (5 tablas)
   - Propósito de cada tabla
   - Campos con tipos de datos
   - Claves primarias y foráneas
   - 3 filas de ejemplo (datos reales de MySQL)

4. **Diagrama ER**
   - Código Mermaid completo
   - Instrucciones para generar imagen

5. **Consultas SQL**
   - Verificación de registros
   - Órdenes con información completa (JOIN)
   - Carga de trabajo por mecánico (GROUP BY)
   - Resultados con datos reales de la BD

6. **Script SQL Completo**
   - Tu script original incluido en el informe

7. **Conclusiones**
   - Justificación del diseño
   - Cumplimiento de requisitos
   - Propuestas de mejora
   - Análisis de normalización
   - Recomendaciones de escalabilidad

## 🔍 Consultas de Ejemplo

### Verificar que todo está OK

```sql
-- Ver cuántos registros hay en cada tabla
SELECT 'Clientes' AS Tabla, COUNT(*) AS Total FROM Clientes
UNION ALL SELECT 'Vehiculos', COUNT(*) FROM Vehiculos
UNION ALL SELECT 'Mecanicos', COUNT(*) FROM Mecanicos
UNION ALL SELECT 'OrdenesServicio', COUNT(*) FROM OrdenesServicio
UNION ALL SELECT 'DetalleServicio', COUNT(*) FROM DetalleServicio;
```

### Reporte Completo de Órdenes

```sql
SELECT 
    CONCAT(c.nombre, ' ', c.apellido) AS Cliente,
    CONCAT(v.marca, ' ', v.modelo) AS Vehiculo,
    v.placa,
    os.fecha_creacion,
    os.estado,
    os.costo_estimado
FROM Clientes c
JOIN Vehiculos v ON c.cliente_id = v.cliente_id
JOIN OrdenesServicio os ON v.vehiculo_id = os.vehiculo_id
ORDER BY os.fecha_creacion DESC;
```

### Productividad por Mecánico

```sql
SELECT 
    CONCAT(m.nombre, ' ', m.apellido) AS Mecanico,
    m.especialidad,
    COUNT(ds.detalle_id) AS Trabajos,
    SUM(ds.horas_trabajadas) AS Horas,
    SUM(ds.costo_mano_obra) AS Ingresos
FROM Mecanicos m
LEFT JOIN DetalleServicio ds ON m.mecanico_id = ds.mecanico_id
GROUP BY m.mecanico_id
ORDER BY Horas DESC;
```

## 🎯 Características del Diseño Original

### ✅ Cumplimiento de Requisitos

- **5 tablas relacionadas** ✓ (Clientes, Vehiculos, Mecanicos, OrdenesServicio, DetalleServicio)
- **≥10 registros por tabla** ✓ (Todas tienen exactamente 10)
- **Todas las tablas relacionadas** ✓ (Sin tablas sueltas)
- **≥2 tablas con fecha** ✓ (4 tablas tienen campos fecha)
- **Claves primarias** ✓ (Todas con AUTO_INCREMENT)
- **Claves foráneas** ✓ (Integridad referencial correcta)

### ✅ Normalización

- **1FN**: Atributos atómicos ✓
- **2FN**: Sin dependencias parciales ✓
- **3FN**: Sin dependencias transitivas ✓

### ✅ Integridad

- Claves primarias únicas
- Claves foráneas con referencias válidas
- Tipos de datos apropiados
- Campos obligatorios vs opcionales bien definidos

## 📈 Mejoras Propuestas (Opcionales)

El script SQL original es completamente funcional. Para producción se sugieren estas **mejoras opcionales** (documentadas en el archivo `TallerAutomotriz_Final.sql`):

1. **Índices** para mejorar búsquedas frecuentes
2. **Restricciones CHECK** para validar datos
3. **ON DELETE CASCADE** para mantener consistencia
4. **Campos NOT NULL** donde sea apropiado
5. **Valores DEFAULT** para campos opcionales

Todas estas mejoras están **documentadas y justificadas** en el informe generado.

## 🔐 Seguridad

**⚠️ IMPORTANTE:** El archivo `generar_informe.py` contiene credenciales de MySQL. 

**Recomendaciones:**
- No subas este archivo a GitHub con credenciales reales
- Usa variables de entorno para credenciales en producción
- Considera usar `.env` con `python-dotenv`

**Ejemplo con variables de entorno:**

```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'TallerAutomotriz'),
    'port': int(os.getenv('DB_PORT', 3306))
}
```

## 📞 Soporte

### Si el script no funciona:

1. **Verifica la conexión a MySQL:**
   ```bash
   mysql -u root -p
   USE TallerAutomotriz;
   SHOW TABLES;
   ```

2. **Verifica que Python puede conectar:**
   ```python
   import mysql.connector
   conn = mysql.connector.connect(
       host='localhost',
       user='root',
       password='tu_password'
   )
   print("Conexión exitosa!")
   ```

3. **Verifica los datos:**
   ```sql
   SELECT COUNT(*) FROM Clientes;
   ```

### Errores comunes:

| Error | Causa | Solución |
|-------|-------|----------|
| Connection refused | MySQL no está corriendo | Inicia MySQL Server |
| Access denied | Credenciales incorrectas | Verifica usuario/password |
| Unknown database | BD no existe | Ejecuta el script SQL |
| No module named | Falta librería Python | `pip install -r requirements.txt` |

## 📄 Licencia

Este proyecto es material educativo y de demostración.

---

**Versión:** 2.0  
**Última actualización:** Diciembre 2025  
**Autor:** Equipo de Desarrollo  
**Motor de BD:** MySQL 8.0+  
**Python:** 3.8+