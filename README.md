# 🚀 LIESE Website

![LIESE Logo](src/web/static/web/images/LogoUnamSat2.png)

Sitio web oficial del Laboratorio de Instrumentación Espacial (LIESE) de la UNAM. Una plataforma moderna y dinámica que presenta las actividades, proyectos y oportunidades del laboratorio.

## 🌟 Características

- **Sistema de Eventos**: Calendario interactivo con gestión de eventos espaciales
- **Gestión de Artículos**: Publicación y visualización de artículos científicos
- **Sección de Proyectos**: Showcase de proyectos espaciales actuales y pasados
- **Líderes de Proyecto**: Perfiles detallados del equipo de investigación
- **Portal de Oportunidades**: Sistema de registro para:
  - Tesis
  - Investigación
  - Servicio Social
  - Programas de Maestría
- **Sistema de Verificación**: Verificación de correo electrónico para solicitudes
- **Actividades Timeline**: Vista cronológica de todas las actividades del laboratorio

## 🛠️ Tecnologías

- **Backend**: Django 5.1.6
- **Frontend**: Bootstrap 5.3.3
- **Base de Datos**: SQLite3
- **Email**: SMTP (Gmail)

## 📁 Estructura del Proyecto

```
liese-website/
├── src/                    # Código fuente principal
│   ├── liese/             # Configuración principal de Django
│   │   ├── settings.py    # Configuraciones del proyecto
│   │   ├── urls.py        # URLs principales
│   │   └── wsgi.py        # Configuración WSGI
│   │
│   ├── web/               # Aplicación principal
│   │   ├── static/        # Archivos estáticos
│   │   ├── templates/     # Plantillas HTML
│   │   ├── models.py      # Modelos de datos
│   │   ├── views.py       # Vistas
│   │   ├── forms.py       # Formularios
│   │   └── urls.py        # URLs de la aplicación
│   │
│   ├── media/             # Archivos subidos por usuarios
│   └── manage.py          # Script de gestión de Django
│
└── requirements.txt        # Dependencias del proyecto
```

## ⚙️ Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/e1th4nUwU/liese-website.git
   cd liese-website
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   - Crear archivo `.env` en la raíz del proyecto
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

5. **Realizar migraciones**
   ```bash
   cd src
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

## 📧 Configuración de Correo

El sistema utiliza Gmail SMTP para enviar correos de verificación. Para configurarlo:

1. Activar verificación en dos pasos en tu cuenta de Gmail
2. Generar una contraseña de aplicación
3. Usar esas credenciales en el archivo `.env`

## 🔐 Seguridad

- Implementación de CSRF tokens
- Verificación de correo electrónico
- Tokens de seguridad temporales
- Sanitización de entrada de datos

## 🌐 Despliegue

### Preparación del Entorno

1. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Aplicar migraciones:
   ```bash
   cd src
   python manage.py migrate
   ```

### Configuración del Servicio

El proyecto incluye un archivo `liese-website.service` para systemd:

```ini
[Unit]
Description=Liese Django Runserver
After=network.target

[Service]
User=saul
Group=saul
WorkingDirectory=/home/saul/liese-website
ExecStart=/home/saul/liese-website/venv/bin/python /home/saul/liese-website/src/manage.py runserver 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Para configurar el servicio:

1. Ajustar las rutas y usuario en el archivo service según tu entorno
2. Copiar el archivo al directorio de systemd:
   ```bash
   sudo cp liese-website.service /etc/systemd/system/
   ```
3. Habilitar e iniciar el servicio:
   ```bash
   sudo systemctl enable liese-website
   sudo systemctl start liese-website
   ```
4. Verificar el estado:
   ```bash
   sudo systemctl status liese-website
   ```

## 🤝 Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m '[FLAG] Descripción de los cambios'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Posibles /Futuras mejoras
- ⚙️ Certificación SSL
- 🔒 Mejoras de Ciberseguridad
- 💰 Botón de Patrocinio (Stripe, PayPal)
- 🛠️ CI/CD (GitHub Actions, Travis CI)
- 🌍 Soporte Multiidioma
- 📊 Dashboard Administrativo
- 🔍 Sistema de Búsqueda
- 📅 Integración con Google Calendar
- 🌓 Modo Claro/Oscuro
- 💭 Sistema de Comentarios
- 🧪 Pruebas Unitarias y de Integración
- 📦 Dockerización
- 📈 Análisis y Monitoreo (Google Analytics, Sentry)

## 👤 Autor

**Jorge Eithan Treviño Selles**

- GitHub: [@e1th4nUwU](https://github.com/e1th4nUwU)

Hecho con 💙 para LIESE