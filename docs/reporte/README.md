# Documentación del Sistema de Telemetría MQTT-PostgreSQL

Esta carpeta contiene la documentación completa del proyecto de servicio de escritura de mensajes MQTT a base de datos PostgreSQL utilizando contenedores Docker.

## Estructura de la Documentación

### Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `A0-main.tex` | Documento principal que incluye todos los capítulos |
| `A1-Portada.tex` | Portada del documento |
| `B-Intro.tex` | Introducción al proyecto |
| `C-Conceptos.tex` | Marco conceptual y fundamentos teóricos |
| `D-AnalisisYDiseno.tex` | Análisis de requisitos y diseño del sistema |
| `E-Cuenta.tex` | Implementación y detalles técnicos |
| `F-Comandos.tex` | Pruebas y validación del sistema |
| `G-Despliegue.tex` | Despliegue y configuración |
| `H-Manual.tex` | Manual de usuario |
| `I-Resultados.tex` | Resultados y evaluación del sistema |
| `J-Conclusiones.tex` | Conclusiones y trabajo futuro |
| `K-Anexos.tex` | Anexos con configuraciones y scripts |
| `O-Reference.tex` | Referencias bibliográficas |

### Contenido por Capítulos

#### 🚀 **Introducción (B-Intro)**
- Contexto del proyecto
- Objetivos generales y específicos
- Justificación técnica
- Alcance y limitaciones

#### 📚 **Conceptos (C-Conceptos)**
- MQTT y protocolos de mensajería
- Bases de datos relacionales
- Containerización con Docker
- Automatización con Makefile

#### 🏗️ **Análisis y Diseño (D-AnalisisYDiseno)**
- Análisis de requisitos
- Arquitectura del sistema
- Diseño de base de datos
- Patrones de diseño aplicados

#### ⚙️ **Implementación (E-Cuenta)**
- Estructura del proyecto
- Componentes principales
- Configuración de contenedores
- Scripts de automatización

#### 🧪 **Pruebas y Validación (F-Comandos)**
- Estrategias de testing
- Pruebas unitarias e integración
- Validación del sistema
- Automatización de pruebas

#### 🚀 **Despliegue (G-Despliegue)**
- Configuración del entorno
- Instalación y configuración
- Monitoreo del sistema
- Procedimientos de backup

#### 📖 **Manual de Usuario (H-Manual)**
- Guía de uso de pgAdmin
- Consultas comunes
- Herramientas de monitoreo
- Resolución de problemas

#### 📊 **Resultados (I-Resultados)**
- Métricas de rendimiento
- Análisis de confiabilidad
- Validación funcional
- Cumplimiento de objetivos

#### 🎯 **Conclusiones (J-Conclusiones)**
- Logros del proyecto
- Contribuciones técnicas
- Trabajo futuro
- Recomendaciones

#### 📎 **Anexos (K-Anexos)**
- Configuraciones completas
- Scripts de utilidad
- Diagramas detallados
- Comandos de troubleshooting

## Compilación de la Documentación

### Requisitos

- LaTeX completo (texlive-full recomendado)
- Python 3 con Pygments (para resaltado de sintaxis)
- Make

### Instalación de Dependencias (Ubuntu/Debian)

```bash
# Instalar LaTeX y dependencias
sudo apt-get update
sudo apt-get install texlive-full texlive-latex-extra texlive-fonts-recommended
sudo apt-get install python3-pygments

# O usar el Makefile
make install-deps
```

### Comandos de Compilación

```bash
# Ver ayuda completa
make help

# Compilación completa (recomendado)
make build

# Compilación rápida
make quick

# Compilar y abrir PDF
make view

# Limpiar archivos temporales
make clean

# Verificar sintaxis
make check

# Ver estructura de documentos
make toc
```

### Archivos Generados

La compilación genera los siguientes archivos en la carpeta `build/`:

- `MQTT_PostgreSQL_Documentation.pdf` - Documento final
- Archivos temporales (`.aux`, `.log`, `.out`, etc.)

## Características de la Documentación

### 🎨 **Estilo y Formato**
- Documento tipo libro (book class)
- Resaltado de sintaxis para código
- Tablas profesionales
- Referencias cruzadas automáticas
- Índice de contenidos navegable

### 💻 **Código y Ejemplos**
- Sintaxis resaltada con Minted
- Ejemplos de configuración reales
- Scripts completos y funcionales
- Comandos listos para usar

### 📋 **Contenido Técnico**
- Diagramas de arquitectura
- Esquemas de base de datos
- Métricas de rendimiento
- Procedimientos operacionales

### 🔗 **Referencias**
- Enlaces a documentación oficial
- Referencias académicas
- Estándares de la industria
- Recursos de aprendizaje

## Personalización

### Modificar Contenido

1. Editar los archivos `.tex` correspondientes
2. Compilar con `make build`
3. Verificar el resultado con `make view`

### Agregar Nuevas Secciones

1. Crear nuevo archivo `.tex`
2. Agregar `\include{NuevoArchivo}` en `A0-main.tex`
3. Recompilar

### Cambiar Estilos

- Modificar preámbulo en `A0-main.tex`
- Ajustar colores y fuentes
- Personalizar formato de código

## Resolución de Problemas

### Error de Compilación

```bash
# Verificar sintaxis
make check

# Limpiar y recompilar
make clean
make build
```

### Paquetes Faltantes

```bash
# Instalar paquetes adicionales
sudo apt-get install texlive-latex-extra
sudo apt-get install texlive-fonts-extra
```

### Problemas con Minted

```bash
# Verificar Pygments
python3 -c "import pygments; print('OK')"

# Instalar si es necesario
pip3 install pygments
```

## Contribución

Para contribuir a la documentación:

1. Mantener el estilo consistente
2. Usar `minted` para bloques de código
3. Incluir ejemplos prácticos
4. Verificar sintaxis antes de commits
5. Actualizar esta documentación si es necesario

## Contacto

- **Proyecto:** Sistema de Telemetría MQTT-PostgreSQL
- **Institución:** LIESE (Laboratorio de Instrumentación Electrónica de Sistemas Espaciales)
- **Formato:** LaTeX con compilación automatizada

---

**Nota:** Esta documentación está diseñada para ser autocontenida y proporcionar toda la información necesaria para entender, implementar y mantener el sistema de telemetría.
