###CRUD de Libros con SOAP

Este proyecto implementa un sistema CRUD (Crear, Leer, Actualizar y Eliminar) de libros como un servicio SOAP, utilizando **Python**, **Spyne** y una base de datos **SQLite**.

### Requisitos

#### Instalar Python 3.11
1. Descargar Python 3.11 desde [Python.org](https://www.python.org/downloads/).
2. Asegúrate de agregar Python al PATH durante la instalación.
3. Verificar la versión instalada:
   ```bash
   python --version
   ```
   Debe mostrar `Python 3.11.x`.

### Instalar Dependencias
1. Instalar las librerías necesarias:
   ```bash
   pip install spyne zeep
   ```

## Estructura del Proyecto

```plaintext
CRUD_LIBROS/
├── database/
│   └── books.db           # Base de datos SQLite
├── server/
│   └── servidor.py        # Código del servidor SOAP
├── client/
│   └── cliente.py         # Código del cliente SOAP
├── README.md              # Documentación del proyecto
```

## Configuración y Ejecución

### Clonar el Repositorio
1. Clona este repositorio desde GitHub:
   ```bash
   git clone https://github.com/GiovannaSoria/CRUD_LIBROS.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd CRUD_LIBROS
   ```

### Configurar el Entorno
1. Crear un entorno virtual:
   ```bash
   python -m venv env
   ```
2. Activar el entorno virtual:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source env/bin/activate
     ```
3. Instalar las dependencias:
   ```bash
   pip install spyne zeep
   ```

### Ejecutar el Servidor
1. Navegar al directorio del servidor:
   ```bash
   cd server
   ```
2. Iniciar el servidor:
   ```bash
   python servidor.py
   ```
3. Acceder al WSDL en el navegador para verificar:
   ```plaintext
   http://127.0.0.1:8000/?wsdl
   ```

### Probar el Cliente
1. Navegar al directorio del cliente:
   ```bash
   cd client
   ```
2. Ejecutar el cliente para interactuar con el servidor:
   ```bash
   python cliente.py
   ```

## Pasos para Ejecutar en Otra Computadora

1. Clona este repositorio en la nueva computadora:
   ```bash
   git clone https://github.com/GiovannaSoria/CRUD_LIBROS.git
   ```
2. Ingresa al directorio del proyecto:
   ```bash
   cd CRUD_LIBROS
   ```
3. Configura un entorno virtual:
   ```bash
   python -m venv env
   ```
4. Activa el entorno virtual:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     source env/bin/activate
     ```
5. Instala las dependencias:
   ```bash
   pip install spyne zeep
   ```
6. Sigue los pasos para ejecutar el servidor y el cliente según la sección anterior.

## Operaciones Disponibles

### Agregar un Libro
- **Input**:
  - Título: `string`
  - Autor: `string`
  - Género: `string`
- **Output**:
  - Mensaje confirmando la adición.

### Listar Libros
- **Input**: Ninguno.
- **Output**:
  - Lista de libros.

### Obtener un Libro por ID
- **Input**:
  - ID del libro: `integer`
- **Output**:
  - Detalles del libro o mensaje de error.

### Editar un Libro
- **Input**:
  - ID: `integer`
  - Título: `string`
  - Autor: `string`
  - Género: `string`
- **Output**:
  - Mensaje confirmando la edición.

### Eliminar un Libro
- **Input**:
  - ID: `integer`
- **Output**:
  - Mensaje confirmando la eliminación.

## Estructura de la Base de Datos

La tabla `books` tiene la siguiente estructura:

| Campo   | Tipo     | Descripción                   |
|---------|----------|-------------------------------|
| `id`    | INTEGER  | ID único del libro.           |
| `title` | TEXT     | Título del libro.             |
| `author`| TEXT     | Autor del libro.              |
| `genre` | TEXT     | Género del libro.             |

