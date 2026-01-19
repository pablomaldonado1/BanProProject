# Projecto Postulacion BanPro

Proyecto desarrollado como parte de una postulación laboral.  
Consiste en un Backend Django con API REST para la gestión de empleados, permitiendo crear, listar, actualizar y desactivar empleados. Ademas contiene Logs en caso de error

## Tecnologías
- Python 3.14
- Django
- Django REST Framework
- PostgreSQL

---

## Requisitos
- Python 3.10+
- pip
- virtualenv
- PostgreSQL 

---

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/pablomaldonado1/BanProProject.git
cd BanProProject
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Mac / Linux
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Crear migraciones
```bash
# se debe configurar variables de entoro si se quiere usar posgres
# ver mas abajo variables de enterono
python manage.py makemigrations
```
5. Ejecutar migraciones
```bash
python manage.py migrate
```

---
## Variables de entorno

El proyecto utiliza un archivo `.env` para manejar configuraciones sensibles como las credenciales de la base de datos.
1. crea archivo .env

2. usa el archico .env.example para ver como debes configurar tus variables de entorno con tu propio postgresql
```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

```
3. Asegurarse de que PostgreSQL esté corriendo y que la base de datos exista antes de ejecutar las migraciones.

---
## Ejecucion

```bash
python manage.py runserver
```

---


## Endpoints principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | /employee/list/        | Listar empleados |
| POST   | /employee/create/        | Crear empleado |
| GET    | /employee/get-employee/  | Obtener empleado |
| PUT    | /employee/update-employee/{id}/   | Actualizar empleado |
| DELETE | /employee/delete/{id}/   | Desactivar empleado |



