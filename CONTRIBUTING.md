# Guía de Contribución - Base de Datos I

¡Gracias por tu interés en contribuir a este repositorio! Esta guía te ayudará a participar de manera efectiva.

## 🤝 Cómo Contribuir

### Para Estudiantes
1. **Reportar errores**: Usa GitHub Issues para reportar problemas
2. **Sugerir mejoras**: Propón nuevos ejercicios o recursos
3. **Compartir soluciones**: Contribuye con soluciones alternativas

### Para Instructores
1. **Añadir contenido**: Nuevos talleres y evaluaciones
2. **Actualizar material**: Mantener recursos actualizados
3. **Revisar contribuciones**: Validar aportes de estudiantes

## 📋 Proceso de Contribución

### 1. Fork del Repositorio
```bash
# Hacer fork desde GitHub
# Clonar tu fork
git clone https://github.com/tu-usuario/Base-de-Datos-I.git
cd Base-de-Datos-I
```

### 2. Crear una Rama
```bash
# Crear rama para tu contribución
git checkout -b feature/nombre-descriptivo
```

### 3. Realizar Cambios
- Seguir las convenciones de nomenclatura
- Documentar adecuadamente
- Probar las soluciones SQL

### 4. Commit y Push
```bash
# Agregar cambios
git add .
git commit -m "Descripción clara del cambio"
git push origin feature/nombre-descriptivo
```

### 5. Pull Request
- Describir claramente los cambios
- Referenciar issues relacionados
- Esperar revisión y feedback

## 📝 Estándares de Contribución

### Nomenclatura de Archivos
```
talleres/
├── taller_01_introduccion/
│   ├── README.md
│   ├── enunciado.md
│   └── solucion.sql
```

### Formato de Código SQL
```sql
-- Comentarios claros y descriptivos
-- Usar MAYÚSCULAS para palabras clave
-- Indentar correctamente

SELECT 
    p.nombre,
    p.apellido,
    c.nombre AS ciudad
FROM personas p
INNER JOIN ciudades c ON p.ciudad_id = c.id
WHERE p.activo = true
ORDER BY p.apellido;
```

### Documentación
- README en cada carpeta principal
- Comentarios en código complejo
- Ejemplos de uso cuando sea necesario

## 🔍 Revisión de Código

### Criterios de Aceptación
- [ ] Funcionalidad correcta
- [ ] Código bien documentado
- [ ] Seguimiento de convenciones
- [ ] Pruebas incluidas (si aplica)

### Proceso de Revisión
1. Revisión automática (linting)
2. Revisión por pares
3. Pruebas de funcionalidad
4. Aprobación final

## 🚫 Qué NO hacer

- No subir archivos binarios grandes
- No incluir información personal sensible
- No copiar código sin atribución
- No hacer commits directos a main

## 📞 Contacto

- **Issues**: Para reportes y sugerencias
- **Discusiones**: Para preguntas generales
- **Email**: [email del instructor]

## 📄 Licencia

Al contribuir, aceptas que tu trabajo se distribuya bajo la misma licencia Apache 2.0 del proyecto.