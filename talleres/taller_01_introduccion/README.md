# Taller 1: Introducción a Base de Datos

## Información General
- **Taller**: 1 - Introducción a Base de Datos
- **Tema**: Conceptos fundamentales y modelo E-R
- **Fecha de entrega**: Semana 3
- **Valor**: 5%

## Objetivos
- [ ] Comprender qué es una base de datos y un SGBD
- [ ] Identificar los componentes de un sistema de base de datos
- [ ] Diseñar un modelo Entidad-Relación básico

## Descripción del Problema

Una pequeña biblioteca universitaria necesita un sistema para gestionar sus libros, autores y préstamos. Como diseñador de bases de datos, debes crear el modelo conceptual que represente esta realidad.

### Requerimientos del Sistema

La biblioteca maneja la siguiente información:
- **Libros**: ISBN, título, año de publicación, número de páginas, editorial
- **Autores**: ID, nombre completo, fecha de nacimiento, nacionalidad
- **Usuarios**: cédula, nombre, tipo (estudiante/profesor), teléfono, email
- **Préstamos**: fecha de préstamo, fecha de devolución, estado

### Reglas de Negocio
1. Un libro puede tener múltiples autores
2. Un autor puede escribir múltiples libros
3. Un usuario puede tener múltiples préstamos
4. Un préstamo es de un solo libro para un solo usuario
5. Se debe registrar la fecha de préstamo y devolución
6. Los profesores pueden prestar libros por 30 días, los estudiantes por 15 días

## Entregables
- [ ] Diagrama Entidad-Relación en formato digital
- [ ] Descripción de entidades y atributos
- [ ] Descripción de relaciones
- [ ] Archivo README con explicación del diseño

## Criterios de Evaluación
| Criterio | Peso | Descripción |
|----------|------|-------------|
| Identificación de entidades | 25% | Entidades correctamente identificadas |
| Atributos apropiados | 25% | Atributos completos y bien definidos |
| Relaciones correctas | 30% | Relaciones y cardinalidades apropiadas |
| Documentación | 20% | Explicación clara del diseño |

## Recursos de Apoyo
- [Guía de Modelo E-R](../../docs/referencias/modelo_er.md)
- [Herramientas de diagramación](../../recursos/#herramientas-online)
- Material de clase sobre conceptos básicos

## Instrucciones de Entrega
1. Crear una carpeta: `taller_01_apellido_nombre`
2. Incluir diagrama en formato PNG o PDF
3. Agregar archivo README.md con explicaciones
4. Comprimir y subir antes de la fecha límite

## Ejemplo de Estructura de Entrega
```
taller_01_garcia_maria/
├── README.md
├── diagrama_er.png
└── descripcion_entidades.md
```

## Notas Adicionales
- Usar notación estándar para diagramas E-R
- Documentar todas las decisiones de diseño
- Consultar dudas en horarios de tutoría