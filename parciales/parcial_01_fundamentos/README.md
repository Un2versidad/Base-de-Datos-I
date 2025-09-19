# Parcial 1: Fundamentos de Base de Datos

## 📋 Información General
- **Evaluación**: Primer Parcial
- **Tema**: Fundamentos y Modelo Entidad-Relación
- **Duración**: 2 horas
- **Valor**: 30% del primer corte
- **Modalidad**: Presencial - individual

## 🎯 Competencias a Evaluar
- Comprensión de conceptos fundamentales de BD
- Identificación de entidades, atributos y relaciones
- Diseño de modelos Entidad-Relación
- Aplicación de cardinalidades y restricciones

## 📝 Estructura del Examen

### Parte I: Conceptos Teóricos (40 puntos)
**Tiempo estimado: 45 minutos**

1. **Definiciones** (10 puntos)
   - ¿Qué es un SGBD?
   - Diferencias entre datos, información y conocimiento
   - Características de un sistema de base de datos

2. **Ventajas y Desventajas** (15 puntos)
   - Ventajas de usar un SGBD vs. archivos tradicionales
   - Cuándo NO usar una base de datos
   - Roles en un sistema de base de datos

3. **Niveles de Abstracción** (15 puntos)
   - Describir los tres niveles de abstracción
   - Explicar la independencia de datos
   - Arquitectura ANSI/SPARC

### Parte II: Modelo Entidad-Relación (60 puntos)
**Tiempo estimado: 75 minutos**

#### Problema: Sistema de Hospital

Un hospital necesita un sistema para gestionar pacientes, médicos y citas médicas.

**Información a manejar:**
- **Pacientes**: número de cédula, nombre, fecha de nacimiento, dirección, teléfono, tipo de sangre
- **Médicos**: código de empleado, nombre, especialidad, teléfono, horario de atención
- **Citas**: fecha, hora, consultorio, motivo de consulta, diagnóstico, tratamiento
- **Especialidades**: código, nombre, descripción

**Reglas de negocio:**
1. Un paciente puede tener múltiples citas
2. Un médico puede atender múltiples pacientes
3. Una cita es entre un paciente y un médico específico
4. Un médico tiene una especialidad principal
5. Se debe registrar histórico de todas las citas
6. Los consultorios están numerados del 101 al 305

**Tareas:**
1. **Identificar entidades** (15 puntos)
   - Listar todas las entidades del sistema
   - Justificar por qué cada una es una entidad

2. **Definir atributos** (20 puntos)
   - Especificar atributos para cada entidad
   - Identificar llaves primarias
   - Marcar atributos obligatorios y opcionales

3. **Establecer relaciones** (25 puntos)
   - Identificar todas las relaciones
   - Determinar cardinalidades
   - Especificar restricciones de participación

## 📊 Criterios de Evaluación

| Sección | Criterio | Excelente (4) | Bueno (3) | Regular (2) | Deficiente (1) |
|---------|----------|---------------|-----------|-------------|----------------|
| Teoría | Precisión conceptual | Definiciones exactas | Definiciones buenas | Definiciones aproximadas | Definiciones incorrectas |
| E-R | Identificación de entidades | Todas correctas | Mayoría correctas | Algunas correctas | Pocas correctas |
| E-R | Atributos y llaves | Completos y apropiados | Mayoría apropiados | Algunos apropiados | Pocos apropiados |
| E-R | Relaciones y cardinalidades | Todas correctas | Mayoría correctas | Algunas correctas | Pocas correctas |

## 📚 Material de Consulta Permitido
- Una hoja de referencia personal (manuscrita)
- Calculadora básica
- **NO** se permite: libros, apuntes, dispositivos electrónicos

## ⏰ Distribución del Tiempo
- **Revisión inicial**: 5 minutos
- **Parte I**: 45 minutos
- **Parte II**: 75 minutos
- **Revisión final**: 15 minutos

## 🎯 Recomendaciones de Estudio
- Repasar talleres 1, 2 y 3
- Practicar diseño de modelos E-R
- Estudiar ejemplos de cardinalidades
- Revisar material de [recursos](../../recursos/)

## 📞 Información Adicional
- Llegar 15 minutos antes del examen
- Traer documento de identidad
- Usar lapicero azul o negro
- En caso de dudas durante el examen, levantar la mano