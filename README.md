# EduDashboard - Proyecto Educativo con Django

EduDashboard es una aplicación educativa desarrollada con **Django 5.1.3** y **Bootstrap 4**, diseñada para gestionar estudiantes, cursos y reportes. Este proyecto incluye una interfaz profesional con un diseño dinámico, efectos visuales y un menú de navegación interactivo.

---

## **Características Principales**
1. **Inicio**: Página de bienvenida con un mensaje motivador y enlaces para explorar el contenido.
2. **Gestión de Estudiantes**: Listado de estudiantes con datos básicos (nombre, apellido, edad, email).
3. **Gestión de Cursos**: Listado de cursos con detalles como nombre, descripción y duración.
4. **Reportes**: Visualización de reportes educativos.
5. **Efectos Dinámicos**:
   - Transición suave del contenido principal al cargar.
   - Efectos de hover en el menú lateral.
   - Navegación interactiva con resaltado dinámico de la sección activa.

---

## **Requisitos Previos**
- **Python 3.8 o superior**.
- **pip** para la gestión de paquetes.
- Un entorno virtual configurado (opcional, pero recomendado).

---

## **Instrucciones de Instalación**

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd edu_dashboard
   ```

2. **Configura el entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos**:
   - Asegúrate de que el archivo `settings.py` utiliza la base de datos SQLite por defecto.
   - Ejecuta las migraciones para crear las tablas necesarias:
     ```bash
     python manage.py migrate
     ```

5. **Crea un superusuario (opcional)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicia el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

   Accede a la aplicación en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## **Uso de la Aplicación**

### **Páginas Disponibles**
1. **Inicio** (`/`): Página principal con un saludo y enlaces rápidos.
2. **Estudiantes** (`/estudiantes/`): Listado de estudiantes registrados.
3. **Cursos** (`/cursos/`): Detalles de los cursos disponibles.
4. **Reportes** (`/reportes/`): Visualización de reportes.

### **Interactividad**
- **Navegación lateral dinámica**: Resalta la sección activa.
- **Efectos visuales**:
  - Los enlaces del menú lateral cambian de estilo al pasar el cursor.
  - El contenido principal aparece con una transición suave al cargar.

---

## **Estructura del Proyecto**

```plaintext
edu_dashboard/
│
├── edu_project/                  # Configuración principal de Django
│   ├── settings.py               # Configuración del proyecto
│   ├── urls.py                   # Rutas principales
│   └── ...
│
├── edu_app/                      # Aplicación inicial (Inicio)
│   ├── views.py                  # Vista del saludo principal
│   ├── urls.py                   # Rutas de la app
│   └── templates/index.html      # Plantilla del saludo inicial
│
├── estudiantes/                  # Gestión de estudiantes
│   ├── models.py                 # Modelo Estudiante
│   ├── views.py                  # Vista del listado de estudiantes
│   ├── urls.py                   # Rutas de la app
│   └── templates/estudiantes/    # Plantillas de estudiantes
│
├── cursos/                       # Gestión de cursos
│   ├── models.py                 # Modelo Curso
│   ├── views.py                  # Vista del listado de cursos
│   ├── urls.py                   # Rutas de la app
│   └── templates/cursos/         # Plantillas de cursos
│
├── reportes/                     # Gestión de reportes
│   ├── models.py                 # Modelo Reporte
│   ├── views.py                  # Vista del listado de reportes
│   ├── urls.py                   # Rutas de la app
│   └── templates/reportes/       # Plantillas de reportes
│
├── static/                       # Archivos estáticos
│   ├── css/style.css             # Estilos personalizados
│   ├── js/scripts.js             # Scripts de interactividad
│   └── ...
└── templates/                    # Plantillas globales
    └── base.html                 # Plantilla base del proyecto
```

---

## **Personalización**

### **Estilos Personalizados**
Los estilos están definidos en `static/css/style.css`. Puedes modificar:
- **Hover del menú lateral**.
- **Transición del contenido principal**.

### **Scripts de Interactividad**
Los efectos dinámicos se controlan desde `static/js/scripts.js`.

---
