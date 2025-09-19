# Guía de Instalación - Entorno de Desarrollo

Esta guía te ayudará a configurar el entorno necesario para el curso de Base de Datos I.

## 🖥️ Requisitos del Sistema

### Mínimos
- RAM: 4 GB
- Espacio en disco: 2 GB libres
- SO: Windows 10, macOS 10.14, Ubuntu 18.04 o superior

### Recomendados
- RAM: 8 GB o más
- Espacio en disco: 5 GB libres
- Conexión a internet estable

## 📦 Software Requerido

### 1. Sistema de Gestión de Base de Datos

#### PostgreSQL (Recomendado)
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# macOS (usando Homebrew)
brew install postgresql

# Windows: Descargar desde postgresql.org
```

#### MySQL (Alternativo)
```bash
# Ubuntu/Debian
sudo apt install mysql-server

# macOS (usando Homebrew)
brew install mysql

# Windows: Descargar desde mysql.com
```

### 2. Cliente de Base de Datos

#### DBeaver (Recomendado - Gratuito)
- Descargar desde: https://dbeaver.io/download/
- Compatible con múltiples SGBD
- Interfaz gráfica intuitiva

#### pgAdmin (Para PostgreSQL)
```bash
# Ubuntu/Debian
sudo apt install pgadmin4

# macOS
brew install --cask pgadmin4

# Windows: Incluido con PostgreSQL
```

### 3. Editor de Código

#### Visual Studio Code
- Descargar desde: https://code.visualstudio.com/
- Extensiones recomendadas:
  - SQLTools
  - PostgreSQL
  - Database Client

## ⚙️ Configuración Inicial

### PostgreSQL
```sql
-- Crear usuario para el curso
CREATE USER estudiante WITH PASSWORD 'password123';

-- Crear base de datos
CREATE DATABASE curso_bd1 OWNER estudiante;

-- Otorgar privilegios
GRANT ALL PRIVILEGES ON DATABASE curso_bd1 TO estudiante;
```

### Verificación de Instalación
```sql
-- Probar conexión
SELECT version();

-- Crear tabla de prueba
CREATE TABLE test (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100)
);

-- Insertar datos
INSERT INTO test (nombre) VALUES ('Prueba exitosa');

-- Consultar
SELECT * FROM test;
```

## 🌐 Herramientas Online (Alternativas)

Si no puedes instalar software localmente:

### DB Fiddle
- URL: https://www.db-fiddle.com/
- Soporta PostgreSQL, MySQL, SQLite
- No requiere instalación

### SQLiteOnline
- URL: https://sqliteonline.com/
- SQLite en el navegador
- Ideal para ejercicios básicos

## 🆘 Solución de Problemas

### PostgreSQL no inicia
```bash
# Ubuntu/Debian
sudo systemctl start postgresql
sudo systemctl enable postgresql

# macOS
brew services start postgresql
```

### Error de conexión
1. Verificar que el servicio esté corriendo
2. Comprobar usuario y contraseña
3. Revisar configuración de puerto (5432 por defecto)

### Problemas de permisos
```sql
-- Como superusuario
ALTER USER estudiante CREATEDB;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO estudiante;
```

## 📞 Soporte

Si tienes problemas con la instalación:
1. Consulta la documentación oficial
2. Busca en los foros de la comunidad
3. Contacta al instructor
4. Usa las herramientas online como alternativa temporal

## ✅ Lista de Verificación

- [ ] SGBD instalado y funcionando
- [ ] Cliente de BD configurado
- [ ] Conexión exitosa
- [ ] Tabla de prueba creada
- [ ] Editor de código instalado
- [ ] Extensiones SQL configuradas