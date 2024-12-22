# Módulo Estudiantes - Odoo 17

Este módulo para Odoo 17 está diseñado para gestionar la información de estudiantes, programas e inscripciones. Incluye la creación de modelos, vistas de formulario, menús y un endpoint público para la consulta de inscripciones.

## Proceso de Creación

### 1. Instalación de Odoo 17 y PostgreSQL 16
- Instalé Odoo 17 y PostgreSQL 16, configurando un usuario `adminodoo` con la contraseña `odoo`.
- Configuré el servidor de Odoo en `localhost`.

### 2. Creación del Módulo
- Utilicé el siguiente comando para crear un nuevo módulo llamado "estudiantes" dentro de la carpeta `modules`:
    ```bash
    python odoo-bin scaffold estudiantes modules
    ```

### 3. Creación de los Modelos
- Se crearon los modelos `Alumno`, `Programa` e `Inscripción`, con sus respectivos campos y relaciones.

### 4. Creación de las Vistas de Formulario
- Se crearon vistas de formulario para los modelos `Alumno`, `Programa` e `Inscripción` para permitir la carga de información.
- Intenté crear vistas de tipo `tree`, pero debido a un error de compatibilidad, no pude implementarlas. Finalmente, solo dejé las vistas de formulario.

### 5. Creación de Menús
- Se añadieron menús para que las vistas fueran accesibles desde la interfaz de usuario de Odoo.

### 6. Edición del Archivo Manifest
- Se modificó el archivo `__manifest__.py` para incluir la información requerida sobre el módulo.
- Se añadieron las vistas creadas en el archivo de manifiesto.

### 7. Configuración de Usuarios, Grupos y Permisos
- Se configuraron usuarios, grupos y permisos en el archivo `ir.model.access` para controlar el acceso a los modelos y vistas.

### 8. Creación del Endpoint Público
- Se implementó un endpoint en el archivo `controllers.py` para permitir la lectura de la información de inscripciones mediante una petición GET:
    ```
    http://localhost:8069/estudiantes/programa_alumnos?programa_id=1
    ```

### 9. Configuración de Seguridad
- Se creó un archivo `security.xml` para definir un grupo de usuarios (`Estudiantes user`), el cual tiene permisos exclusivos para acceder a las vistas creadas.
- Se asignó este permiso en cada una de las vistas correspondientes.

### 10. Ejecución del Módulo
- Finalmente, se ejecutó el módulo con el siguiente comando:
    ```bash
    python odoo-bin -r adminodoo -w odoo --addons-path=addons,modules -d odoo
    ```

## Requisitos

- Odoo 17
- PostgreSQL 16

## Cómo Ejecutar el Módulo

1. Clona el repositorio:
    ```bash
    git clone <URL_del_repositorio>
    ```

2. Instala las dependencias de Odoo.

3. Ejecuta Odoo con el siguiente comando:
    ```bash
    python odoo-bin -r adminodoo -w odoo --addons-path=addons,modules -d odoo
    ```

