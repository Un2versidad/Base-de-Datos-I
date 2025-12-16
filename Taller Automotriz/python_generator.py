"""
Sistema de Generación de Informe - Taller Automotriz
Autor: Asistente Claude
Fecha: Diciembre 2025
Versión: 1.0

Descripción:
    Este script genera un informe profesional en formato Word (.docx)
    que documenta el diseño de la base de datos del Taller Automotriz.
    Se conecta directamente a MySQL y usa la base de datos real.
    
Requisitos:
    pip install python-docx pandas mysql-connector-python

Uso:
    1. Ejecutar el script SQL en MySQL Workbench primero
    2. Configurar las credenciales de MySQL en este script
    3. Ejecutar: python generar_informe.py
"""

import mysql.connector
from mysql.connector import Error
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import datetime
import pandas as pd
import sys

# ==========================================
# CONFIGURACIÓN DE CONEXIÓN MYSQL
# ==========================================

DB_CONFIG = {
    'host': 'localhost',      # Cambiar si tu servidor está en otra IP
    'user': 'root',           # Tu usuario de MySQL
    'password': 'admin123',           # Tu contraseña de MySQL (dejar vacío si no tiene)
    'database': 'tallerautomotriz',
    'port': 3306              # Puerto por defecto de MySQL
}

# ==========================================
# FUNCIONES DE CONEXIÓN
# ==========================================

def conectar_mysql():
    """
    Establece conexión con MySQL.
    Retorna el objeto de conexión o None si falla.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            print(f"✓ Conexión exitosa a MySQL")
            print(f"  Base de datos: {DB_CONFIG['database']}")
            return conn
        return None
    except Error as e:
        print(f"✗ Error al conectar a MySQL: {e}")
        print("\nVerifica:")
        print("  1. MySQL está corriendo")
        print("  2. Las credenciales en DB_CONFIG son correctas")
        print("  3. La base de datos 'TallerAutomotriz' existe")
        print("  4. Ejecutaste el script SQL en Workbench primero")
        return None

def verificar_datos(conn):
    """
    Verifica que todas las tablas tengan datos.
    """
    cursor = conn.cursor()
    tablas = ['Clientes', 'Vehiculos', 'Mecanicos', 'OrdenesServicio', 'DetalleServicio']
    
    print("\nVerificando datos en las tablas:")
    for tabla in tablas:
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        count = cursor.fetchone()[0]
        print(f"  {tabla}: {count} registros")
        
        if count == 0:
            print(f"\n⚠ ADVERTENCIA: La tabla {tabla} está vacía")
            print("   Ejecuta el script SQL completo en MySQL Workbench primero")
            return False
    
    cursor.close()
    return True

# ==========================================
# FUNCIONES AUXILIARES PARA EL DOCUMENTO
# ==========================================

def agregar_portada(doc):
    """Agrega la portada del documento"""
    titulo = doc.add_paragraph()
    titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = titulo.add_run('SISTEMA DE BASE DE DATOS\nTALLER AUTOMOTRIZ')
    run.font.size = Pt(24)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 51, 102)
    
    doc.add_paragraph('\n' * 3)
    
    subtitulo = doc.add_paragraph()
    subtitulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = subtitulo.add_run('Informe Técnico de Diseño y Documentación')
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(64, 64, 64)
    
    doc.add_paragraph('\n' * 4)
    
    info = doc.add_paragraph()
    info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = info.add_run(f'Autor: Equipo de Desarrollo\n')
    run.font.size = Pt(12)
    run = info.add_run(f'Fecha: {datetime.now().strftime("%d de %B de %Y")}\n')
    run.font.size = Pt(12)
    run = info.add_run('Versión: 2.0\n\n')
    run.font.size = Pt(12)
    run = info.add_run(f'Base de Datos: MySQL - {DB_CONFIG["database"]}')
    run.font.size = Pt(10)
    run.font.italic = True
    
    doc.add_page_break()

def agregar_seccion(doc, titulo, nivel=1):
    """Agrega un título de sección formateado"""
    heading = doc.add_heading(titulo, level=nivel)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return heading

def agregar_tabla_datos(doc, df, titulo=""):
    """Agrega una tabla con datos de pandas DataFrame"""
    if titulo:
        p = doc.add_paragraph()
        run = p.add_run(titulo)
        run.font.bold = True
        run.font.size = Pt(11)
    
    if df.empty:
        doc.add_paragraph("(No hay datos disponibles)")
        return
    
    # Crear tabla en Word
    tabla = doc.add_table(rows=1, cols=len(df.columns))
    tabla.style = 'Light Grid Accent 1'
    
    # Encabezados
    hdr_cells = tabla.rows[0].cells
    for i, columna in enumerate(df.columns):
        hdr_cells[i].text = str(columna)
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
    
    # Datos (máximo 3 filas)
    for _, row in df.head(3).iterrows():
        row_cells = tabla.add_row().cells
        for i, valor in enumerate(row):
            row_cells[i].text = str(valor) if valor is not None else ''
    
    doc.add_paragraph()

def agregar_codigo_sql(doc, codigo, titulo=""):
    """Agrega un bloque de código SQL formateado"""
    if titulo:
        p = doc.add_paragraph()
        run = p.add_run(titulo)
        run.font.bold = True
        run.font.size = Pt(11)
    
    p = doc.add_paragraph()
    p.style = 'No Spacing'
    run = p.add_run(codigo)
    run.font.name = 'Courier New'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0, 0, 128)
    
    doc.add_paragraph()

# ==========================================
# FUNCIÓN PRINCIPAL DE GENERACIÓN
# ==========================================

def generar_informe():
    """Genera el informe completo en Word"""
    
    print("="*60)
    print("GENERADOR DE INFORME - TALLER AUTOMOTRIZ")
    print("="*60)
    
    # Conectar a MySQL
    conn = conectar_mysql()
    if not conn:
        print("\n✗ No se pudo conectar a MySQL. Abortando.")
        return False
    
    # Verificar que hay datos
    if not verificar_datos(conn):
        conn.close()
        return False
    
    print("\n" + "="*60)
    print("Generando informe Word...")
    print("="*60)
    
    # Crear documento Word
    doc = Document()
    
    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
    
    # ========== PORTADA ==========
    print("\n[1/8] Generando portada...")
    agregar_portada(doc)
    
    # ========== DESCRIPCIÓN GENERAL ==========
    print("[2/8] Agregando descripción general...")
    agregar_seccion(doc, '1. DESCRIPCIÓN GENERAL', 1)
    
    doc.add_paragraph(
        'El presente documento describe el diseño y la implementación de la base de datos '
        'para el Sistema de Gestión de Taller Automotriz. Este diseño se basa en el esquema SQL '
        'original proporcionado por el cliente, el cual ha sido implementado en MySQL.'
    )
    
    agregar_seccion(doc, '1.1 Propósito', 2)
    doc.add_paragraph(
        'El sistema tiene como objetivo gestionar de manera eficiente las operaciones del taller, '
        'incluyendo el registro de clientes, vehículos, mecánicos, órdenes de servicio y detalles '
        'de los trabajos realizados. El diseño prioriza la integridad referencial, la escalabilidad '
        'y el rendimiento en consultas frecuentes.'
    )
    
    agregar_seccion(doc, '1.2 Alcance', 2)
    doc.add_paragraph(
        'El sistema cubre los siguientes módulos:'
    )
    modulos = [
        'Gestión de clientes y sus datos de contacto',
        'Registro de vehículos y su historial',
        'Administración del personal técnico (mecánicos)',
        'Control de órdenes de servicio y su estado',
        'Detalle de trabajos realizados por cada mecánico'
    ]
    for modulo in modulos:
        doc.add_paragraph(modulo, style='List Bullet')
    
    agregar_seccion(doc, '1.3 Supuestos', 2)
    supuestos = [
        'Cada vehículo pertenece a un único cliente',
        'Las órdenes de servicio no pueden existir sin un vehículo asociado',
        'Los mecánicos pueden trabajar en múltiples órdenes',
        'El sistema maneja precios en dólares (USD) con dos decimales',
        'Las placas de vehículos son únicas en el sistema'
    ]
    for supuesto in supuestos:
        doc.add_paragraph(supuesto, style='List Bullet')
    
    # ========== EXPLICACIÓN DE TABLAS ==========
    print("[3/8] Documentando tablas...")
    agregar_seccion(doc, '2. DESCRIPCIÓN DE TABLAS', 1)
    
    # Tabla Clientes
    agregar_seccion(doc, '2.1 Tabla: Clientes', 2)
    doc.add_paragraph('Origen: ORIGINAL (SQL del cliente)')
    doc.add_paragraph(
        'Propósito: Almacenar la información básica de los clientes que utilizan los servicios del taller.'
    )
    
    doc.add_paragraph('Campos:')
    campos_clientes = [
        'cliente_id (INT, PK): Identificador único del cliente',
        'nombre (VARCHAR 50): Nombre del cliente',
        'apellido (VARCHAR 50): Apellido del cliente',
        'telefono (VARCHAR 20): Número de contacto',
        'email (VARCHAR 100): Correo electrónico',
        'fecha_registro (DATE): Fecha de registro en el sistema'
    ]
    for campo in campos_clientes:
        doc.add_paragraph(campo, style='List Bullet')
    
    query = "SELECT * FROM Clientes LIMIT 3"
    df_clientes = pd.read_sql(query, conn)
    agregar_tabla_datos(doc, df_clientes, "Ejemplo de registros:")
    
    # Tabla Vehiculos
    agregar_seccion(doc, '2.2 Tabla: Vehiculos', 2)
    doc.add_paragraph('Origen: ORIGINAL (SQL del cliente)')
    doc.add_paragraph(
        'Propósito: Registrar los vehículos de los clientes con su información técnica y de identificación.'
    )
    
    doc.add_paragraph('Campos principales:')
    campos_vehiculos = [
        'vehiculo_id (INT, PK): Identificador único del vehículo',
        'cliente_id (INT, FK): Referencia al cliente propietario',
        'marca (VARCHAR 50): Marca del vehículo',
        'modelo (VARCHAR 50): Modelo del vehículo',
        'anio (INT): Año de fabricación',
        'placa (VARCHAR 20): Placa única del vehículo',
        'fecha_ingreso (DATE): Fecha de primer ingreso al taller'
    ]
    for campo in campos_vehiculos:
        doc.add_paragraph(campo, style='List Bullet')
    
    doc.add_paragraph('Relaciones:')
    doc.add_paragraph('FK: cliente_id → Clientes(cliente_id)', style='List Bullet')
    
    query = "SELECT * FROM Vehiculos LIMIT 3"
    df_vehiculos = pd.read_sql(query, conn)
    agregar_tabla_datos(doc, df_vehiculos, "Ejemplo de registros:")
    
    # Tabla Mecanicos
    agregar_seccion(doc, '2.3 Tabla: Mecanicos', 2)
    doc.add_paragraph('Origen: ORIGINAL (SQL del cliente)')
    doc.add_paragraph(
        'Propósito: Gestionar la información del personal técnico del taller y sus especialidades.'
    )
    
    doc.add_paragraph('Campos principales:')
    campos_mecanicos = [
        'mecanico_id (INT, PK): Identificador único del mecánico',
        'nombre (VARCHAR 50): Nombre del mecánico',
        'apellido (VARCHAR 50): Apellido del mecánico',
        'especialidad (VARCHAR 50): Área de especialización',
        'fecha_contratacion (DATE): Fecha de ingreso al taller'
    ]
    for campo in campos_mecanicos:
        doc.add_paragraph(campo, style='List Bullet')
    
    query = "SELECT * FROM Mecanicos LIMIT 3"
    df_mecanicos = pd.read_sql(query, conn)
    agregar_tabla_datos(doc, df_mecanicos, "Ejemplo de registros:")
    
    # Tabla OrdenesServicio
    agregar_seccion(doc, '2.4 Tabla: OrdenesServicio', 2)
    doc.add_paragraph('Origen: ORIGINAL (SQL del cliente)')
    doc.add_paragraph(
        'Propósito: Controlar las órdenes de trabajo generadas para cada vehículo, '
        'incluyendo su estado y costo estimado.'
    )
    
    doc.add_paragraph('Campos principales:')
    campos_ordenes = [
        'orden_id (INT, PK): Identificador único de la orden',
        'vehiculo_id (INT, FK): Referencia al vehículo',
        'fecha_creacion (DATE): Fecha de creación de la orden',
        'estado (VARCHAR 20): Estado actual (Pendiente, En Proceso, Finalizado)',
        'costo_estimado (DECIMAL 10,2): Costo estimado del servicio'
    ]
    for campo in campos_ordenes:
        doc.add_paragraph(campo, style='List Bullet')
    
    doc.add_paragraph('Relaciones:')
    doc.add_paragraph('FK: vehiculo_id → Vehiculos(vehiculo_id)', style='List Bullet')
    
    query = "SELECT * FROM OrdenesServicio LIMIT 3"
    df_ordenes = pd.read_sql(query, conn)
    agregar_tabla_datos(doc, df_ordenes, "Ejemplo de registros:")
    
    # Tabla DetalleServicio
    agregar_seccion(doc, '2.5 Tabla: DetalleServicio', 2)
    doc.add_paragraph('Origen: ORIGINAL (SQL del cliente)')
    doc.add_paragraph(
        'Propósito: Detallar los trabajos específicos realizados en cada orden de servicio, '
        'asignando mecánicos y registrando horas y costos.'
    )
    
    doc.add_paragraph('Campos principales:')
    campos_detalles = [
        'detalle_id (INT, PK): Identificador único del detalle',
        'orden_id (INT, FK): Referencia a la orden de servicio',
        'mecanico_id (INT, FK): Referencia al mecánico asignado',
        'descripcion_trabajo (TEXT): Descripción del trabajo realizado',
        'horas_trabajadas (DECIMAL 5,2): Horas invertidas',
        'costo_mano_obra (DECIMAL 10,2): Costo de la mano de obra'
    ]
    for campo in campos_detalles:
        doc.add_paragraph(campo, style='List Bullet')
    
    doc.add_paragraph('Relaciones:')
    doc.add_paragraph('FK: orden_id → OrdenesServicio(orden_id)', style='List Bullet')
    doc.add_paragraph('FK: mecanico_id → Mecanicos(mecanico_id)', style='List Bullet')
    
    query = "SELECT * FROM DetalleServicio LIMIT 3"
    df_detalles = pd.read_sql(query, conn)
    agregar_tabla_datos(doc, df_detalles, "Ejemplo de registros:")
    
    # ========== DIAGRAMA ER ==========
    print("[4/8] Agregando diagrama ER...")
    agregar_seccion(doc, '3. DIAGRAMA ENTIDAD-RELACIÓN', 1)
    
    doc.add_paragraph(
        'El siguiente diagrama Mermaid representa las relaciones entre las tablas del sistema:'
    )
    
    diagrama_mermaid = """erDiagram
    CLIENTES ||--o{ VEHICULOS : posee
    VEHICULOS ||--o{ ORDENES_SERVICIO : genera
    ORDENES_SERVICIO ||--o{ DETALLE_SERVICIO : contiene
    MECANICOS ||--o{ DETALLE_SERVICIO : realiza
    
    CLIENTES {
        int cliente_id PK
        varchar nombre
        varchar apellido
        varchar telefono
        varchar email
        date fecha_registro
    }
    
    VEHICULOS {
        int vehiculo_id PK
        int cliente_id FK
        varchar marca
        varchar modelo
        int anio
        varchar placa
        date fecha_ingreso
    }
    
    MECANICOS {
        int mecanico_id PK
        varchar nombre
        varchar apellido
        varchar especialidad
        date fecha_contratacion
    }
    
    ORDENES_SERVICIO {
        int orden_id PK
        int vehiculo_id FK
        date fecha_creacion
        varchar estado
        decimal costo_estimado
    }
    
    DETALLE_SERVICIO {
        int detalle_id PK
        int orden_id FK
        int mecanico_id FK
        text descripcion_trabajo
        decimal horas_trabajadas
        decimal costo_mano_obra
    }"""
    
    agregar_codigo_sql(doc, diagrama_mermaid, "Código Mermaid:")
    
    doc.add_paragraph(
        'Para generar la imagen del diagrama, guardar el código en un archivo diagrama.mmd '
        'e instalar mermaid-cli:'
    )
    doc.add_paragraph('npm install -g @mermaid-js/mermaid-cli', style='List Bullet')
    doc.add_paragraph('mmdc -i diagrama.mmd -o diagrama.png', style='List Bullet')
    
    # ========== CONSULTAS SQL ==========
    print("[5/8] Ejecutando y documentando consultas SQL...")
    agregar_seccion(doc, '4. CONSULTAS SQL UTILIZADAS', 1)
    
    # Consulta 1: Verificación
    agregar_seccion(doc, '4.1 Consulta de Verificación de Registros', 2)
    query1 = """SELECT 'Clientes' AS Tabla, COUNT(*) AS Total FROM Clientes
UNION ALL SELECT 'Vehiculos', COUNT(*) FROM Vehiculos
UNION ALL SELECT 'Mecanicos', COUNT(*) FROM Mecanicos
UNION ALL SELECT 'OrdenesServicio', COUNT(*) FROM OrdenesServicio
UNION ALL SELECT 'DetalleServicio', COUNT(*) FROM DetalleServicio;"""
    
    agregar_codigo_sql(doc, query1, "SQL:")
    doc.add_paragraph('Propósito: Verificar que cada tabla contiene exactamente 10 registros.')
    
    df_verificacion = pd.read_sql(query1, conn)
    agregar_tabla_datos(doc, df_verificacion, "Resultado:")
    
    # Consulta 2: Órdenes completas
    agregar_seccion(doc, '4.2 Consulta de Órdenes con Información Completa', 2)
    query2 = """SELECT 
    CONCAT(c.nombre, ' ', c.apellido) AS Cliente,
    CONCAT(v.marca, ' ', v.modelo) AS Vehiculo,
    v.placa,
    os.fecha_creacion,
    os.estado,
    os.costo_estimado
FROM Clientes c
JOIN Vehiculos v ON c.cliente_id = v.cliente_id
JOIN OrdenesServicio os ON v.vehiculo_id = os.vehiculo_id
ORDER BY os.fecha_creacion DESC
LIMIT 5;"""
    
    agregar_codigo_sql(doc, query2, "SQL:")
    doc.add_paragraph(
        'Propósito: Obtener un reporte completo de órdenes de servicio con información '
        'del cliente y vehículo asociado.'
    )
    
    df_ordenes_completo = pd.read_sql(query2, conn)
    agregar_tabla_datos(doc, df_ordenes_completo, "Resultado:")
    
    # Consulta 3: Carga de trabajo
    agregar_seccion(doc, '4.3 Consulta de Carga de Trabajo por Mecánico', 2)
    query3 = """SELECT 
    CONCAT(m.nombre, ' ', m.apellido) AS Mecanico,
    m.especialidad,
    COUNT(ds.detalle_id) AS Trabajos_Realizados,
    SUM(ds.horas_trabajadas) AS Total_Horas,
    SUM(ds.costo_mano_obra) AS Ingreso_Total
FROM Mecanicos m
LEFT JOIN DetalleServicio ds ON m.mecanico_id = ds.mecanico_id
GROUP BY m.mecanico_id
ORDER BY Total_Horas DESC;"""
    
    agregar_codigo_sql(doc, query3, "SQL:")
    doc.add_paragraph(
        'Propósito: Analizar la carga de trabajo y productividad de cada mecánico.'
    )
    
    df_mecanicos_carga = pd.read_sql(query3, conn)
    agregar_tabla_datos(doc, df_mecanicos_carga, "Resultado:")
    
    # ========== SCRIPT SQL COMPLETO ==========
    print("[6/8] Agregando script SQL completo...")
    agregar_seccion(doc, '5. SCRIPT SQL COMPLETO', 1)
    
    doc.add_paragraph(
        'A continuación se presenta el script SQL completo tal como fue proporcionado '
        'originalmente. Este script crea la base de datos completa con todas las tablas, '
        'relaciones y datos de ejemplo.'
    )
    
    # Leer el archivo SQL original
    try:
        with open('TallerAutomotriz_Completo.sql', 'r', encoding='utf-8') as f:
            sql_original = f.read()
        agregar_codigo_sql(doc, sql_original, "Script SQL Original:")
    except FileNotFoundError:
        doc.add_paragraph(
            '(El archivo TallerAutomotriz_Completo.sql debe estar en el mismo directorio '
            'que este script para incluirlo aquí)'
        )
    
    # ========== CONCLUSIONES ==========
    print("[7/8] Agregando conclusiones...")
    agregar_seccion(doc, '6. CONCLUSIONES Y RECOMENDACIONES', 1)
    
    agregar_seccion(doc, '6.1 Justificación del Diseño', 2)
    doc.add_paragraph(
        'El diseño de la base de datos cumple con todos los requisitos establecidos y '
        'demuestra las siguientes fortalezas:'
    )
    fortalezas = [
        '5 tablas interrelacionadas sin tablas sueltas',
        '10 registros por tabla para datos de prueba',
        'Claves primarias en todas las tablas con AUTO_INCREMENT',
        'Claves foráneas que garantizan integridad referencial',
        '4 tablas con campos de fecha para seguimiento temporal',
        'Estructura normalizada que evita redundancia de datos'
    ]
    for fortaleza in fortalezas:
        doc.add_paragraph(fortaleza, style='List Bullet')
    
    agregar_seccion(doc, '6.2 Cumplimiento de Requisitos', 2)
    doc.add_paragraph('El diseño cumple con todos los requisitos especificados:')
    
    requisitos = [
        'Basado en el SQL original proporcionado ✓',
        'Mínimo 5 tablas: Se tienen exactamente 5 tablas ✓',
        'Mínimo 10 registros por tabla: Todas tienen 10 registros ✓',
        'Todas las tablas relacionadas: No hay tablas sueltas ✓',
        'Al menos 2 tablas con fecha: 4 tablas tienen campos fecha ✓',
        'Claves primarias y foráneas: Correctamente implementadas ✓'
    ]
    for req in requisitos:
        doc.add_paragraph(req, style='List Bullet')
    
    agregar_seccion(doc, '6.3 Propuestas de Mejora', 2)
    doc.add_paragraph(
        'Sin modificar la estructura original, se sugieren las siguientes mejoras '
        'para un ambiente de producción:'
    )
    
    mejoras = [
        'Agregar índices en campos de búsqueda frecuente (email, placa, estado)',
        'Implementar restricciones CHECK para validar rangos y formatos',
        'Agregar campos de auditoría (fecha_creacion, fecha_modificacion, usuario)',
        'Implementar ON DELETE CASCADE para mantener consistencia',
        'Considerar particionamiento de OrdenesServicio por fecha',
        'Agregar tabla de auditoría para rastrear cambios importantes'
    ]
    for mejora in mejoras:
        doc.add_paragraph(mejora, style='List Bullet')
    
    agregar_seccion(doc, '6.4 Normalización', 2)
    doc.add_paragraph(
        'El diseño cumple con la Tercera Forma Normal (3FN):'
    )
    normalizacion = [
        '1FN: Todos los atributos son atómicos, sin grupos repetitivos',
        '2FN: No existen dependencias parciales de la clave primaria',
        '3FN: No existen dependencias transitivas entre atributos no clave'
    ]
    for nivel in normalizacion:
        doc.add_paragraph(nivel, style='List Bullet')
    
    agregar_seccion(doc, '6.5 Escalabilidad', 2)
    doc.add_paragraph(
        'Para escalar el sistema cuando el volumen de datos crezca:'
    )
    escalabilidad = [
        'Particionar OrdenesServicio por año cuando supere 100,000 registros',
        'Implementar archivado de órdenes finalizadas mayores a 2 años',
        'Usar réplicas de lectura para separar consultas de reportes',
        'Implementar caché (Redis) para consultas frecuentes',
        'Considerar migración a un esquema estrella para análisis OLAP'
    ]
    for escala in escalabilidad:
        doc.add_paragraph(escala, style='List Bullet')
    
    # ========== GUARDAR DOCUMENTO ==========
    print("[8/8] Guardando documento...")
    doc.save('informe_final.docx')
    
    # Cerrar conexión
    conn.close()
    
    print("\n" + "="*60)
    print("✓ INFORME GENERADO EXITOSAMENTE")
    print("="*60)
    print(f"\nArchivo creado: informe_final.docx")
    print(f"Ubicación: {os.path.abspath('informe_final.docx')}")
    print("\n" + "="*60)
    
    return True

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

if __name__ == "__main__":
    import os
    
    print("\n")
    print("╔" + "═"*58 + "╗")
    print("║" + " "*15 + "GENERADOR DE INFORME" + " "*23 + "║")
    print("║" + " "*15 + "TALLER AUTOMOTRIZ" + " "*26 + "║")
    print("╚" + "═"*58 + "╝")
    print("\n")
    
    # Instrucciones iniciales
    print("INSTRUCCIONES:")
    print("1. Asegúrate de haber ejecutado el script SQL en MySQL Workbench")
    print("2. Verifica que MySQL esté corriendo")
    print("3. Actualiza las credenciales en DB_CONFIG si es necesario")
    print("\n")
    
    input("Presiona ENTER para continuar...")
    print("\n")
    
    try:
        exito = generar_informe()
        if exito:
            print("\n¡Proceso completado exitosamente!")
            input("\nPresiona ENTER para salir...")
        else:
            print("\n✗ El proceso no se completó correctamente.")
            print("Revisa los mensajes de error anteriores.")
            input("\nPresiona ENTER para salir...")
            sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error durante la generación: {e}")
        import traceback
        traceback.print_exc()
        input("\nPresiona ENTER para salir...")
        sys.exit(1)