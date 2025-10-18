# TP13

/DB/ CREATE DATABASE biblioteca;
USE biblioteca;


CREATE TABLE autores 
(id INT IDENTITY(1,1) PRIMARY KEY,
nombre VARCHAR(100),
nacionalidad VARCHAR(100),
)

CREATE TABLE libros 
(id INT IDENTITY(1,1) PRIMARY KEY,
titulo VARCHAR(100),
genero VARCHAR(50),
año INT,
id_autor INT,
FOREIGN KEY (id_autor) REFERENCES autores(id)
)


📚 Proyecto: Biblioteca - Base de Datos 1 (IPET 247)

Aplicación de consola desarrollada en Python con conexión a SQL Server.  
Permite gestionar una base de datos de autores y libros.

⚙️Instalación y configuración

Requisitos
- Python 3.x instalado  
- SQL Server 2008 o superior  
- Visual Studio Code (recomendado)

Instalar el conector para SQL Server
En la terminal de VS Code:
Escribes pip install pyodbc asi podras instalar el conector (aclaro que yo utilize sql server magnament studio)


Crear la base de datos

En SQL Server Management Studio (SSMS):

Ejecutar el script /db/biblioteca.sql

Configurar la conexión en el código

En el archivo app.bibliotec.py, verificar:

conexion = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-SAC7IAI;'
    'DATABASE=biblioteca;'
    'Trusted_Connection=yes;'
)


Cambiar SERVER si tu nombre de servidor es diferente.

Este es el formato de menu principal del programa

========= MENÚ PRINCIPAL =========
1. Insertar autor
2. Insertar libro
3. Listar autores
4. Listar libros
5. Actualizar libro
6. Eliminar autor
0. Salir

Ezequiel Anaya
6º E - IPET 247
Año 2025
(no puse el codigo de python del programa ya q es muy grande lo agregue como archivo ya mensionado antes como app.biblioteca.py)
